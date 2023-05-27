```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.88:80 2>&1
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://10.10.10.88:80
Status    : 200 OK
Title     : Landing Page
IP        : 10.10.10.88
Country   : RESERVED, ZZ

Summary   : Apache[2.4.18], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.18 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Ubuntu Linux
	String       : Apache/2.4.18 (Ubuntu) (from server string)

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Thu, 29 Sep 2022 23:08:54 GMT
	Server: Apache/2.4.18 (Ubuntu)
	Last-Modified: Wed, 21 Feb 2018 20:31:20 GMT
	ETag: "2a0e-565becf5ff08d-gzip"
	Accept-Ranges: bytes
	Vary: Accept-Encoding
	Content-Encoding: gzip
	Content-Length: 2146
	Connection: close
	Content-Type: text/html



```
