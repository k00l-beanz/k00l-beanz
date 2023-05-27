```bash
feroxbuster -u http://10.10.10.146:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
200      GET        8l       40w      229c http://10.10.10.146/
403      GET        8l       22w      207c http://10.10.10.146/.html
403      GET        8l       22w      206c http://10.10.10.146/.hta
403      GET        8l       22w      210c http://10.10.10.146/.hta.txt
403      GET        8l       22w      211c http://10.10.10.146/.htpasswd
403      GET        8l       22w      211c http://10.10.10.146/.hta.html
403      GET        8l       22w      211c http://10.10.10.146/.htaccess
403      GET        8l       22w      215c http://10.10.10.146/.htpasswd.txt
403      GET        8l       22w      210c http://10.10.10.146/.hta.php
403      GET        8l       22w      215c http://10.10.10.146/.htaccess.txt
403      GET        8l       22w      216c http://10.10.10.146/.htpasswd.html
403      GET        8l       22w      210c http://10.10.10.146/.hta.asp
403      GET        8l       22w      216c http://10.10.10.146/.htaccess.html
403      GET        8l       22w      215c http://10.10.10.146/.htpasswd.php
403      GET        8l       22w      211c http://10.10.10.146/.hta.aspx
403      GET        8l       22w      215c http://10.10.10.146/.htaccess.php
403      GET        8l       22w      215c http://10.10.10.146/.htpasswd.asp
403      GET        8l       22w      210c http://10.10.10.146/.hta.jsp
403      GET        8l       22w      215c http://10.10.10.146/.htaccess.asp
403      GET        8l       22w      216c http://10.10.10.146/.htpasswd.aspx
403      GET        8l       22w      216c http://10.10.10.146/.htaccess.aspx
403      GET        8l       22w      215c http://10.10.10.146/.htpasswd.jsp
403      GET        8l       22w      215c http://10.10.10.146/.htaccess.jsp
301      GET        7l       20w      235c http://10.10.10.146/backup => http://10.10.10.146/backup/
403      GET        8l       22w      210c http://10.10.10.146/cgi-bin/
403      GET        8l       22w      215c http://10.10.10.146/cgi-bin/.html
200      GET        8l       40w      229c http://10.10.10.146/index.php
200      GET        0l        0w        0c http://10.10.10.146/lib.php
200      GET       17l       98w     3915c http://10.10.10.146/uploads/127_0_0_1.png
200      GET       17l       98w     3915c http://10.10.10.146/uploads/127_0_0_4.png
200      GET       17l       98w     3915c http://10.10.10.146/uploads/127_0_0_3.png
200      GET       17l       98w     3915c http://10.10.10.146/uploads/127_0_0_2.png
200      GET       22l       88w     1302c http://10.10.10.146/photos.php
200      GET        5l       13w      169c http://10.10.10.146/upload.php
301      GET        7l       20w      236c http://10.10.10.146/uploads => http://10.10.10.146/uploads/

```
