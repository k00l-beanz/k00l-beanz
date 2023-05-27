```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_full_tcp_nmap.xml" 10.10.10.88
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_full_tcp_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_full_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Sep 29 19:07:57 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_full_tcp_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_full_tcp_nmap.xml 10.10.10.88
adjust_timeouts2: packet supposedly had rtt of -624302 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -624302 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -628445 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -628445 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -307055 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -307055 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -588141 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -588141 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -479520 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -479520 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -472409 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -472409 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.88
Host is up, received user-set (0.014s latency).
Scanned at 2022-09-29 19:07:58 EDT for 48s
Not shown: 65534 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
| http-robots.txt: 5 disallowed entries 
| /webservices/tar/tar/source/ 
| /webservices/monstra-3.0.4/ /webservices/easy-file-uploader/ 
|_/webservices/developmental/ /webservices/phpmyadmin/
|_http-title: Landing Page
|_http-server-header: Apache/2.4.18 (Ubuntu)
Aggressive OS guesses: Linux 3.2 - 4.9 (95%), Linux 3.16 (95%), Linux 3.18 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.1 (93%), Linux 3.2 (93%), Linux 3.10 - 4.11 (93%), Linux 3.12 (93%), Linux 3.13 (93%), Linux 3.13 - 3.16 (93%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=9/29%OT=80%CT=1%CU=30673%PV=Y%DS=2%DC=T%G=Y%TM=6336257
OS:E%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=10C%TI=Z%CI=I%II=I%TS=A)OPS
OS:(O1=M539ST11NW7%O2=M539ST11NW7%O3=M539NNT11NW7%O4=M539ST11NW7%O5=M539ST1
OS:1NW7%O6=M539ST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)ECN
OS:(R=Y%DF=Y%TG=40%W=7210%O=M539NNSNW7%CC=Y%Q=)ECN(R=Y%DF=Y%T=40%W=7210%O=M
OS:539NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%TG=40%S=O%A=S+%F=AS%RD=0%Q=)T1(R=Y%DF=Y%T=
OS:40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T4(R=Y%DF=Y%T=40%W=0%S=O%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%TG=4
OS:0%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=%RD=0
OS:%Q=)T6(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=
OS:O%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T7(R
OS:=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)U1(R=N)U1(R=Y%DF=N%T=40%IPL=164
OS:%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%TG=40%CD=S)IE(R=Y%D
OS:FI=N%T=40%CD=S)

Uptime guess: 16.655 days (since Tue Sep 13 03:25:26 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 256/tcp)
HOP RTT      ADDRESS
1   19.25 ms 10.10.14.1
2   19.78 ms 10.10.10.88

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Sep 29 19:08:46 2022 -- 1 IP address (1 host up) scanned in 48.37 seconds

```
