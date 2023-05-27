```bash
whatweb --color=never --no-errors -a 3 -v http://192.168.78.83:8715 2>&1
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_whatweb.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_whatweb.txt):

```
WhatWeb report for http://192.168.78.83:8715
Status    : 401 Unauthorized
Title     : 401 Authorization Required
IP        : 192.168.78.83
Country   : RESERVED, ZZ

Summary   : HTTPServer[nginx/1.14.2], nginx[1.14.2], WWW-Authenticate[Restricted Content][Basic]

Detected Plugins:
[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : nginx/1.14.2 (from server string)

[ WWW-Authenticate ]
	This plugin identifies the WWW-Authenticate HTTP header and
	extracts the authentication method and realm.

	Module       : Basic
	String       : Restricted Content

[ nginx ]
	Nginx (Engine-X) is a free, open-source, high-performance
	HTTP server and reverse proxy, as well as an IMAP/POP3
	proxy server.

	Version      : 1.14.2
	Website     : http://nginx.net/

HTTP Headers:
	HTTP/1.1 401 Unauthorized
	Server: nginx/1.14.2
	Date: Thu, 08 Dec 2022 01:15:20 GMT
	Content-Type: text/html
	Content-Length: 195
	Connection: close
	WWW-Authenticate: Basic realm="Restricted Content"



```
