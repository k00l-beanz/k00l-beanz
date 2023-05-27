```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/xml/_top_100_udp_nmap.xml" 10.10.10.117
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/_top_100_udp_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Sep 27 22:17:11 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/_top_100_udp_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/xml/_top_100_udp_nmap.xml 10.10.10.117
Warning: 10.10.10.117 giving up on port because retransmission cap hit (6).
Increasing send delay for 10.10.10.117 from 100 to 200 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.10.117 from 200 to 400 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.117 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 10.10.10.117
Host is up, received user-set (0.014s latency).
Scanned at 2022-09-27 22:17:18 EDT for 237s
Not shown: 85 closed udp ports (port-unreach)
PORT      STATE         SERVICE        REASON               VERSION
68/udp    open|filtered dhcpc          no-response
111/udp   open          rpcbind        udp-response ttl 63  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          37435/tcp   status
|   100024  1          42129/udp6  status
|   100024  1          50128/udp   status
|_  100024  1          50871/tcp6  status
138/udp   open|filtered netbios-dgm    no-response
514/udp   open|filtered syslog         no-response
631/udp   open|filtered ipp            no-response
1030/udp  open|filtered iad1           no-response
1900/udp  open|filtered upnp           no-response
2222/udp  open|filtered msantipiracy   no-response
3456/udp  open|filtered IISrpc-or-vat  no-response
5353/udp  open          mdns           udp-response ttl 254 DNS-based service discovery
| dns-service-discovery: 
|   9/tcp workstation
|     Address=10.10.10.117 dead:beef::250:56ff:feb9:9800
|   80/tcp http
|_    Address=10.10.10.117 dead:beef::250:56ff:feb9:9800
5632/udp  open|filtered pcanywherestat no-response
9200/udp  open|filtered wap-wsp        no-response
32771/udp open|filtered sometimes-rpc6 no-response
33281/udp open|filtered unknown        no-response
49181/udp open|filtered unknown        no-response
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=9/27%OT=%CT=%CU=7%PV=Y%DS=2%DC=T%G=N%TM=6333AF9B%P=x86_64-pc-linux-gnu)
SEQ(CI=I%II=I)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops

TRACEROUTE (using port 520/udp)
HOP RTT      ADDRESS
1   15.26 ms 10.10.14.1
2   15.26 ms 10.10.10.117

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep 27 22:21:15 2022 -- 1 IP address (1 host up) scanned in 244.32 seconds

```
