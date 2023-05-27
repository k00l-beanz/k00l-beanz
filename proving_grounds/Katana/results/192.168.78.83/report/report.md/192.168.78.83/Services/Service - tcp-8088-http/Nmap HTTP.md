```bash
nmap -vv --reason -Pn -T4 -sV -p 8088 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/xml/tcp_8088_http_nmap.xml" 192.168.78.83
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nmap.txt):

```
# Nmap 7.92 scan initiated Wed Dec  7 20:14:30 2022 as: nmap -vv --reason -Pn -T4 -sV -p 8088 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/xml/tcp_8088_http_nmap.xml 192.168.78.83
Nmap scan report for 192.168.78.83
Host is up, received user-set (0.024s latency).
Scanned at 2022-12-07 20:14:31 EST for 102s

Bug in http-security-headers: no string output.
PORT     STATE SERVICE REASON         VERSION
8088/tcp open  http    syn-ack ttl 63 LiteSpeed httpd
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
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-feed: Couldn't find any feeds.
| http-enum: 
|_  /phpinfo.php: Possible information file
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-wordpress-enum: 
| Search limited to top 100 themes/plugins
|   plugins
|     wordpress-seo
|   themes
|_    twentyten
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-server-header: LiteSpeed
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-malware-host: Host appears to be clean
| http-headers: 
|   Etag: "28f-5eb97c92-c08a6;;;"
|   Last-Modified: Mon, 11 May 2020 16:25:54 GMT
|   Content-Type: text/html
|   Content-Length: 655
|   Accept-Ranges: bytes
|   Date: Thu, 08 Dec 2022 01:14:39 GMT
|   Server: LiteSpeed
|   Connection: close
|   
|_  (Request type: HEAD)
| http-php-version: Logo query returned unknown hash 6fbf73bc3d44a2fe3581fbf20c569bf6
|_Credits query returned unknown hash 6fbf73bc3d44a2fe3581fbf20c569bf6
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-litespeed-sourcecode-download: Page: /index.php was not found. Try with an existing file.
|_http-title: Katana X
| http-vhosts: 
|_128 names had status 200
|_http-date: Thu, 08 Dec 2022 01:14:41 GMT; 0s from local time.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-errors: Couldn't find any error pages.
|_http-chrono: Request times for /; avg: 150.97ms; min: 150.00ms; max: 152.95ms
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    Other: 1
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-comments-displayer: Couldn't find any comments.
|_http-mobileversion-checker: No mobile version detected.

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Dec  7 20:16:13 2022 -- 1 IP address (1 host up) scanned in 102.93 seconds

```
