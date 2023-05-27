```bash
nmap -vv --reason -Pn -T4 -sV -p 5985 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/xml/tcp_5985_http_nmap.xml" 10.10.10.239
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Aug  4 19:35:47 2022 as: nmap -vv --reason -Pn -T4 -sV -p 5985 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/xml/tcp_5985_http_nmap.xml 10.10.10.239
Nmap scan report for staging.love.htb (10.10.10.239)
Host is up, received user-set (0.027s latency).
Scanned at 2022-08-04 19:35:48 EDT for 102s

Bug in http-security-headers: no string output.
PORT     STATE SERVICE REASON          VERSION
5985/tcp open  http    syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
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
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-mobileversion-checker: No mobile version detected.
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-chrono: Request times for /; avg: 171.79ms; min: 150.53ms; max: 250.91ms
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=staging.love.htb
|   Found the following error pages: 
|   
|   Error Code: 404
|_  	http://staging.love.htb:5985/
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-title: Not Found
|_http-malware-host: Host appears to be clean
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
| http-vhosts: 
|_128 names had status 404
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-date: Thu, 04 Aug 2022 23:58:10 GMT; +22m13s from local time.
| http-headers: 
|   Content-Type: text/html; charset=us-ascii
|   Server: Microsoft-HTTPAPI/2.0
|   Date: Thu, 04 Aug 2022 23:58:10 GMT
|   Connection: close
|   Content-Length: 315
|   
|_  (Request type: GET)
|_http-feed: Couldn't find any feeds.
|_http-comments-displayer: Couldn't find any comments.
|_http-dombased-xss: Couldn't find any DOM based XSS.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  4 19:37:30 2022 -- 1 IP address (1 host up) scanned in 102.82 seconds

```
