```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/xml/_full_tcp_nmap.xml" 192.168.70.195
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_full_tcp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_full_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Dec  1 21:43:34 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/_full_tcp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/xml/_full_tcp_nmap.xml 192.168.70.195
Increasing send delay for 192.168.70.195 from 0 to 5 due to 523 out of 1307 dropped probes since last increase.
Increasing send delay for 192.168.70.195 from 5 to 10 due to 11 out of 16 dropped probes since last increase.
Warning: 192.168.70.195 giving up on port because retransmission cap hit (6).
adjust_timeouts2: packet supposedly had rtt of -288092 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -288092 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -287717 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -287717 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -302400 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -302400 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -821519 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -821519 microseconds.  Ignoring time.
Nmap scan report for 192.168.70.195
Host is up, received user-set (0.020s latency).
Scanned at 2022-12-01 21:43:34 EST for 956s
Not shown: 65395 closed tcp ports (reset), 138 filtered tcp ports (no-response)
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 8d:60:57:06:6c:27:e0:2f:76:2c:e6:42:c0:01:ba:25 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCp6/VowbK8MWfMDQsxHRV2yvL8ZO+FEkyIBPnDwTVKkJiVKaJMZ5ztAwTnkc30c3tvC/yCqDAJ5IbHzgvR3kHKS37d17K+/OLxalDutFjrWjG7mBxhMW/0gnrCqJokZBDXDuvHQonajsfSN6FmWoP0PDsfL8NQXwWIoMvTRYHtiEQqczV5CYZZtMKuOyiLCiWINUqKMwY+PTb0M9RzSGYSJvN8sZZnvIw/xU7xBCmaWuq8h2dIfsxy+FhrwZMhvhJOpBYtwZB+hos3bbV5FKHhVztxEo+Y2vyKTl6MXJ4qwCChJdaBAip/aUt1zDoF3cIb+yebteyDk8KIqmp5Ju4r
|   256 e7:83:8c:d7:bb:84:f3:2e:e8:a2:5f:79:6f:8e:19:30 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIbZ4PXPXShXCcbe25IY3SYbzB4hxP4K2BliUGtuYSABZosGlLlL1Pi214yCLs3ORpGxsRIHv8R0KFQX+5SNSog=
|   256 fd:39:47:8a:5e:58:33:99:73:73:9e:22:7f:90:4f:4b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDcvQZ2DbLqSSOzIbIXhyrDJ15duVKd9TEtxfX35ubsM
80/tcp open  http    syn-ack ttl 63 nginx 1.15.10
|_http-title: System Tools
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nginx/1.15.10
Aggressive OS guesses: Linux 3.11 - 4.1 (95%), Linux 4.4 (95%), Linux 3.16 (93%), Linux 3.13 (92%), Linux 3.10 - 3.16 (92%), Linux 3.10 - 3.12 (91%), Linux 2.6.32 (91%), Linux 3.2 - 3.8 (91%), Linux 3.8 (91%), Kyocera CopyStar CS-2560 printer (91%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/1%OT=22%CT=1%CU=39018%PV=Y%DS=2%DC=T%G=Y%TM=63896A1
OS:2%P=x86_64-pc-linux-gnu)SEQ(SP=107%GCD=1%ISR=10B%TI=Z%II=I%TS=8)OPS(O1=M
OS:54EST11NW7%O2=M54EST11NW7%O3=M54ENNT11NW7%O4=M54EST11NW7%O5=M54EST11NW7%
OS:O6=M54EST11)WIN(W1=7120%W2=7120%W3=7120%W4=7120%W5=7120%W6=7120)ECN(R=Y%
OS:DF=Y%T=40%W=7210%O=M54ENNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=
OS:0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
OS:T5(R=N)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%
OS:RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)IE(R=N)

Uptime guess: 0.010 days (since Thu Dec  1 21:45:13 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=263 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)
HOP RTT      ADDRESS
1   19.68 ms 192.168.49.1
2   19.70 ms 192.168.70.195

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Dec  1 21:59:30 2022 -- 1 IP address (1 host up) scanned in 956.41 seconds

```
