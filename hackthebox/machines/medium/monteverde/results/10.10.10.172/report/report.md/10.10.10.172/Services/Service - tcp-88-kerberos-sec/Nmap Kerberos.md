```bash
nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.172
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp88/tcp_88_kerberos_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp88/tcp_88_kerberos_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Sep 20 18:59:04 2022 as: nmap -vv --reason -Pn -T4 -sV -p 88 --script=banner,krb5-enum-users -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp88/tcp_88_kerberos_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp88/xml/tcp_88_kerberos_nmap.xml 10.10.10.172
Nmap scan report for 10.10.10.172
Host is up, received user-set (0.014s latency).
Scanned at 2022-09-20 18:59:05 EDT for 16s

PORT   STATE SERVICE      REASON          VERSION
88/tcp open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2022-09-20 22:59:11Z)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep 20 18:59:21 2022 -- 1 IP address (1 host up) scanned in 17.06 seconds

```
