```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/xml/_full_tcp_nmap.xml" 10.10.10.180
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_full_tcp_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_full_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Aug  2 14:45:56 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_full_tcp_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/xml/_full_tcp_nmap.xml 10.10.10.180
adjust_timeouts2: packet supposedly had rtt of -134676 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -134676 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -369553 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -369553 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -672771 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -672771 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.180
Host is up, received user-set (0.014s latency).
Scanned at 2022-08-02 14:45:57 EDT for 205s
Not shown: 65519 closed tcp ports (reset)
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
Aggressive OS guesses: Microsoft Windows 10 1709 - 1909 (93%), Microsoft Windows Server 2012 (93%), Microsoft Windows Vista SP1 (92%), Microsoft Windows Longhorn (92%), Microsoft Windows Server 2016 (92%), Microsoft Windows 10 1709 - 1803 (90%), Microsoft Windows 10 1809 - 1909 (90%), Microsoft Windows Server 2012 R2 (90%), Microsoft Windows Server 2012 R2 Update 1 (90%), Microsoft Windows Server 2016 build 10586 - 14393 (90%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=8/2%OT=21%CT=1%CU=35241%PV=Y%DS=2%DC=T%G=Y%TM=62E971B2
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=109%CI=I%II=I%TS=U)SEQ(SP=10
OS:6%GCD=1%ISR=109%II=I%TS=U)OPS(O1=M539NW8NNS%O2=M539NW8NNS%O3=M539NW8%O4=
OS:M539NW8NNS%O5=M539NW8NNS%O6=M539NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%
OS:W5=FFFF%W6=FF70)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M539NW8NNS%CC=Y%Q=)T1(R=Y%DF=
OS:Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q
OS:=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%
OS:A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%
OS:DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%
OS:O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD
OS:=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: 0s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 45222/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 36184/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 44964/udp): CLEAN (Timeout)
|   Check 4 (port 15893/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time: 
|   date: 2022-08-02T18:48:53
|_  start_date: N/A
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required

TRACEROUTE (using port 5900/tcp)
HOP RTT      ADDRESS
1   18.94 ms 10.10.14.1
2   19.38 ms 10.10.10.180

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  2 14:49:22 2022 -- 1 IP address (1 host up) scanned in 206.26 seconds

```
