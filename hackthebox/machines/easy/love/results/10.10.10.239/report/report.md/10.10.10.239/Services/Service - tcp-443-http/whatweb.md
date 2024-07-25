```bash
whatweb --color=never --no-errors -a 3 -v https://10.10.10.239:443 2>&1
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_whatweb.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_whatweb.txt):

```
WhatWeb report for https://10.10.10.239:443
Status    : 403 Forbidden
Title     : 403 Forbidden
IP        : 10.10.10.239
Country   : RESERVED, ZZ

Summary   : Apache[2.4.46], HTTPServer[Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27], OpenSSL[1.1.1j], PHP[7.3.27]

Detected Plugins:
[ Apache ]
	The Apache HTTP Server Project is an effort to develop and
	maintain an open-source HTTP server for modern operating
	systems including UNIX and Windows NT. The goal of this
	project is to provide a secure, efficient and extensible
	server that provides HTTP services in sync with the current
	HTTP standards.

	Version      : 2.4.46 (from HTTP Server Header)
	Google Dorks: (3)
	Website     : http://httpd.apache.org/

[ HTTPServer ]
	HTTP server header string. This plugin also attempts to
	identify the operating system from the server header.

	String       : Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27 (from server string)

[ OpenSSL ]
	The OpenSSL Project is a collaborative effort to develop a
	robust, commercial-grade, full-featured, and Open Source
	toolkit implementing the Secure Sockets Layer (SSL v2/v3)
	and Transport Layer Security (TLS v1) protocols as well as
	a full-strength general purpose cryptography library.

	Version      : 1.1.1j
	Website     : http://www.openssl.org/

[ PHP ]
	PHP is a widely-used general-purpose scripting language
	that is especially suited for Web development and can be
	embedded into HTML. This plugin identifies PHP errors,
	modules and versions and extracts the local file path and
	username if present.

	Version      : 7.3.27
	Google Dorks: (2)
	Website     : http://www.php.net/

HTTP Headers:
	HTTP/1.1 403 Forbidden
	Date: Thu, 04 Aug 2022 23:36:20 GMT
	Server: Apache/2.4.46 (Win64) OpenSSL/1.1.1j PHP/7.3.27
	Content-Length: 303
	Connection: close
	Content-Type: text/html; charset=iso-8859-1



```
