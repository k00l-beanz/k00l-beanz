```bash
nmap -vv --reason -Pn -T4 -sV -p 88 --script="banner,krb5-enum-users" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp88/tcp_88_kerberos_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp88/xml/tcp_88_kerberos_nmap.xml" 10.10.10.161
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp88/tcp_88_kerberos_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp88/tcp_88_kerberos_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Jul 26 18:50:52 2022 as: nmap -vv --reason -Pn -T4 -sV -p 88 --script=banner,krb5-enum-users -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp88/tcp_88_kerberos_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp88/xml/tcp_88_kerberos_nmap.xml 10.10.10.161
Nmap scan report for 10.10.10.161
Host is up, received user-set (0.013s latency).
Scanned at 2022-07-26 18:50:53 EDT for 16s

PORT   STATE SERVICE      REASON          VERSION
88/tcp open  kerberos-sec syn-ack ttl 127 Microsoft Windows Kerberos (server time: 2022-07-26 22:58:22Z)
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul 26 18:51:09 2022 -- 1 IP address (1 host up) scanned in 17.29 seconds

```
