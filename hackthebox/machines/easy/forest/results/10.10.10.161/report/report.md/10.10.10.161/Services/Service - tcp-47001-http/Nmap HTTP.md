```bash
nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 10.10.10.161
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp47001/tcp_47001_http_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp47001/tcp_47001_http_nmap.txt):

```
# Nmap 7.92 scan initiated Tue Jul 26 18:59:13 2022 as: nmap -vv --reason -Pn -T4 -sV -p 47001 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp47001/tcp_47001_http_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/forest/results/10.10.10.161/scans/tcp47001/xml/tcp_47001_http_nmap.xml 10.10.10.161
Nmap scan report for 10.10.10.161
Host is up, received user-set (0.016s latency).
Scanned at 2022-07-26 18:59:14 EDT for 85s

Bug in http-security-headers: no string output.
PORT      STATE SERVICE REASON          VERSION
47001/tcp open  http    syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-server-header: Microsoft-HTTPAPI/2.0
| http-useragent-tester: 
|   Status for browser useragent: 404
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
|_http-date: Tue, 26 Jul 2022 23:06:49 GMT; +7m22s from local time.
|_http-malware-host: Host appears to be clean
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-title: Not Found
| http-vhosts: 
|_128 names had status 404
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-comments-displayer: Couldn't find any comments.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-feed: Couldn't find any feeds.
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.10.161
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://10.10.10.161:47001/
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-chrono: Request times for /; avg: 151.92ms; min: 149.54ms; max: 155.37ms
| http-headers: 
|   Content-Type: text/html; charset=us-ascii
|   Server: Microsoft-HTTPAPI/2.0
|   Date: Tue, 26 Jul 2022 23:06:52 GMT
|   Connection: close
|   Content-Length: 315
|   
|_  (Request type: GET)
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-mobileversion-checker: No mobile version detected.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jul 26 19:00:39 2022 -- 1 IP address (1 host up) scanned in 86.11 seconds

```
