```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.98
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Nov 15 19:36:22 2022 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.10.98
Nmap scan report for 10.10.10.98
Host is up, received user-set (0.013s latency).
Scanned at 2022-11-15 19:36:23 EST for 48s

Bug in http-security-headers: no string output.
PORT   STATE SERVICE REASON          VERSION
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 7.5
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-comments-displayer: Couldn't find any comments.
| http-headers: 
|   Content-Length: 391
|   Content-Type: text/html
|   Last-Modified: Thu, 23 Aug 2018 23:33:43 GMT
|   Accept-Ranges: bytes
|   ETag: "44a87bb393bd41:0"
|   Server: Microsoft-IIS/7.5
|   X-Powered-By: ASP.NET
|   Date: Wed, 16 Nov 2022 00:36:30 GMT
|   Connection: close
|   
|_  (Request type: HEAD)
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-chrono: Request times for /; avg: 153.63ms; min: 151.31ms; max: 158.46ms
|_http-errors: Couldn't find any error pages.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-feed: Couldn't find any feeds.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-vhosts: 
|_128 names had status 200
|_http-exif-spider: ERROR: Script execution failed (use -d to debug)
|_http-malware-host: Host appears to be clean
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-title: MegaCorp
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
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
| http-php-version: Logo query returned unknown hash e93be337a60d7cbd8a60a1793bb91439
|_Credits query returned unknown hash e93be337a60d7cbd8a60a1793bb91439
|_http-server-header: Microsoft-IIS/7.5
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-mobileversion-checker: No mobile version detected.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; jpg: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1; jpg: 1
|_http-devframework: ASP.NET detected. Found related header.
|_http-date: Wed, 16 Nov 2022 00:36:29 GMT; -1s from local time.
|_http-dombased-xss: Couldn't find any DOM based XSS.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Nov 15 19:37:11 2022 -- 1 IP address (1 host up) scanned in 48.74 seconds

```
