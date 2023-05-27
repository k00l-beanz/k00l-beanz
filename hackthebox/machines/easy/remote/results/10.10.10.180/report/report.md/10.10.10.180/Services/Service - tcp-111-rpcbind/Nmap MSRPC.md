```bash
nmap -vv --reason -Pn -T4 -sV -p 111 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp111/tcp_111_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp111/xml/tcp_111_rpc_nmap.xml" 10.10.10.180
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp111/tcp_111_rpc_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp111/tcp_111_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Aug  2 14:48:40 2022 as: nmap -vv --reason -Pn -T4 -sV -p 111 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp111/tcp_111_rpc_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp111/xml/tcp_111_rpc_nmap.xml 10.10.10.180
Nmap scan report for 10.10.10.180
Host is up, received user-set (0.052s latency).
Scanned at 2022-08-02 14:48:41 EDT for 80s

PORT    STATE SERVICE REASON          VERSION
111/tcp open  rpcbind syn-ack ttl 127 2-4 (RPC #100000)
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

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  2 14:50:01 2022 -- 1 IP address (1 host up) scanned in 80.89 seconds

```
