```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.117
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp80/tcp_80_http_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Sep 27 22:17:37 2022 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp80/tcp_80_http_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/irked/results/10.10.10.117/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.117
Nmap scan report for 10.10.10.117
Host is up, received user-set (0.013s latency).
Scanned at 2022-09-27 22:17:44 EDT for 17s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.10 ((Debian))
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; jpg: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1; jpg: 1
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-headers: 
|   Date: Wed, 28 Sep 2022 02:17:50 GMT
|   Server: Apache/2.4.10 (Debian)
|   Last-Modified: Mon, 14 May 2018 18:00:02 GMT
|   ETag: "48-56c2e413aa86b"
|   Accept-Ranges: bytes
|   Content-Length: 72
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-mobileversion-checker: No mobile version detected.
|_http-feed: Couldn't find any feeds.
|_http-errors: Couldn't find any error pages.
|_http-chrono: Request times for /; avg: 170.30ms; min: 157.41ms; max: 180.40ms
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-exif-spider: ERROR: Script execution failed (use -d to debug)
| http-vhosts: 
|_128 names had status 200
|_http-comments-displayer: Couldn't find any comments.
|_http-date: Wed, 28 Sep 2022 02:17:50 GMT; -2s from local time.
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-php-version: Logo query returned unknown hash b746d87c37a909650ded7d08c8d87784
|_Credits query returned unknown hash b746d87c37a909650ded7d08c8d87784
|_http-title: Site doesn't have a title (text/html).
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-malware-host: Host appears to be clean
| http-enum: 
|_  /manual/: Potentially interesting folder
|_http-server-header: Apache/2.4.10 (Debian)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
| http-useragent-tester: 
|   Status for browser useragent: 200
|   Allowed User Agents: 
|     Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)
|     libwww
|     lwp-trivial
|     libcurl-agent/1.0
|     PHP/
|     Python-urllib/2.5
|     GT::WWW
|     Snoopy
|     MFC_Tear_Sample
|     HTTP::Lite
|     PHPCrawl
|     URI::Fetch
|     Zend_Http_Client
|     http client
|     PECL::HTTP
|     Wget/1.13.4 (linux-gnu)
|_    WWW-Mechanize/1.34

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Sep 27 22:18:01 2022 -- 1 IP address (1 host up) scanned in 23.84 seconds

```
