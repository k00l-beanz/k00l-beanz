# OpenAdmin

## Enumeration

Start with a basic `nmap` scan

```s
# Nmap 7.93 scan initiated Mon Apr  3 19:29:58 2023 as: nmap -p- -A -oN nmap/openadmin_all.nmap 10.10.10.171
Nmap scan report for 10.10.10.171
Host is up (0.012s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 4b98df85d17ef03dda48cdbc9200b754 (RSA)
|   256 dceb3dc944d118b122b4cfdebd6c7a54 (ECDSA)
|_  256 dcadca3c11315b6fe6a489347c9be550 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
```

### tcp/80 

I run a `whatweb` to get an idea of what I'm working with. 

```s
$ whatweb "http://10.10.10.171" -a 3
http://10.10.10.171 [200 OK] Apache[2.4.29], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], IP[10.10.10.171], Title[Apache2 Ubuntu Default Page: It works]
```

I also did a `cURL` request to verify this information.

```s
$ curl -I "http://10.10.10.171"
HTTP/1.1 200 OK
Date: Tue, 04 Apr 2023 00:32:38 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Thu, 21 Nov 2019 14:08:45 GMT
ETag: "2aa6-597dbd5dcea8b"
Accept-Ranges: bytes
Content-Length: 10918
Vary: Accept-Encoding
Content-Type: text/html
```

The landing page for `http://10.10.10.171` is the default `It Works` apache2 page.