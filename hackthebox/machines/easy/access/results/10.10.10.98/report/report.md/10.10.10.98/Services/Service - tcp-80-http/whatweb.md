```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.98:80 2>&1
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://10.10.10.98:80
Status    : 200 OK
Title     : MegaCorp
IP        : 10.10.10.98
Country   : RESERVED, ZZ

Summary   : HTTPServer[Microsoft-IIS/7.5], Microsoft-IIS[7.5], X-Powered-By[ASP.NET]

Detected Plugins:
[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Microsoft-IIS/7.5 (from server string)

[ Microsoft-IIS ]
	Microsoft Internet Information Services (IIS) for Windows
	Server is a flexible, secure and easy-to-manage Web server
	for hosting anything on the Web. From media streaming to
	web application hosting, IIS's scalable and open
	architecture is ready to handle the most demanding tasks.

	Version      : 7.5
	Website     : http://www.iis.net/

[ X-Powered-By ]
	X-Powered-By HTTP header

	String       : ASP.NET (from x-powered-by string)

HTTP Headers:
	HTTP/1.1 200 OK
	Content-Type: text/html
	Last-Modified: Thu, 23 Aug 2018 23:33:43 GMT
	Accept-Ranges: bytes
	ETag: "44a87bb393bd41:0"
	Server: Microsoft-IIS/7.5
	X-Powered-By: ASP.NET
	Date: Wed, 16 Nov 2022 00:36:23 GMT
	Connection: close
	Content-Length: 391



```
