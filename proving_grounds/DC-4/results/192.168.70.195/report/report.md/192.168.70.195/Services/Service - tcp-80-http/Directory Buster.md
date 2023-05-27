```bash
feroxbuster -u http://192.168.70.195:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
200      GET       29l       46w      340c http://192.168.70.195/css/styles.css
302      GET       15l       17w        0c http://192.168.70.195/login.php => index.php
200      GET       23l       40w        0c http://192.168.70.195/
200      GET       23l       40w        0c http://192.168.70.195/index.php
302      GET       25l       67w        0c http://192.168.70.195/command.php => index.php
301      GET        7l       11w      170c http://192.168.70.195/css => http://192.168.70.195/css/
301      GET        7l       11w      170c http://192.168.70.195/images => http://192.168.70.195/images/
302      GET       10l       13w        0c http://192.168.70.195/logout.php => index.php

```
