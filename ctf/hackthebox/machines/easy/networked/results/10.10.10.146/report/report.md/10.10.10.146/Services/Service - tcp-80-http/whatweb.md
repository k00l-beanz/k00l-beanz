```bash
whatweb --color=never --no-errors -a 3 -v http://10.10.10.146:80 2>&1
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp80/tcp_80_http_whatweb.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp80/tcp_80_http_whatweb.txt):

```
WhatWeb report for http://10.10.10.146:80
Status    : 200 OK
Title     : <None>
IP        : 10.10.10.146
Country   : RESERVED, ZZ

Summary   : Apache[2.4.6], HTTPServer[CentOS][Apache/2.4.6 (CentOS) PHP/5.4.16], PHP[5.4.16], X-Powered-By[PHP/5.4.16]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.6 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	OS           : CentOS
	String       : Apache/2.4.6 (CentOS) PHP/5.4.16 (from server string)

[ PHP ]
	PHP is a widely-used general-purpose scripting language
	that is especially suited for Web development and can be
	embedded into HTML. This plugin identifies PHP errors,
	modules and versions and extracts the local file path and
	username if present.

	Version      : 5.4.16
	Version      : 5.4.16
	Google Dorks: (2)
	Website     : http://www.php.net/

[ X-Powered-By ]
	X-Powered-By HTTP header

	String       : PHP/5.4.16 (from x-powered-by string)

HTTP Headers:
	HTTP/1.1 200 OK
	Date: Wed, 28 Sep 2022 04:00:16 GMT
	Server: Apache/2.4.6 (CentOS) PHP/5.4.16
	X-Powered-By: PHP/5.4.16
	Content-Length: 229
	Connection: close
	Content-Type: text/html; charset=UTF-8



```
