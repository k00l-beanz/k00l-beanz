```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/xml/_quick_tcp_nmap.xml" 10.10.10.161
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/_quick_tcp_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Jul 26 18:50:20 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/_quick_tcp_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/xml/_quick_tcp_nmap.xml 10.10.10.161
adjust_timeouts2: packet supposedly had rtt of -193219 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -193219 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -519709 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -519709 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.161
Host is up, received user-set (0.013s latency).
Scanned at 2022-07-26 18:50:21 EDT for 31s
Not shown: 989 closed tcp ports (reset)
PORT     STATE SERVICE      REASON          VERSION
53/tcp   open  domain       syn-ack ttl 127 Simple DNS Plus
88/tcp   open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2022-07-26 22:57:51Z)
135/tcp  open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp  open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
389/tcp  open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds (workgroup: HTB)
464/tcp  open  kpasswd5?    syn-ack ttl 127
593/tcp  open  ncacn_http   syn-ack ttl 127 Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped   syn-ack ttl 127
3268/tcp open  ldap         syn-ack ttl 127 Microsoft Windows Active Directory LDAP (Domain: htb.local, Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped   syn-ack ttl 127
OS fingerprint not ideal because: Didn't receive UDP response. Please try again with -sSU
Aggressive OS guesses: Microsoft Windows Server 2016 build 10586 - 14393 (93%), Microsoft Windows Server 2016 (92%), Microsoft Windows Server 2012 (91%), Microsoft Windows Vista SP1 (91%), Microsoft Windows 10 (89%), Microsoft Windows 10 10586 - 14393 (89%), Microsoft Windows 10 1507 - 1607 (89%), Microsoft Windows 10 1511 (89%), Microsoft Windows 10 1607 (89%), Microsoft Windows Server 2012 R2 (89%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=7/26%OT=53%CT=1%CU=%PV=Y%DS=2%DC=T%G=N%TM=62E06FCC%P=x86_64-pc-linux-gnu)
SEQ(SP=FE%GCD=1%ISR=10F%II=I%TS=A)
SEQ(SP=FE%GCD=1%ISR=10F%CI=RI%TS=A)
OPS(O1=M539NW8ST11%O2=M539NW8ST11%O3=M539NW8NNT11%O4=M539NW8ST11%O5=M539NW8ST11%O6=M539ST11)
WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)
ECN(R=Y%DF=Y%TG=80%W=2000%O=M539NW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=Y%DF=Y%TG=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)
T3(R=N)
T3(R=Y%DF=Y%TG=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)
T4(R=Y%DF=Y%TG=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
T5(R=N)
T5(R=Y%DF=Y%TG=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=N)
T6(R=Y%DF=Y%TG=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
T7(R=N)
T7(R=Y%DF=Y%TG=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Uptime guess: 1.030 days (since Mon Jul 25 18:07:31 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=254 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: Host: FOREST; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 2h27m23s, deviation: 4h02m30s, median: 7m22s
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2022-07-26T22:58:06
|_  start_date: 2022-07-25T22:15:12
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: FOREST
|   NetBIOS computer name: FOREST\x00
|   Domain name: htb.local
|   Forest name: htb.local
|   FQDN: FOREST.htb.local
|_  System time: 2022-07-26T15:58:07-07:00
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 45805/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 32753/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 12357/udp): CLEAN (Timeout)
|   Check 4 (port 44587/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked

TRACEROUTE (using port 993/tcp)
HOP RTT      ADDRESS
1   14.08 ms 10.10.14.1
2   14.46 ms 10.10.10.161

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul 26 18:50:52 2022 -- 1 IP address (1 host up) scanned in 31.72 seconds

```
