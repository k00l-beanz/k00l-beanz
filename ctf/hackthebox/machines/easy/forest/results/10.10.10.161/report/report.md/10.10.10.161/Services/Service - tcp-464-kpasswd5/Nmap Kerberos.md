```bash
nmap -vv --reason -Pn -T4 -sV -p 464 --script="banner,krb5-enum-users" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp464/tcp_464_kerberos_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp464/xml/tcp_464_kerberos_nmap.xml" 10.10.10.161
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp464/tcp_464_kerberos_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp464/tcp_464_kerberos_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Jul 26 18:50:53 2022 as: nmap -vv --reason -Pn -T4 -sV -p 464 --script=banner,krb5-enum-users -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp464/tcp_464_kerberos_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp464/xml/tcp_464_kerberos_nmap.xml 10.10.10.161
Nmap scan report for 10.10.10.161
Host is up, received user-set (0.013s latency).
Scanned at 2022-07-26 18:50:54 EDT for 17s

PORT    STATE SERVICE   REASON          VERSION
464/tcp open  kpasswd5? syn-ack ttl 127

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul 26 18:51:11 2022 -- 1 IP address (1 host up) scanned in 18.41 seconds

```
