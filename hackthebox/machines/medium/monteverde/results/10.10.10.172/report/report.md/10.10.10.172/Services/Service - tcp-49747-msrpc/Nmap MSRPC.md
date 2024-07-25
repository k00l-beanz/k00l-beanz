```bash
nmap -vv --reason -Pn -T4 -sV -p 49747 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp49747/tcp_49747_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp49747/xml/tcp_49747_rpc_nmap.xml" 10.10.10.172
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp49747/tcp_49747_rpc_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp49747/tcp_49747_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Sep 20 18:59:05 2022 as: nmap -vv --reason -Pn -T4 -sV -p 49747 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp49747/tcp_49747_rpc_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp49747/xml/tcp_49747_rpc_nmap.xml 10.10.10.172
Nmap scan report for 10.10.10.172
Host is up, received user-set (0.037s latency).
Scanned at 2022-09-20 18:59:05 EDT for 70s

PORT      STATE SERVICE REASON          VERSION
49747/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep 20 19:00:15 2022 -- 1 IP address (1 host up) scanned in 69.98 seconds

```