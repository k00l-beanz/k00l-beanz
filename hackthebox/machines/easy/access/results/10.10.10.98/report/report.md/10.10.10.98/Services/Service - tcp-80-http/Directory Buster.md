```bash
feroxbuster -u http://10.10.10.98:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt):

```
200      GET      274l     1766w    88712c http://10.10.10.98/out.jpg
200      GET       14l       31w      391c http://10.10.10.98/
200      GET       14l       31w      391c http://10.10.10.98/Index.html
301      GET        2l       10w      156c http://10.10.10.98/aspnet_client => http://10.10.10.98/aspnet_client/
200      GET       14l       31w      391c http://10.10.10.98/index.html
301      GET        2l       10w      156c http://10.10.10.98/Aspnet_client => http://10.10.10.98/Aspnet_client/
301      GET        2l       10w      156c http://10.10.10.98/aspnet_Client => http://10.10.10.98/aspnet_Client/
200      GET       14l       31w      391c http://10.10.10.98/INDEX.html
301      GET        2l       10w      156c http://10.10.10.98/ASPNET_CLIENT => http://10.10.10.98/ASPNET_CLIENT/
301      GET        2l       10w      156c http://10.10.10.98/Aspnet_Client => http://10.10.10.98/Aspnet_Client/

```
