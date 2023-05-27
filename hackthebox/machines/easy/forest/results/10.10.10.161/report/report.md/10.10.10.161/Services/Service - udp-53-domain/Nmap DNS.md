```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 53 --script="banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/udp53/udp_53_dns_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/udp53/xml/udp_53_dns_nmap.xml" 10.10.10.161
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/udp53/udp_53_dns_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/udp53/udp_53_dns_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Jul 26 18:59:30 2022 as: nmap -vv --reason -Pn -T4 -sU -sV -p 53 "--script=banner,(dns* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/udp53/udp_53_dns_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/udp53/xml/udp_53_dns_nmap.xml 10.10.10.161
Nmap scan report for 10.10.10.161
Host is up, received user-set.
Scanned at 2022-07-26 18:59:30 EDT for 30s

PORT   STATE SERVICE REASON       VERSION
53/udp open  domain  udp-response (generic dns response: SERVFAIL)
|_dns-nsec3-enum: Can't determine domain for host 10.10.10.161; use dns-nsec3-enum.domains script arg.
| fingerprint-strings: 
|   NBTStat: 
|_    CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
|_dns-nsec-enum: Can't determine domain for host 10.10.10.161; use dns-nsec-enum.domains script arg.
|_dns-cache-snoop: 0 of 100 tested domains are cached.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port53-UDP:V=7.92%I=7%D=7/26%Time=62E071E7%P=x86_64-pc-linux-gnu%r(NBTS
SF:tat,32,"\x80\xf0\x80\x82\0\x01\0\0\0\0\0\0\x20CKAAAAAAAAAAAAAAAAAAAAAAA
SF:AAAAAAA\0\0!\0\x01");

Host script results:
|_dns-brute: Can't guess domain of "10.10.10.161"; use dns-brute.domain script argument.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul 26 19:00:00 2022 -- 1 IP address (1 host up) scanned in 30.22 seconds

```
