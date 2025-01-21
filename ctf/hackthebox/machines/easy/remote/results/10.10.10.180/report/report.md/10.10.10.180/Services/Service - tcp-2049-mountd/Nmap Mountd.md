```bash
nmap -vv --reason -Pn -T4 -sV -p 2049 --script="banner,nfs* and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp2049/tcp_2049_mountd_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp2049/xml/tcp_2049_mountd_nmap.xml" 10.10.10.180
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp2049/tcp_2049_mountd_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp2049/tcp_2049_mountd_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Aug  2 14:48:41 2022 as: nmap -vv --reason -Pn -T4 -sV -p 2049 "--script=banner,nfs* and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp2049/tcp_2049_mountd_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/remote/results/10.10.10.180/scans/tcp2049/xml/tcp_2049_mountd_nmap.xml 10.10.10.180
Nmap scan report for 10.10.10.180
Host is up, received user-set (0.015s latency).
Scanned at 2022-08-02 14:48:42 EDT for 16s

PORT     STATE SERVICE REASON          VERSION
2049/tcp open  mountd  syn-ack ttl 127 1-3 (RPC #100005)
| nfs-showmount: 
|_  /site_backups 

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Aug  2 14:48:58 2022 -- 1 IP address (1 host up) scanned in 17.69 seconds

```
