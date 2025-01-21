```bash
nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.239
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/tcp_135_rpc_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/tcp_135_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Aug  4 19:14:04 2022 as: nmap -vv --reason -Pn -T4 -sV -p 135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/tcp_135_rpc_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/xml/tcp_135_rpc_nmap.xml 10.10.10.239
Nmap scan report for 10.10.10.239
Host is up, received user-set (0.013s latency).
Scanned at 2022-08-04 19:14:05 EDT for 21s

PORT    STATE SERVICE REASON          VERSION
135/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  4 19:14:26 2022 -- 1 IP address (1 host up) scanned in 21.85 seconds

```
