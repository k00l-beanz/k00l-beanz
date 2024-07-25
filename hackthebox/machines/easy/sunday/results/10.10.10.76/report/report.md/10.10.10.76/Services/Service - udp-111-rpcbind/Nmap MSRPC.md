```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 111 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/xml/udp_111_rpc_nmap.xml" 10.10.10.76
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_rpc_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_rpc_nmap.txt):

```
# Nmap 7.92 scan initiated Mon Oct  3 22:27:00 2022 as: nmap -vv --reason -Pn -T4 -sU -sV -p 111 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_rpc_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/xml/udp_111_rpc_nmap.xml 10.10.10.76
Nmap scan report for 10.10.10.76
Host is up, received user-set (0.013s latency).
Scanned at 2022-10-03 22:27:00 EDT for 0s

PORT    STATE SERVICE REASON               VERSION
111/udp open  rpcbind udp-response ttl 254 2-4 (RPC #100000)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Oct  3 22:27:00 2022 -- 1 IP address (1 host up) scanned in 0.59 seconds

```
