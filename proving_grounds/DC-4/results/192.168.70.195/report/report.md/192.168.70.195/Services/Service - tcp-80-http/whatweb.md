```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.70.195:80 2>&1
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://192.168.70.195:80
Status    : 200 OK
Title     : System Tools
IP        : 192.168.70.195
Country   : RESERVED, ZZ

Summary   : HTML5, HTTPServer[nginx/1.15.10], nginx[1.15.10], PasswordField[password]

Detected Plugins:
[ HTML5 ]
	HTML version 5, detected by the doctype declaration


[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : nginx/1.15.10 (from server string)

[ PasswordField ]
	find password fields

	String       : password (from field name)

[ nginx ]
	Nginx (Engine-X) is a free, open-source, high-performance
	HTTP server and reverse proxy, as well as an IMAP/POP3
	proxy server.

	Version      : 1.15.10
	Website     : http://nginx.net/

HTTP Headers:
	HTTP/1.1 200 OK
	Server: nginx/1.15.10
	Date: Fri, 02 Dec 2022 02:43:50 GMT
	Content-Type: text/html; charset=UTF-8
	Transfer-Encoding: chunked
	Connection: close



```
