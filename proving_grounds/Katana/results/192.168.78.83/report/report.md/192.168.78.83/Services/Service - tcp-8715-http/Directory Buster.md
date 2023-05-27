```bash
feroxbuster -u http://192.168.78.83:8715/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_feroxbuster_dirbuster.txt):

```
WLD      GET        7l       12w      195c Got 401 for http://192.168.78.83:8715/e653d9b043f04134a713ce04ef2e716d (url length: 32)
WLD      GET        7l       12w      195c Got 401 for http://192.168.78.83:8715/c78e966b9d3144a896365655f084a6896c0253dcf5db400082061e9c7d62c3e17ee2f76a1e9048f9980ac4ddceaee944 (url length: 96)
403      GET        7l       10w      169c http://192.168.78.83:8715/.html
403      GET        7l       10w      169c http://192.168.78.83:8715/.git/logs/.html
403      GET        7l       10w      169c http://192.168.78.83:8715/.hta
403      GET        7l       10w      169c http://192.168.78.83:8715/.htaccess
403      GET        7l       10w      169c http://192.168.78.83:8715/.htpasswd
403      GET        7l       10w      169c http://192.168.78.83:8715/.hta.txt
403      GET        7l       10w      169c http://192.168.78.83:8715/.htaccess.txt
403      GET        7l       10w      169c http://192.168.78.83:8715/.htpasswd.txt
403      GET        7l       10w      169c http://192.168.78.83:8715/.hta.html
403      GET        7l       10w      169c http://192.168.78.83:8715/.htpasswd.html
403      GET        7l       10w      169c http://192.168.78.83:8715/.htaccess.html
403      GET        7l       10w      169c http://192.168.78.83:8715/.hta.asp
403      GET        7l       10w      169c http://192.168.78.83:8715/.htpasswd.asp
403      GET        7l       10w      169c http://192.168.78.83:8715/.htaccess.asp
403      GET        7l       10w      169c http://192.168.78.83:8715/.hta.aspx
403      GET        7l       10w      169c http://192.168.78.83:8715/.htpasswd.aspx
403      GET        7l       10w      169c http://192.168.78.83:8715/.htaccess.aspx
403      GET        7l       10w      169c http://192.168.78.83:8715/.hta.jsp
403      GET        7l       10w      169c http://192.168.78.83:8715/.htpasswd.jsp
403      GET        7l       10w      169c http://192.168.78.83:8715/.htaccess.jsp
403      GET        7l       10w      169c http://192.168.78.83:8715/cgi-bin/.html

```
