```bash
nmap -vv --reason -Pn -T4 -sV -p 5000 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/xml/tcp_5000_http_nmap.xml" 10.10.10.239
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Aug  4 19:14:04 2022 as: nmap -vv --reason -Pn -T4 -sV -p 5000 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/xml/tcp_5000_http_nmap.xml 10.10.10.239
Nmap scan report for 10.10.10.239
Host is up, received user-set (0.013s latency).
Scanned at 2022-08-04 19:14:05 EDT for 25s

Bug in http-security-headers: no string output.
PORT     STATE SERVICE REASON          VERSION
5000/tcp open  http    syn-ack ttl 127 Apache httpd 2.4.46 (OpenSSL/1.1.1j PHP/7.3.27)
| http-grep: 
|   (1) http://10.10.10.239:5000/: 
|     (1) ip: 
|_      + 10.10.10.239
|_http-comments-displayer: Couldn't find any comments.
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-useragent-tester: 
|   Status for browser useragent: 403
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
| http-vhosts: 
|_128 names had status 403
|_http-server-header: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.
|_http-title: 403 Forbidden
|_http-date: Thu, 04 Aug 2022 23:36:35 GMT; +22m13s from local time.
|_http-mobileversion-checker: No mobile version detected.
| http-sitemap-generator: 
|   Directory structure:
|   Longest directory structure:
|     Depth: 0
|     Dir: /
|   Total files found (by extension):
|_    
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-headers: 
|   Date: Thu, 04 Aug 2022 23:36:38 GMT
|   Server: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
|   Content-Length: 304
|   Connection: close
|   Content-Type: text/html; charset=iso-8859-1
|   
|_  (Request type: GET)
|_http-chrono: Request times for /; avg: 154.50ms; min: 148.75ms; max: 164.85ms
|_http-drupal-enum: Nothing found amongst the top 100 resources,use --script-args number=<number|all> for deeper analysis)
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-referer-checker: Couldn't find any cross-domain scripts.
|_http-wordpress-enum: Nothing found amongst the top 100 resources,use --script-args search-limit=<number|all> for deeper analysis)
| http-enum: 
|_  /icons/: Potentially interesting folder w/ directory listing
| http-errors: 
| Spidering limited to: maxpagecount=40; withinhost=10.10.10.239
|   Found the following error pages: 
|   
|   Error Code: 403
|_  	http://10.10.10.239:5000/
|_http-fetch: Please enter the complete path of the directory to save data in.
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
|_http-feed: Couldn't find any feeds.
| http-trace: TRACE is enabled
| Headers:
| Date: Thu, 04 Aug 2022 23:36:30 GMT
| Server: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
| Connection: close
| Transfer-Encoding: chunked
|_Content-Type: message/http
|_http-malware-host: Host appears to be clean
|_http-litespeed-sourcecode-download: Request with null byte did not work. This web server might not be vulnerable
|_http-config-backup: ERROR: Script execution failed (use -d to debug)
Service Info: Host: www.love.htb

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Aug  4 19:14:30 2022 -- 1 IP address (1 host up) scanned in 25.44 seconds

```
