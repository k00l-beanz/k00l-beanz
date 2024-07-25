```bash
nmap -vv --reason -Pn -T4 -sV -p 111 --script="banner,(rpcinfo or nfs*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp111/tcp_111_nfs_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp111/xml/tcp_111_nfs_nmap.xml" 10.10.10.117
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp111/tcp_111_nfs_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp111/tcp_111_nfs_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Sep 27 22:17:37 2022 as: nmap -vv --reason -Pn -T4 -sV -p 111 "--script=banner,(rpcinfo or nfs*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp111/tcp_111_nfs_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp111/xml/tcp_111_nfs_nmap.xml 10.10.10.117
Nmap scan report for 10.10.10.117
Host is up, received user-set (0.014s latency).
Scanned at 2022-09-27 22:17:44 EDT for 16s

PORT    STATE SERVICE REASON         VERSION
111/tcp open  rpcbind syn-ack ttl 63 2-4 (RPC #100000)
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

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep 27 22:18:00 2022 -- 1 IP address (1 host up) scanned in 23.18 seconds

```
