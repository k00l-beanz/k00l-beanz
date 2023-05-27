```bash
feroxbuster -u http://192.168.78.83:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
403      GET        9l       28w      278c http://192.168.78.83/.hta
403      GET        9l       28w      278c http://192.168.78.83/.htaccess
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd
403      GET        9l       28w      278c http://192.168.78.83/.hta.txt
403      GET        9l       28w      278c http://192.168.78.83/.htaccess.txt
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd.txt
403      GET        9l       28w      278c http://192.168.78.83/.htaccess.html
403      GET        9l       28w      278c http://192.168.78.83/.hta.html
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd.html
403      GET        9l       28w      278c http://192.168.78.83/.htaccess.php
403      GET        9l       28w      278c http://192.168.78.83/.hta.php
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd.php
403      GET        9l       28w      278c http://192.168.78.83/.htaccess.asp
403      GET        9l       28w      278c http://192.168.78.83/.hta.asp
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd.asp
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd.aspx
403      GET        9l       28w      278c http://192.168.78.83/.htaccess.aspx
403      GET        9l       28w      278c http://192.168.78.83/.hta.aspx
403      GET        9l       28w      278c http://192.168.78.83/.htpasswd.jsp
403      GET        9l       28w      278c http://192.168.78.83/.htaccess.jsp
403      GET        9l       28w      278c http://192.168.78.83/.hta.jsp
200      GET       23l       73w      655c http://192.168.78.83/
403      GET        9l       28w      278c http://192.168.78.83/.html
403      GET        9l       28w      278c http://192.168.78.83/.php
301      GET        9l       28w      314c http://192.168.78.83/ebook => http://192.168.78.83/ebook/
200      GET       23l       73w      655c http://192.168.78.83/index.html
403      GET        9l       28w      278c http://192.168.78.83/server-status

```
