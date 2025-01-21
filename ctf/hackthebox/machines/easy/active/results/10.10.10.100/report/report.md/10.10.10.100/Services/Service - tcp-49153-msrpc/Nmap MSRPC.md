```bash
nmap -vv --reason -Pn -T4 -sV -p 49153 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp49153/tcp_49153_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp49153/xml/tcp_49153_rpc_nmap.xml" 10.10.10.100
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp49153/tcp_49153_rpc_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp49153/tcp_49153_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Mon Sep 19 18:45:10 2022 as: nmap -vv --reason -Pn -T4 -sV -p 49153 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp49153/tcp_49153_rpc_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/tcp49153/xml/tcp_49153_rpc_nmap.xml 10.10.10.100
Nmap scan report for 10.10.10.100
Host is up, received user-set (0.013s latency).
Scanned at 2022-09-19 18:45:10 EDT for 74s

PORT      STATE SERVICE REASON          VERSION
49153/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Sep 19 18:46:24 2022 -- 1 IP address (1 host up) scanned in 74.65 seconds

```
