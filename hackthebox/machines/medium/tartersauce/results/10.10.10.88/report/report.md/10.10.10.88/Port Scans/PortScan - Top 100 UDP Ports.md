```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_top_100_udp_nmap.xml" 10.10.10.88
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_top_100_udp_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Sep 29 19:07:57 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_top_100_udp_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_top_100_udp_nmap.xml 10.10.10.88
Warning: 10.10.10.88 giving up on port because retransmission cap hit (6).
Increasing send delay for 10.10.10.88 from 100 to 200 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.10.88 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.10.88 from 400 to 800 due to 11 out of 13 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -107651 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -107651 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -324961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -324961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -493999 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -493999 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -524752 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -524752 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -183537 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -183537 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.88
Host is up, received user-set (0.032s latency).
Scanned at 2022-09-29 19:07:58 EDT for 218s
Not shown: 81 closed udp ports (port-unreach)
PORT      STATE         SERVICE        REASON      VERSION
7/udp     open|filtered echo           no-response
67/udp    open|filtered dhcps          no-response
68/udp    open|filtered dhcpc          no-response
443/udp   open|filtered https          no-response
593/udp   open|filtered http-rpc-epmap no-response
996/udp   open|filtered vsinet         no-response
1026/udp  open|filtered win-rpc        no-response
1718/udp  open|filtered h225gatedisc   no-response
1719/udp  open|filtered h323gatestat   no-response
1813/udp  open|filtered radacct        no-response
1900/udp  open|filtered upnp           no-response
4500/udp  open|filtered nat-t-ike      no-response
5632/udp  open|filtered pcanywherestat no-response
9200/udp  open|filtered wap-wsp        no-response
30718/udp open|filtered unknown        no-response
31337/udp open|filtered BackOrifice    no-response
|_backorifice-info: ERROR: Script execution failed (use -d to debug)
49181/udp open|filtered unknown        no-response
49190/udp open|filtered unknown        no-response
65024/udp open|filtered unknown        no-response
Device type: storage-misc|phone|general purpose|media device
Running: Buffalo embedded, Google Android 6.X, Linux 2.6.X|3.X, Sony embedded
OS CPE: cpe:/o:google:android:6.0.1 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3.13 cpe:/o:google:android
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=9/29%OT=%CT=%CU=9%PV=Y%DS=2%DC=T%G=N%TM=63362628%P=x86_64-pc-linux-gnu)
SEQ(CI=I)
SEQ(CI=I%II=I)
T5(R=Y%DF=Y%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%TG=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=O%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%TG=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)
U1(R=N)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%TG=40%CD=S)
IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops

TRACEROUTE (using port 139/udp)
HOP RTT      ADDRESS
1   37.22 ms 10.10.14.1
2   39.03 ms 10.10.10.88

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Sep 29 19:11:36 2022 -- 1 IP address (1 host up) scanned in 218.72 seconds

```
