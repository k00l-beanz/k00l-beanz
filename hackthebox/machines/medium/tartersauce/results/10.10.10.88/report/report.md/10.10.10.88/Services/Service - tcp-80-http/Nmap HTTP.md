```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.88
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Sep 29 19:08:12 2022 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.88
Nmap scan report for 10.10.10.88
Host is up, received user-set (0.016s latency).
Scanned at 2022-09-29 19:08:13 EDT for 17s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 63 Apache httpd 2.4.18 ((Ubuntu))
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-errors: Couldn't find any error pages.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1
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
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-mobileversion-checker: No mobile version detected.
| http-vhosts: 
| 123 names had status 200
| test2
| dev
| dns2
| mailgate
|_corp
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-enum: 
|_  /robots.txt: Robots file
|_http-chrono: Request times for /; avg: 180.20ms; min: 156.95ms; max: 228.25ms
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-comments-displayer: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.10.10.88
|     
|     Path: http://10.10.10.88:80/
|     Line number: 563
|     Comment: 
|_        <!--Carry on, nothing to see here :D-->
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-malware-host: Host appears to be clean
|_http-date: Thu, 29 Sep 2022 23:09:02 GMT; +40s from local time.
|_http-title: Landing Page
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-referer-checker: Couldn't find any cross-domain scripts.
| http-headers: 
|   Date: Thu, 29 Sep 2022 23:09:01 GMT
|   Server: Apache/2.4.18 (Ubuntu)
|   Last-Modified: Wed, 21 Feb 2018 20:31:20 GMT
|   ETag: "2a0e-565becf5ff08d"
|   Accept-Ranges: bytes
|   Content-Length: 10766
|   Vary: Accept-Encoding
|   Connection: close
|   Content-Type: text/html
|   
|_  (Request type: HEAD)
|_http-feed: Couldn't find any feeds.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
| http-robots.txt: 5 disallowed entries 
| /webservices/tar/tar/source/ 
| /webservices/monstra-3.0.4/ /webservices/easy-file-uploader/ 
|_/webservices/developmental/ /webservices/phpmyadmin/
| http-php-version: Logo query returned unknown hash f6113ca0f116286cb2492752dbcd1b2c
|_Credits query returned unknown hash f6113ca0f116286cb2492752dbcd1b2c
|_http-config-backup: ERROR: Script execution failed (use -d to debug)

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Sep 29 19:08:30 2022 -- 1 IP address (1 host up) scanned in 17.85 seconds

```
