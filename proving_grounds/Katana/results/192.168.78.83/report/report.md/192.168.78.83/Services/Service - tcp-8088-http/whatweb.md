```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.78.83:8088 2>&1
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_whatweb.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_whatweb.txt):

```
WhatWeb report for http://192.168.78.83:8088
Status    : 200 OK
Title     : Katana X
IP        : 192.168.78.83
Country   : RESERVED, ZZ

Summary   : HTTPServer[LiteSpeed], LiteSpeed

Detected Plugins:
[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : LiteSpeed (from server string)

[ LiteSpeed ]
	LiteSpeed web server, which is able to read Apache
	configuration directly and used together with web hosting
	control panels by replacing Apache


HTTP Headers:
	HTTP/1.1 200 OK
	Etag: "28f-5eb97c92-c08a6;gz"
	Last-Modified: Mon, 11 May 2020 16:25:54 GMT
	Content-Type: text/html
	Content-Length: 379
	Accept-Ranges: bytes
	Content-Encoding: gzip
	Vary: Accept-Encoding
	Date: Thu, 08 Dec 2022 01:14:33 GMT
	Server: LiteSpeed
	Connection: close



```
