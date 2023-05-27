```bash
nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 10.10.10.180
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp49666/tcp_49666_rpc_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp49666/tcp_49666_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Aug  2 14:49:23 2022 as: nmap -vv --reason -Pn -T4 -sV -p 49666 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp49666/tcp_49666_rpc_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml 10.10.10.180
Nmap scan report for 10.10.10.180
Host is up, received user-set (0.17s latency).
Scanned at 2022-08-02 14:49:24 EDT for 70s

PORT      STATE SERVICE REASON          VERSION
49666/tcp open  msrpc   syn-ack ttl 127 Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  2 14:50:34 2022 -- 1 IP address (1 host up) scanned in 71.10 seconds

```
