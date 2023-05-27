```bash
feroxbuster -u http://192.168.78.83:8088/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_feroxbuster_dirbuster.txt):

```
200      GET       23l       73w      655c http://192.168.78.83:8088/
403      GET       14l      107w     1227c http://192.168.78.83:8088/.htaccess
301      GET       14l      109w     1260c http://192.168.78.83:8088/blocked => http://192.168.78.83:8088/blocked/
301      GET       14l      109w     1260c http://192.168.78.83:8088/cgi-bin => http://192.168.78.83:8088/cgi-bin/
301      GET       14l      109w     1260c http://192.168.78.83:8088/css => http://192.168.78.83:8088/css/
301      GET       14l      109w     1260c http://192.168.78.83:8088/docs => http://192.168.78.83:8088/docs/
200      GET       11l       25w      195c http://192.168.78.83:8088/error404.html
301      GET       14l      109w     1260c http://192.168.78.83:8088/img => http://192.168.78.83:8088/img/
200      GET       23l       73w      655c http://192.168.78.83:8088/index.html
200      GET      494l     2889w        0c http://192.168.78.83:8088/phpinfo.php
301      GET       14l      109w     1260c http://192.168.78.83:8088/protected => http://192.168.78.83:8088/protected/
200      GET       35l      202w     1800c http://192.168.78.83:8088/upload.php
200      GET      198l      531w     6480c http://192.168.78.83:8088/upload.html

```
