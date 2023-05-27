```bash
nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/xml/_top_100_udp_nmap.xml" 10.10.10.180
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_top_100_udp_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_top_100_udp_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Aug  2 14:45:56 2022 as: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/_top_100_udp_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/xml/_top_100_udp_nmap.xml 10.10.10.180
Warning: 10.10.10.180 giving up on port because retransmission cap hit (6).
Increasing send delay for 10.10.10.180 from 100 to 200 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.180 from 200 to 400 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.10.180 from 400 to 800 due to 11 out of 15 dropped probes since last increase.
Increasing send delay for 10.10.10.180 from 800 to 1000 due to 11 out of 21 dropped probes since last increase.
adjust_timeouts2: packet supposedly had rtt of -362725 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -362725 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -392961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -392961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -417855 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -417855 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -449075 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -449075 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -446525 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -446525 microseconds.  Ignoring time.
Nmap scan report for 10.10.10.180
Host is up, received user-set (0.12s latency).
Scanned at 2022-08-02 14:45:57 EDT for 454s
Not shown: 78 closed udp ports (port-unreach)
PORT      STATE         SERVICE         REASON               VERSION
7/udp     open|filtered echo            no-response
19/udp    open|filtered chargen         no-response
69/udp    open|filtered tftp            no-response
80/udp    open|filtered http            no-response
88/udp    open|filtered kerberos-sec    no-response
111/udp   open          rpcbind         udp-response ttl 127 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100003  2,3         2049/udp   nfs
|   100003  2,3,4       2049/tcp   nfs
|   100005  1,2,3       2049/tcp   mountd
|   100005  1,2,3       2049/udp   mountd
|   100021  1,2,3,4     2049/tcp   nlockmgr
|   100021  1,2,3,4     2049/udp   nlockmgr
|   100024  1           2049/tcp   status
|_  100024  1           2049/udp   status
120/udp   open|filtered cfdptkt         no-response
123/udp   open|filtered ntp             no-response
137/udp   open|filtered netbios-ns      no-response
138/udp   open|filtered netbios-dgm     no-response
500/udp   open|filtered isakmp          no-response
514/udp   open|filtered syslog          no-response
1433/udp  open|filtered ms-sql-s        no-response
1813/udp  open|filtered radacct         no-response
2049/udp  open          mountd          udp-response ttl 127 1-3 (RPC #100005)
3283/udp  open|filtered netassistant    no-response
4500/udp  open|filtered nat-t-ike       no-response
5353/udp  open|filtered zeroconf        no-response
20031/udp open|filtered bakbonenetvault no-response
32768/udp open|filtered omad            no-response
32771/udp open|filtered sometimes-rpc6  no-response
49190/udp open|filtered unknown         no-response
Too many fingerprints match this host to give specific OS details
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=8/2%OT=%CT=%CU=9%PV=Y%DS=4%DC=T%G=N%TM=62E972AB%P=x86_64-pc-linux-gnu)
T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
T6(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)
T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)
IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 4 hops

TRACEROUTE (using port 593/udp)
HOP RTT       ADDRESS
1   13.41 ms  10.10.14.1
2   ... 3
4   650.53 ms 10.10.10.180

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  2 14:53:31 2022 -- 1 IP address (1 host up) scanned in 455.03 seconds

```
