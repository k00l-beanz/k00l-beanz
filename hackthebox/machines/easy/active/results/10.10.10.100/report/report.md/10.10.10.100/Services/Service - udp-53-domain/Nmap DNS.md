```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/udp53/udp_53_dns_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/udp53/xml/udp_53_dns_nmap.xml" 10.10.10.100
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/udp53/udp_53_dns_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/udp53/udp_53_dns_nmap.txt):

```
# Nmap 7.92 scan initiated Mon Sep 19 18:50:17 2022 as: nmap -vv --reason -Pn -T4 -sU -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/udp53/udp_53_dns_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/active/results/10.10.10.100/scans/udp53/xml/udp_53_dns_nmap.xml 10.10.10.100
Nmap scan report for 10.10.10.100
Host is up, received user-set (0.015s latency).
Scanned at 2022-09-19 18:50:18 EDT for 9s

PORT   STATE SERVICE REASON               VERSION
53/udp open  domain  udp-response ttl 127 Microsoft DNS 6.1.7601 (1DB15D39) (Windows Server 2008 R2 SP1)
|_dns-cache-snoop: 0 of 100 tested domains are cached.
|_dns-nsec3-enum: Can't determine domain for host 10.10.10.100; use dns-nsec3-enum.domains script arg.
|_dns-nsec-enum: Can't determine domain for host 10.10.10.100; use dns-nsec-enum.domains script arg.
| dns-nsid: 
|_  bind.version: Microsoft DNS 6.1.7601 (1DB15D39)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows_server_2008:r2:sp1

Host script results:
|_dns-brute: Can't guess domain of "10.10.10.100"; use dns-brute.domain script argument.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Sep 19 18:50:27 2022 -- 1 IP address (1 host up) scanned in 9.33 seconds

```
