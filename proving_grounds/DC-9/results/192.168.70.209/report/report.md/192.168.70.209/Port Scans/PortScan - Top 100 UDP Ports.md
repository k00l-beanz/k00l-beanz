```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/xml/_top_100_udp_nmap.xml" 192.168.70.209
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/_top_100_udp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Fri Dec  2 22:57:30 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/_top_100_udp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/xml/_top_100_udp_nmap.xml 192.168.70.209
Increasing send delay for 192.168.70.209 from 50 to 100 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 192.168.70.209 from 100 to 200 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.70.209 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 192.168.70.209 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 192.168.70.209
Host is up, received user-set (0.064s latency).
Scanned at 2022-12-02 22:57:31 EST for 306s

PORT      STATE         SERVICE         REASON              VERSION
7/udp     open|filtered echo            no-response
9/udp     closed        discard         port-unreach ttl 63
17/udp    closed        qotd            port-unreach ttl 63
19/udp    closed        chargen         port-unreach ttl 63
49/udp    closed        tacacs          port-unreach ttl 63
53/udp    closed        domain          port-unreach ttl 63
67/udp    open|filtered dhcps           no-response
68/udp    open|filtered dhcpc           no-response
69/udp    open|filtered tftp            no-response
80/udp    closed        http            port-unreach ttl 63
88/udp    closed        kerberos-sec    port-unreach ttl 63
111/udp   open|filtered rpcbind         no-response
120/udp   open|filtered cfdptkt         no-response
123/udp   closed        ntp             port-unreach ttl 63
135/udp   open|filtered msrpc           no-response
136/udp   closed        profile         port-unreach ttl 63
137/udp   closed        netbios-ns      port-unreach ttl 63
138/udp   closed        netbios-dgm     port-unreach ttl 63
139/udp   closed        netbios-ssn     port-unreach ttl 63
158/udp   closed        pcmail-srv      port-unreach ttl 63
161/udp   closed        snmp            port-unreach ttl 63
162/udp   open|filtered snmptrap        no-response
177/udp   closed        xdmcp           port-unreach ttl 63
427/udp   open|filtered svrloc          no-response
443/udp   closed        https           port-unreach ttl 63
445/udp   closed        microsoft-ds    port-unreach ttl 63
497/udp   open|filtered retrospect      no-response
500/udp   closed        isakmp          port-unreach ttl 63
514/udp   closed        syslog          port-unreach ttl 63
515/udp   closed        printer         port-unreach ttl 63
518/udp   open|filtered ntalk           no-response
520/udp   closed        route           port-unreach ttl 63
593/udp   closed        http-rpc-epmap  port-unreach ttl 63
623/udp   open|filtered asf-rmcp        no-response
626/udp   open|filtered serialnumberd   no-response
631/udp   closed        ipp             port-unreach ttl 63
996/udp   open|filtered vsinet          no-response
997/udp   open|filtered maitrd          no-response
998/udp   open|filtered puparp          no-response
999/udp   closed        applix          port-unreach ttl 63
1022/udp  open|filtered exp2            no-response
1023/udp  open|filtered unknown         no-response
1025/udp  open|filtered blackjack       no-response
1026/udp  closed        win-rpc         port-unreach ttl 63
1027/udp  open|filtered unknown         no-response
1028/udp  open|filtered ms-lsa          no-response
1029/udp  open|filtered solid-mux       no-response
1030/udp  closed        iad1            port-unreach ttl 63
1433/udp  closed        ms-sql-s        port-unreach ttl 63
1434/udp  open|filtered ms-sql-m        no-response
1645/udp  closed        radius          port-unreach ttl 63
1646/udp  closed        radacct         port-unreach ttl 63
1701/udp  closed        L2TP            port-unreach ttl 63
1718/udp  open|filtered h225gatedisc    no-response
1719/udp  closed        h323gatestat    port-unreach ttl 63
1812/udp  closed        radius          port-unreach ttl 63
1813/udp  closed        radacct         port-unreach ttl 63
1900/udp  closed        upnp            port-unreach ttl 63
2000/udp  closed        cisco-sccp      port-unreach ttl 63
2048/udp  closed        dls-monitor     port-unreach ttl 63
2049/udp  open|filtered nfs             no-response
2222/udp  closed        msantipiracy    port-unreach ttl 63
2223/udp  closed        rockwell-csp2   port-unreach ttl 63
3283/udp  open|filtered netassistant    no-response
3456/udp  open|filtered IISrpc-or-vat   no-response
3703/udp  open|filtered adobeserver-3   no-response
4444/udp  open|filtered krb524          no-response
4500/udp  closed        nat-t-ike       port-unreach ttl 63
5000/udp  open|filtered upnp            no-response
5060/udp  closed        sip             port-unreach ttl 63
5353/udp  open|filtered zeroconf        no-response
5632/udp  closed        pcanywherestat  port-unreach ttl 63
9200/udp  closed        wap-wsp         port-unreach ttl 63
10000/udp open|filtered ndmp            no-response
17185/udp closed        wdbrpc          port-unreach ttl 63
20031/udp closed        bakbonenetvault port-unreach ttl 63
30718/udp closed        unknown         port-unreach ttl 63
31337/udp closed        BackOrifice     port-unreach ttl 63
32768/udp closed        omad            port-unreach ttl 63
32769/udp closed        filenet-rpc     port-unreach ttl 63
32771/udp open|filtered sometimes-rpc6  no-response
32815/udp open|filtered unknown         no-response
33281/udp closed        unknown         port-unreach ttl 63
49152/udp closed        unknown         port-unreach ttl 63
49153/udp closed        unknown         port-unreach ttl 63
49154/udp closed        unknown         port-unreach ttl 63
49156/udp closed        unknown         port-unreach ttl 63
49181/udp closed        unknown         port-unreach ttl 63
49182/udp closed        unknown         port-unreach ttl 63
49185/udp open|filtered unknown         no-response
49186/udp open|filtered unknown         no-response
49188/udp closed        unknown         port-unreach ttl 63
49190/udp open|filtered unknown         no-response
49191/udp closed        unknown         port-unreach ttl 63
49192/udp closed        unknown         port-unreach ttl 63
49193/udp open|filtered unknown         no-response
49194/udp open|filtered unknown         no-response
49200/udp open|filtered unknown         no-response
49201/udp closed        unknown         port-unreach ttl 63
65024/udp closed        unknown         port-unreach ttl 63
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=12/2%OT=%CT=%CU=9%PV=Y%DS=2%DC=T%G=N%TM=638ACA5D%P=x86_64-pc-linux-gnu)
SEQ(II=I)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops

TRACEROUTE (using port 1813/udp)
HOP RTT      ADDRESS
1   19.36 ms 192.168.49.1
2   19.83 ms 192.168.70.209

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Dec  2 23:02:37 2022 -- 1 IP address (1 host up) scanned in 307.05 seconds

```
