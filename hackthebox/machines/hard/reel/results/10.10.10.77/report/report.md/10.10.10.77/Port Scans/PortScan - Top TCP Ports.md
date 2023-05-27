```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/xml/_quick_tcp_nmap.xml" 10.10.10.77
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_quick_tcp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_quick_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Fri Oct 21 00:06:51 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_quick_tcp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/xml/_quick_tcp_nmap.xml 10.10.10.77
Nmap scan report for 10.10.10.77
Host is up, received user-set (0.013s latency).
Scanned at 2022-10-21 00:06:51 EDT for 535s
Not shown: 997 filtered tcp ports (no-response)
PORT   STATE SERVICE REASON          VERSION
21/tcp open  ftp     syn-ack ttl 127 Microsoft ftpd
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_05-29-18  12:19AM       <DIR>          documents
| ftp-syst: 
|_  SYST: Windows_NT
22/tcp open  ssh     syn-ack ttl 127 OpenSSH 7.6 (protocol 2.0)
| ssh-hostkey: 
|   2048 82:20:c3:bd:16:cb:a2:9c:88:87:1d:6c:15:59:ed:ed (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQkehAZGj87mZluxFiVu+GPAAnC/OQ9QKUF2wlIwvefrD2L4zWyGXlAgSbUq/MqujR/efrTIjPYWK+5Mlxc7gEoZBylGAPbdxFivL8YQs3dQPt6aHNF0v+ABS01L2qZ4ewd1sTi1TlT6LtWHehX2PBJ6S3LWG09v+E/3ue97y9gaOjfA6BCMWgQ7K3yvQeHrRpBSk/vQxfCh4TINwV3EGbGTfbs8VvvR+Et7weB5EOifgXfHbyh04KemONkceFSAnjRRYOgwvtXai9imsDJ8KtS2RMR197VK4MBhsY7+h0nOvUMgm76RcRc6N8GW1mn6gWp98Ds9VeymzAmQvprs97
|   256 23:2b:b8:0a:8c:1c:f4:4d:8d:7e:5e:64:58:80:33:45 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAw2CYanDlTRpGqzVXrfGTcAYVe/vUnnkWicQPzdfix5gFsv4nOGNUM+Fko7QAW0jqCFQKc8anGAwJjFGLTB00k=
|   256 ac:8b:de:25:1d:b7:d8:38:38:9b:9c:16:bf:f6:3f:ed (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICdDfn+n5xueGtHP20/aPkI8pvCfxb2UZA3RQdqnpjBk
25/tcp open  smtp?   syn-ack ttl 127
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Kerberos, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, SSLv23SessionReq, TLSSessionReq, X11Probe: 
|     220 Mail Service ready
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, RTSPRequest: 
|     220 Mail Service ready
|     sequence of commands
|     sequence of commands
|   Hello: 
|     220 Mail Service ready
|     EHLO Invalid domain address.
|   Help: 
|     220 Mail Service ready
|     DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
|   SIPOptions: 
|     220 Mail Service ready
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|     sequence of commands
|   TerminalServerCookie: 
|     220 Mail Service ready
|_    sequence of commands
| smtp-commands: REEL, SIZE 20480000, AUTH LOGIN PLAIN, HELP
|_ 211 DATA HELO EHLO MAIL NOOP QUIT RCPT RSET SAML TURN VRFY
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port25-TCP:V=7.92%I=9%D=10/21%Time=63521AE6%P=x86_64-pc-linux-gnu%r(NUL
SF:L,18,"220\x20Mail\x20Service\x20ready\r\n")%r(Hello,3A,"220\x20Mail\x20
SF:Service\x20ready\r\n501\x20EHLO\x20Invalid\x20domain\x20address\.\r\n")
SF:%r(Help,54,"220\x20Mail\x20Service\x20ready\r\n211\x20DATA\x20HELO\x20E
SF:HLO\x20MAIL\x20NOOP\x20QUIT\x20RCPT\x20RSET\x20SAML\x20TURN\x20VRFY\r\n
SF:")%r(GenericLines,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\x20
SF:sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\
SF:r\n")%r(GetRequest,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\x2
SF:0sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands
SF:\r\n")%r(HTTPOptions,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\
SF:x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20comman
SF:ds\r\n")%r(RTSPRequest,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Ba
SF:d\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20comm
SF:ands\r\n")%r(RPCCheck,18,"220\x20Mail\x20Service\x20ready\r\n")%r(DNSVe
SF:rsionBindReqTCP,18,"220\x20Mail\x20Service\x20ready\r\n")%r(DNSStatusRe
SF:questTCP,18,"220\x20Mail\x20Service\x20ready\r\n")%r(SSLSessionReq,18,"
SF:220\x20Mail\x20Service\x20ready\r\n")%r(TerminalServerCookie,36,"220\x2
SF:0Mail\x20Service\x20ready\r\n503\x20Bad\x20sequence\x20of\x20commands\r
SF:\n")%r(TLSSessionReq,18,"220\x20Mail\x20Service\x20ready\r\n")%r(SSLv23
SF:SessionReq,18,"220\x20Mail\x20Service\x20ready\r\n")%r(Kerberos,18,"220
SF:\x20Mail\x20Service\x20ready\r\n")%r(SMBProgNeg,18,"220\x20Mail\x20Serv
SF:ice\x20ready\r\n")%r(X11Probe,18,"220\x20Mail\x20Service\x20ready\r\n")
SF:%r(FourOhFourRequest,54,"220\x20Mail\x20Service\x20ready\r\n503\x20Bad\
SF:x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20comman
SF:ds\r\n")%r(LPDString,18,"220\x20Mail\x20Service\x20ready\r\n")%r(LDAPSe
SF:archReq,18,"220\x20Mail\x20Service\x20ready\r\n")%r(LDAPBindReq,18,"220
SF:\x20Mail\x20Service\x20ready\r\n")%r(SIPOptions,162,"220\x20Mail\x20Ser
SF:vice\x20ready\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad
SF:\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20comma
SF:nds\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequen
SF:ce\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503
SF:\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x
SF:20commands\r\n503\x20Bad\x20sequence\x20of\x20commands\r\n503\x20Bad\x2
SF:0sequence\x20of\x20commands\r\n503\x20Bad\x20sequence\x20of\x20commands
SF:\r\n");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
OS fingerprint not ideal because: Missing a closed TCP port so results incomplete
Aggressive OS guesses: Microsoft Windows Server 2012 (91%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (91%), Microsoft Windows Server 2012 R2 (91%), Microsoft Windows 7 Professional (87%), Microsoft Windows 8.1 Update 1 (86%), Microsoft Windows Phone 7.5 or 8.0 (86%), Microsoft Windows 7 or Windows Server 2008 R2 (85%), Microsoft Windows Server 2008 R2 (85%), Microsoft Windows Server 2008 R2 or Windows 8.1 (85%), Microsoft Windows Server 2008 R2 SP1 or Windows 8 (85%)
No exact OS matches for host (test conditions non-ideal).
TCP/IP fingerprint:
SCAN(V=7.92%E=4%D=10/21%OT=21%CT=%CU=%PV=Y%DS=2%DC=T%G=N%TM=63521CF2%P=x86_64-pc-linux-gnu)
SEQ(SP=102%GCD=1%ISR=109%TI=I%II=I%SS=S%TS=7)
OPS(O1=M539NW8ST11%O2=M539NW8ST11%O3=M539NW8NNT11%O4=M539NW8ST11%O5=M539NW8ST11%O6=M539ST11)
WIN(W1=2000%W2=2000%W3=2000%W4=2000%W5=2000%W6=2000)
ECN(R=Y%DF=Y%TG=80%W=2000%O=M539NW8NNS%CC=Y%Q=)
T1(R=Y%DF=Y%TG=80%S=O%A=S+%F=AS%RD=0%Q=)
T2(R=N)
T3(R=N)
T4(R=N)
U1(R=N)
IE(R=Y%DFI=N%TG=80%CD=Z)

Uptime guess: 0.007 days (since Fri Oct 21 00:05:39 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   13.13 ms 10.10.14.1
2   13.52 ms 10.10.10.77

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Oct 21 00:15:46 2022 -- 1 IP address (1 host up) scanned in 535.24 seconds

```
