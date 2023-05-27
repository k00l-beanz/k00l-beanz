```bash
feroxbuster -u http://10.10.10.88:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
301      GET        9l       28w      330c http://10.10.10.88/webservices/monstra-3.0.4 => http://10.10.10.88/webservices/monstra-3.0.4/
200      GET      563l      128w    10766c http://10.10.10.88/
403      GET       11l       32w      291c http://10.10.10.88/.html
403      GET       11l       32w      290c http://10.10.10.88/.php
403      GET       11l       32w      290c http://10.10.10.88/.hta
403      GET       11l       32w      295c http://10.10.10.88/.htpasswd
403      GET       11l       32w      295c http://10.10.10.88/.htaccess
403      GET       11l       32w      294c http://10.10.10.88/.hta.txt
403      GET       11l       32w      299c http://10.10.10.88/.htpasswd.txt
403      GET       11l       32w      299c http://10.10.10.88/.htaccess.txt
403      GET       11l       32w      295c http://10.10.10.88/.hta.html
403      GET       11l       32w      300c http://10.10.10.88/.htaccess.html
403      GET       11l       32w      300c http://10.10.10.88/.htpasswd.html
403      GET       11l       32w      294c http://10.10.10.88/.hta.php
403      GET       11l       32w      299c http://10.10.10.88/.htpasswd.php
403      GET       11l       32w      299c http://10.10.10.88/.htaccess.php
403      GET       11l       32w      299c http://10.10.10.88/.htaccess.asp
403      GET       11l       32w      299c http://10.10.10.88/.htpasswd.asp
403      GET       11l       32w      294c http://10.10.10.88/.hta.asp
403      GET       11l       32w      295c http://10.10.10.88/.hta.aspx
403      GET       11l       32w      300c http://10.10.10.88/.htpasswd.aspx
403      GET       11l       32w      300c http://10.10.10.88/.htaccess.aspx
403      GET       11l       32w      299c http://10.10.10.88/.htaccess.jsp
403      GET       11l       32w      299c http://10.10.10.88/.htpasswd.jsp
403      GET       11l       32w      294c http://10.10.10.88/.hta.jsp
200      GET      563l      128w    10766c http://10.10.10.88/index.html
200      GET        7l       12w      208c http://10.10.10.88/robots.txt
403      GET       11l       32w      299c http://10.10.10.88/server-status
301      GET        9l       28w      316c http://10.10.10.88/webservices => http://10.10.10.88/webservices/

```
