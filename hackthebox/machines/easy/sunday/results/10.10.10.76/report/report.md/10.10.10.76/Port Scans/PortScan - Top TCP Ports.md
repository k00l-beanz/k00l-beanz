```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_quick_tcp_nmap.xml" 10.10.10.76
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_quick_tcp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Mon Oct  3 22:25:34 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_quick_tcp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_quick_tcp_nmap.xml 10.10.10.76
Increasing send delay for 10.10.10.76 from 0 to 5 due to 11 out of 16 dropped probes since last increase.
Increasing send delay for 10.10.10.76 from 5 to 10 due to 14 out of 34 dropped probes since last increase.
Warning: 10.10.10.76 giving up on port because retransmission cap hit (6).
adjust_timeouts2: packet supposedly had rtt of -115674 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -115674 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -139793 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -139793 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -138877 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -138877 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.76
Host is up, received user-set (0.015s latency).
Scanned at 2022-10-03 22:25:35 EDT for 106s
Not shown: 813 closed tcp ports (reset), 178 filtered tcp ports (no-response), 8 filtered tcp ports (host-unreach)
PORT    STATE SERVICE REASON         VERSION
111/tcp open  rpcbind syn-ack ttl 63 2-4 (RPC #100000)
Aggressive OS guesses: Oracle Solaris 11 (94%), Oracle Solaris 10 (93%), Oracle Solaris 11 or OpenIndiana (93%), Sun Solaris 11.3 (92%), Nexenta OS 3.0 - 3.1.2 (OpenSolaris snv_130 - snv_134f) (92%), Sun Solaris 11 (snv_151a) or OpenIndiana oi_147 (92%), Sun Solaris 11 (snv_151a) or OpenIndiana oi_147 - oi_151a (92%), Sun OpenSolaris snv_129 (91%), Solaris 12 (91%), Sun Storage 7410 NAS device (90%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=10/3%OT=111%CT=3%CU=38224%PV=Y%DS=2%DC=I%G=Y%TM=633B9A
OS:09%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=106%CI=I%II=I%TS=7)SEQ(SP=
OS:101%GCD=1%ISR=106%TI=I%CI=I%II=I%TS=7)SEQ(SP=101%GCD=1%ISR=106%II=I%TS=7
OS:)SEQ(SP=101%GCD=1%ISR=106%TI=I%CI=I%II=I%SS=S%TS=7)OPS(O1=ST11M539NW2%O2
OS:=ST11M539NW2%O3=NNT11M539NW2%O4=ST11M539NW2%O5=ST11M539NW2%O6=ST11M539)W
OS:IN(W1=FB06%W2=FB06%W3=FA38%W4=FA3B%W5=FA3B%W6=FFF7)ECN(R=Y%DF=Y%T=40%W=F
OS:AB0%O=M539NNSNW2%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T
OS:3(R=Y%DF=Y%T=40%W=FA09%S=O%A=S+%F=AS%O=ST11M539NW2%RD=0%Q=)T4(R=Y%DF=Y%T
OS:=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=N%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=
OS:0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF
OS:=N%T=FF%IPL=70%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=Y%T=FF%
OS:CD=S)

Uptime guess: 0.001 days (since Mon Oct  3 22:25:37 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: Incremental

TRACEROUTE (using port 9898/tcp)
HOP RTT      ADDRESS
1   13.30 ms 10.10.14.1
2   ... 30

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Oct  3 22:27:21 2022 -- 1 IP address (1 host up) scanned in 106.94 seconds

```
