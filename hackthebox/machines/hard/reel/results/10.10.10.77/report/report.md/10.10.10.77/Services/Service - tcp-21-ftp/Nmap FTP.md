```bash
nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.10.77
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_nmap.txt):

```
# Nmap 7.92 scan initiated Fri Oct 21 00:15:46 2022 as: nmap -vv --reason -Pn -T4 -sV -p 21 "--script=banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/xml/tcp_21_ftp_nmap.xml 10.10.10.77
Nmap scan report for 10.10.10.77
Host is up, received user-set (0.011s latency).
Scanned at 2022-10-21 00:15:47 EDT for 0s

PORT   STATE SERVICE REASON          VERSION
21/tcp open  ftp     syn-ack ttl 127 Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_05-29-18  12:19AM       <DIR>          documents
|_banner: 220 Microsoft FTP Service
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Oct 21 00:15:47 2022 -- 1 IP address (1 host up) scanned in 0.76 seconds

```
