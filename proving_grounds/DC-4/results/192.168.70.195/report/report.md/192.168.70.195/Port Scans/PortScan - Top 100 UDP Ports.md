```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/xml/_top_100_udp_nmap.xml" 192.168.70.195
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_top_100_udp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Dec  1 21:43:34 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_top_100_udp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/xml/_top_100_udp_nmap.xml 192.168.70.195
Warning: 192.168.70.195 giving up on port because retransmission cap hit (6).
Increasing send delay for 192.168.70.195 from 100 to 200 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.70.195 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.70.195 from 400 to 800 due to 11 out of 14 dropped probes since last increase.
Nmap scan report for 192.168.70.195
Host is up, received user-set (0.026s latency).
Scanned at 2022-12-01 21:43:34 EST for 228s
Not shown: 79 closed udp ports (port-unreach)
PORT      STATE         SERVICE       REASON      VERSION
17/udp    open|filtered qotd          no-response
53/udp    open|filtered domain        no-response
138/udp   open|filtered netbios-dgm   no-response
427/udp   open|filtered svrloc        no-response
518/udp   open|filtered ntalk         no-response
623/udp   open|filtered asf-rmcp      no-response
999/udp   open|filtered applix        no-response
1029/udp  open|filtered solid-mux     no-response
1030/udp  open|filtered iad1          no-response
1434/udp  open|filtered ms-sql-m      no-response
1645/udp  open|filtered radius        no-response
1701/udp  open|filtered L2TP          no-response
3283/udp  open|filtered netassistant  no-response
3703/udp  open|filtered adobeserver-3 no-response
4444/udp  open|filtered krb524        no-response
5000/udp  open|filtered upnp          no-response
5060/udp  open|filtered sip           no-response
5353/udp  open|filtered zeroconf      no-response
30718/udp open|filtered unknown       no-response
33281/udp open|filtered unknown       no-response
49152/udp open|filtered unknown       no-response
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=12/1%OT=%CT=%CU=7%PV=Y%DS=2%DC=T%G=N%TM=6389673A%P=x86_64-pc-linux-gnu)
SEQ(II=I)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops

TRACEROUTE (using port 10000/udp)
HOP RTT      ADDRESS
1   23.93 ms 192.168.49.1
2   22.83 ms 192.168.70.195

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Dec  1 21:47:22 2022 -- 1 IP address (1 host up) scanned in 228.41 seconds

```
