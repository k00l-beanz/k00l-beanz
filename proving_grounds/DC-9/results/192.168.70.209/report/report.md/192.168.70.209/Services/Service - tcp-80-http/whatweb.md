```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.70.209:80 2>&1
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-9/results/192.168.70.209/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.70.209:80
Status    : 200 OK
Title     : Example.com - Staff Details - Welcome
IP        : 192.168.70.209
Country   : RESERVED, ZZ

Summary   : Apache[2.4.38], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.38 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : Debian Linux
	String       : Apache/2.4.38 (Debian) (from server string)

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Sat, 03 Dec 2022 03:57:45 GMT
	Server: Apache/2.4.38 (Debian)
	Vary: Accept-Encoding
	Content-Encoding: gzip
	Content-Length: 402
	Connection: close
	Content-Type: text/html; charset=UTF-8



```
