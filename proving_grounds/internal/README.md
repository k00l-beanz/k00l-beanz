# Internal
## Information Gathering
#### Ports/Services
53/tcp      domain             Microsoft DNS 6.0.6001 (17714650) (Windows Server 2008 SP1)

135/tcp     msrpc              Microsoft Windows RPC

139/tcp     netbios-ssn        Microsoft Windows netbios-ssn

445/tcp     microsoft-ds       Windows Server (R) 2008 Standard 6001 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)

3389/tcp    ssl/ms-wbt-server?

5357/tcp    http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

## Enumeration
### Nmap scan
```bash
PORT      STATE SERVICE            VERSION
53/tcp    open  domain             Microsoft DNS 6.0.6001 (17714650) (Windows Server 2008 SP1)
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.0.6001 (17714650)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Windows Server (R) 2008 Standard 6001 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
| ssl-cert: Subject: commonName=internal
| Not valid before: 2022-07-27T05:16:05
|_Not valid after:  2023-01-26T05:16:05
|_ssl-date: 2023-01-10T02:43:43+00:00; +1s from scanner time.
5357/tcp  open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49156/tcp open  msrpc              Microsoft Windows RPC
49157/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC

Host script results:
| smb2-time: 
|   date: 2023-01-10T02:43:33
|_  start_date: 2022-07-28T05:16:03
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.0.2: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows Server (R) 2008 Standard 6001 Service Pack 1 (Windows Server (R) 2008 Standard 6.0)
|   OS CPE: cpe:/o:microsoft:windows_server_2008::sp1
|   Computer name: internal
|   NetBIOS computer name: INTERNAL\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-01-09T18:43:33-08:00
|_nbstat: NetBIOS name: INTERNAL, NetBIOS user: <unknown>, NetBIOS MAC: 00:50:56:bf:ee:87 (VMware)
|_clock-skew: mean: 2h00m00s, deviation: 4h00m00s, median: 0s
```

- Running vulnerability scan on SMB
```bash
sudo nmap -p139,445 --script=smb-vuln* 192.168.185.40 -Pn -oN smb_vuln_scan.nmap
PORT    STATE SERVICE
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds

Host script results:
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: TIMEOUT
|_smb-vuln-ms10-054: false
| smb-vuln-cve2009-3103: 
|   VULNERABLE:
|   SMBv2 exploit (CVE-2009-3103, Microsoft Security Advisory 975497)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2009-3103
|           Array index error in the SMBv2 protocol implementation in srv2.sys in Microsoft Windows Vista Gold, SP1, and SP2,
|           Windows Server 2008 Gold and SP2, and Windows 7 RC allows remote attackers to execute arbitrary code or cause a
|           denial of service (system crash) via an & (ampersand) character in a Process ID High header field in a NEGOTIATE
|           PROTOCOL REQUEST packet, which triggers an attempted dereference of an out-of-bounds memory location,
|           aka "SMBv2 Negotiation Vulnerability."
|           
|     Disclosure date: 2009-09-08
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3103
|_      http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-3103
```

### 53/tcp Microsoft DNS 6.0.6001
- Attempted `dig`
```bash
dig axfr @192.168.185.40
; <<>> DiG 9.18.6-2-Debian <<>> axfr @192.168.185.40
; (1 server found)
;; global options: +cmd
;; Query time: 19 msec
;; SERVER: 192.168.185.40#53(192.168.185.40) (UDP)
;; WHEN: Mon Jan 09 21:45:33 EST 2023
;; MSG SIZE  rcvd: 40
```

### 135/tcp Microsoft Windows RPC
- Attempting to use `rpcclient` to enumerate
```bash
rpcclient -U '' -N 192.168.185.40
rpcclient $> enumdomgroups
do_cmd: Could not initialise samr. Error was NT_STATUS_ACCESS_DENIED
```

### 139/tcp, 445/tcp Microsoft Windows netbios-ssn, Windows Server (R) 2008 Standard 6001 Service Pack 1
- Attempting `smbmap`
```bash
smbmap -u '' -p '' -H 192.168.185.40
[+] IP: 192.168.185.40:445      Name: 192.168.185.40 
```

- Running `enum4linux`
	- Server allows sessions using username '', password ''

## Exploitation
- This server is vulnerable to CVE-2009-3103 which is an SMBv2 exploit
- I load up `windows/smb/ms09_050_smb2_negotiate_func_index` in `msfconsole` 
	- After setting the options and running, I caught a reverse shell as `NT AUTHORITY\SYSTEM`
