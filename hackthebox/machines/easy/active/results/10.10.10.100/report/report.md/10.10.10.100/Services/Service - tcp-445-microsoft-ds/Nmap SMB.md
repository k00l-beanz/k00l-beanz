```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.100
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.92 scan initiated Mon Sep 19 18:45:09 2022 as: nmap -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.10.100
Nmap scan report for 10.10.10.100
Host is up, received user-set (0.017s latency).
Scanned at 2022-09-19 18:45:10 EDT for 41s

PORT    STATE SERVICE       REASON          VERSION
445/tcp open  microsoft-ds? syn-ack ttl 127
|_smb-enum-services: ERROR: Script execution failed (use -d to debug)

Host script results:
|_smb-vuln-ms10-061: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-capabilities: 
|   2.0.2: 
|     Distributed File System
|   2.1: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
| smb-protocols: 
|   dialects: 
|     2.0.2
|_    2.1
| smb-mbenum: 
|_  ERROR: Failed to connect to browser service: Could not negotiate a connection:SMB: Failed to receive bytes: ERROR
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-09-19T22:45:25
|_  start_date: 2022-09-19T03:56:24
|_smb-print-text: false

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Sep 19 18:45:51 2022 -- 1 IP address (1 host up) scanned in 41.87 seconds

```
