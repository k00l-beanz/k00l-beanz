```bash
nmap -vv --reason -Pn -T4 -sV -p 3306 --script="banner,(mysql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/tcp_3306_mysql_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/xml/tcp_3306_mysql_nmap.xml" 10.10.10.239
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/tcp_3306_mysql_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/tcp_3306_mysql_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Aug  4 19:14:04 2022 as: nmap -vv --reason -Pn -T4 -sV -p 3306 "--script=banner,(mysql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/tcp_3306_mysql_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/xml/tcp_3306_mysql_nmap.xml 10.10.10.239
Nmap scan report for 10.10.10.239
Host is up, received user-set (0.015s latency).
Scanned at 2022-08-04 19:14:05 EDT for 2s

PORT     STATE SERVICE REASON          VERSION
3306/tcp open  mysql?  syn-ack ttl 127
| fingerprint-strings: 
|   NULL, SMBProgNeg, giop, oracle-tns: 
|_    Host '10.10.14.10' is not allowed to connect to this MariaDB server
| banner: F\x00\x00\x01\xFFj\x04Host '10.10.14.10' is not allowed to conn
|_ect to this MariaDB server
| mysql-info: 
|_  MySQL Error: Host '10.10.14.10' is not allowed to connect to this MariaDB server
|_mysql-empty-password: Host '10.10.14.10' is not allowed to connect to this MariaDB server
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3306-TCP:V=7.92%I=7%D=8/4%Time=62EC52BD%P=x86_64-pc-linux-gnu%r(NUL
SF:L,4A,"F\0\0\x01\xffj\x04Host\x20'10\.10\.14\.10'\x20is\x20not\x20allowe
SF:d\x20to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(SMBProgNeg,4A
SF:,"F\0\0\x01\xffj\x04Host\x20'10\.10\.14\.10'\x20is\x20not\x20allowed\x2
SF:0to\x20connect\x20to\x20this\x20MariaDB\x20server")%r(oracle-tns,4A,"F\
SF:0\0\x01\xffj\x04Host\x20'10\.10\.14\.10'\x20is\x20not\x20allowed\x20to\
SF:x20connect\x20to\x20this\x20MariaDB\x20server")%r(giop,4A,"F\0\0\x01\xf
SF:fj\x04Host\x20'10\.10\.14\.10'\x20is\x20not\x20allowed\x20to\x20connect
SF:\x20to\x20this\x20MariaDB\x20server");

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  4 19:14:07 2022 -- 1 IP address (1 host up) scanned in 2.66 seconds

```
