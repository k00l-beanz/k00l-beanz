```bash
nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.111
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/tcp_445_smb_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/tcp_445_smb_nmap.txt):

```
# Nmap 7.92 scan initiated Wed Nov 16 16:42:44 2022 as: nmap -vv --reason -Pn -T4 -sV -p 445 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/tcp_445_smb_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/xml/tcp_445_smb_nmap.xml 10.10.10.111
Nmap scan report for 10.10.10.111
Host is up, received user-set (0.011s latency).
Scanned at 2022-11-16 16:42:44 EST for 310s

PORT    STATE SERVICE     REASON         VERSION
445/tcp open  netbios-ssn syn-ack ttl 63 Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
Service Info: Host: FROLIC

Host script results:
| smb-enum-domains: 
|   Builtin
|     Groups: n/a
|     Users: n/a
|     Creation time: unknown
|     Passwords: min length: 5; min age: n/a days; max age: n/a days; history: n/a passwords
|     Account lockout disabled
|   FROLIC
|     Groups: n/a
|     Users: n/a
|     Creation time: unknown
|     Passwords: min length: 5; min age: n/a days; max age: n/a days; history: n/a passwords
|_    Account lockout disabled
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.10.111\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (frolic server (Samba, Ubuntu))
|     Users: 7
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.10.111\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: frolic
|   NetBIOS computer name: FROLIC\x00
|   Domain name: \x00
|   FQDN: frolic
|_  System time: 2022-11-17T03:12:55+05:30
|_smb-system-info: ERROR: Script execution failed (use -d to debug)
| smb-enum-sessions: 
|_  <nobody>
| smb-mbenum: 
|   DFS Root
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Master Browser
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Print server
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Server
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Server service
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Unix server
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Windows NT/2000/XP/2003 server
|     FROLIC  0.0  frolic server (Samba, Ubuntu)
|   Workstation
|_    FROLIC  0.0  frolic server (Samba, Ubuntu)
|_smb-print-text: false
| smb2-time: 
|   date: 2022-11-16T21:42:55
|_  start_date: N/A
|_smb-vuln-ms10-061: false
| nbstat: NetBIOS name: FROLIC, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   FROLIC<00>           Flags: <unique><active>
|   FROLIC<03>           Flags: <unique><active>
|   FROLIC<20>           Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
| smb2-capabilities: 
|   2.0.2: 
|     Distributed File System
|   2.1: 
|     Distributed File System
|     Multi-credit operations
|   3.0: 
|     Distributed File System
|     Multi-credit operations
|   3.0.2: 
|     Distributed File System
|     Multi-credit operations
|   3.1.1: 
|     Distributed File System
|_    Multi-credit operations
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.0.2
|     2.1
|     3.0
|     3.0.2
|_    3.1.1

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Nov 16 16:47:54 2022 -- 1 IP address (1 host up) scanned in 309.90 seconds

```
