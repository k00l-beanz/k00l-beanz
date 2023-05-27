```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/xml/_top_100_udp_nmap.xml" 10.10.10.111
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_top_100_udp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Wed Nov 16 16:42:16 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_top_100_udp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/xml/_top_100_udp_nmap.xml 10.10.10.111
Increasing send delay for 10.10.10.111 from 50 to 100 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.111 from 100 to 200 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.10.111 from 200 to 400 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.10.111 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
Nmap scan report for 10.10.10.111
Host is up, received user-set (0.013s latency).
Scanned at 2022-11-16 16:42:16 EST for 292s

PORT      STATE         SERVICE         REASON              VERSION
7/udp     open|filtered echo            no-response
9/udp     open|filtered discard         no-response
17/udp    closed        qotd            port-unreach ttl 63
19/udp    closed        chargen         port-unreach ttl 63
49/udp    open|filtered tacacs          no-response
53/udp    closed        domain          port-unreach ttl 63
67/udp    closed        dhcps           port-unreach ttl 63
68/udp    closed        dhcpc           port-unreach ttl 63
69/udp    open|filtered tftp            no-response
80/udp    open|filtered http            no-response
88/udp    closed        kerberos-sec    port-unreach ttl 63
111/udp   open|filtered rpcbind         no-response
120/udp   closed        cfdptkt         port-unreach ttl 63
123/udp   open|filtered ntp             no-response
135/udp   closed        msrpc           port-unreach ttl 63
136/udp   open|filtered profile         no-response
137/udp   open          netbios-ns      udp-response ttl 63 Samba nmbd netbios-ns (workgroup: WORKGROUP)
| nbns-interfaces: 
|   hostname: FROLIC
|   interfaces: 
|_    10.10.10.111
138/udp   open|filtered netbios-dgm     no-response
139/udp   open|filtered netbios-ssn     no-response
158/udp   closed        pcmail-srv      port-unreach ttl 63
161/udp   open|filtered snmp            no-response
162/udp   closed        snmptrap        port-unreach ttl 63
177/udp   open|filtered xdmcp           no-response
427/udp   open|filtered svrloc          no-response
443/udp   open|filtered https           no-response
445/udp   closed        microsoft-ds    port-unreach ttl 63
497/udp   closed        retrospect      port-unreach ttl 63
500/udp   closed        isakmp          port-unreach ttl 63
514/udp   closed        syslog          port-unreach ttl 63
515/udp   closed        printer         port-unreach ttl 63
518/udp   closed        ntalk           port-unreach ttl 63
520/udp   closed        route           port-unreach ttl 63
593/udp   closed        http-rpc-epmap  port-unreach ttl 63
623/udp   closed        asf-rmcp        port-unreach ttl 63
626/udp   open|filtered serialnumberd   no-response
631/udp   closed        ipp             port-unreach ttl 63
996/udp   closed        vsinet          port-unreach ttl 63
997/udp   closed        maitrd          port-unreach ttl 63
998/udp   open|filtered puparp          no-response
999/udp   closed        applix          port-unreach ttl 63
1022/udp  closed        exp2            port-unreach ttl 63
1023/udp  closed        unknown         port-unreach ttl 63
1025/udp  closed        blackjack       port-unreach ttl 63
1026/udp  closed        win-rpc         port-unreach ttl 63
1027/udp  closed        unknown         port-unreach ttl 63
1028/udp  closed        ms-lsa          port-unreach ttl 63
1029/udp  open|filtered solid-mux       no-response
1030/udp  closed        iad1            port-unreach ttl 63
1433/udp  closed        ms-sql-s        port-unreach ttl 63
1434/udp  closed        ms-sql-m        port-unreach ttl 63
1645/udp  closed        radius          port-unreach ttl 63
1646/udp  open|filtered radacct         no-response
1701/udp  open|filtered L2TP            no-response
1718/udp  closed        h225gatedisc    port-unreach ttl 63
1719/udp  closed        h323gatestat    port-unreach ttl 63
1812/udp  closed        radius          port-unreach ttl 63
1813/udp  open|filtered radacct         no-response
1900/udp  open|filtered upnp            no-response
2000/udp  closed        cisco-sccp      port-unreach ttl 63
2048/udp  open|filtered dls-monitor     no-response
2049/udp  closed        nfs             port-unreach ttl 63
2222/udp  open|filtered msantipiracy    no-response
2223/udp  closed        rockwell-csp2   port-unreach ttl 63
3283/udp  closed        netassistant    port-unreach ttl 63
3456/udp  closed        IISrpc-or-vat   port-unreach ttl 63
3703/udp  open|filtered adobeserver-3   no-response
4444/udp  closed        krb524          port-unreach ttl 63
4500/udp  closed        nat-t-ike       port-unreach ttl 63
5000/udp  closed        upnp            port-unreach ttl 63
5060/udp  closed        sip             port-unreach ttl 63
5353/udp  closed        zeroconf        port-unreach ttl 63
5632/udp  open|filtered pcanywherestat  no-response
9200/udp  closed        wap-wsp         port-unreach ttl 63
10000/udp open|filtered ndmp            no-response
17185/udp open|filtered wdbrpc          no-response
20031/udp closed        bakbonenetvault port-unreach ttl 63
30718/udp open|filtered unknown         no-response
31337/udp closed        BackOrifice     port-unreach ttl 63
32768/udp open|filtered omad            no-response
32769/udp closed        filenet-rpc     port-unreach ttl 63
32771/udp closed        sometimes-rpc6  port-unreach ttl 63
32815/udp open|filtered unknown         no-response
33281/udp open|filtered unknown         no-response
49152/udp closed        unknown         port-unreach ttl 63
49153/udp closed        unknown         port-unreach ttl 63
49154/udp open|filtered unknown         no-response
49156/udp open|filtered unknown         no-response
49181/udp open|filtered unknown         no-response
49182/udp closed        unknown         port-unreach ttl 63
49185/udp closed        unknown         port-unreach ttl 63
49186/udp open|filtered unknown         no-response
49188/udp closed        unknown         port-unreach ttl 63
49190/udp closed        unknown         port-unreach ttl 63
49191/udp closed        unknown         port-unreach ttl 63
49192/udp closed        unknown         port-unreach ttl 63
49193/udp closed        unknown         port-unreach ttl 63
49194/udp closed        unknown         port-unreach ttl 63
49200/udp open|filtered unknown         no-response
49201/udp closed        unknown         port-unreach ttl 63
65024/udp open|filtered unknown         no-response
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=11/16%OT=%CT=%CU=17%PV=Y%DS=2%DC=T%G=N%TM=63755A5C%P=x86_64-pc-linux-gnu)
SEQ(CI=I%II=I)
T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: Host: FROLIC

Host script results:
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

TRACEROUTE (using port 162/udp)
HOP RTT      ADDRESS
1   13.02 ms 10.10.14.1
2   13.86 ms 10.10.10.111

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Nov 16 16:47:08 2022 -- 1 IP address (1 host up) scanned in 292.11 seconds

```
