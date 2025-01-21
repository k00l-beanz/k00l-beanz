# curling

## Information Gathering

- Passowrds
    - Curling2018!

## Enumeration

Basic nmap scan

```s
$ sudo nmap -p 22,80 -A -oN nmap/curling 10.10.10.150
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-20 21:46 EDT
Nmap scan report for 10.10.10.150
Host is up (0.012s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8a:d1:69:b4:90:20:3e:a7:b6:54:01:eb:68:30:3a:ca (RSA)
|   256 9f:0b:c2:b2:0b:ad:8f:a1:4e:0b:f6:33:79:ef:fb:43 (ECDSA)
|_  256 c1:2a:35:44:30:0c:5b:56:6a:3f:a5:cc:64:66:d9:a9 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Home
|_http-generator: Joomla! - Open Source Content Management
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 5.0 (96%), Linux 4.15 - 5.8 (96%), Linux 3.1 (95%), Linux 3.2 (95%), Linux 5.3 - 5.4 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), Linux 2.6.32 (94%), Linux 5.0 - 5.5 (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   11.41 ms 10.10.14.1
2   12.16 ms 10.10.10.150
```

### 22/tcp

### 80/tcp

- Technologies
    - Apache/2.4.29

Banner grabbing
```
$ curl -I "http://10.10.10.150"                                             
HTTP/1.1 200 OK
Date: Thu, 21 Sep 2023 01:49:35 GMT
Server: Apache/2.4.29 (Ubuntu)
Set-Cookie: c0548020854924e0aecd05ed9f5b672b=472i1imbojgj2301in7q8tn1qr; path=/; HttpOnly
Expires: Wed, 17 Aug 2005 00:00:00 GMT
Last-Modified: Thu, 21 Sep 2023 01:49:35 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
Content-Type: text/html; charset=utf-8
```

There is possibly a custom implementation of a session cookie. The cookie is also HttpOnly. This means we may be able to steal other users sessions if we find an XSS.

Running gobuster scan on root directory
```

```

There is a file `/secret.txt`:
```
Q3VybGluZzIwMTgh
```

Base64 decoding this:
```s
$ echo "Q3VybGluZzIwMTgh" | base64 -d                                                         
Curling2018!
```

## Foothold

## Privilege Escalation