```bash
feroxbuster -u http://10.10.10.111:9999/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp9999/tcp_9999_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp9999/tcp_9999_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp9999/tcp_9999_http_feroxbuster_dirbuster.txt):

```
200      GET       28l       71w      637c http://10.10.10.111:9999/
403      GET        7l       11w      178c http://10.10.10.111:9999/.html
403      GET        7l       11w      178c http://10.10.10.111:9999/.git/logs/.html
403      GET        7l       11w      178c http://10.10.10.111:9999/.htaccess
403      GET        7l       11w      178c http://10.10.10.111:9999/.hta
403      GET        7l       11w      178c http://10.10.10.111:9999/.htpasswd
403      GET        7l       11w      178c http://10.10.10.111:9999/.htaccess.txt
403      GET        7l       11w      178c http://10.10.10.111:9999/.hta.txt
403      GET        7l       11w      178c http://10.10.10.111:9999/.htpasswd.txt
403      GET        7l       11w      178c http://10.10.10.111:9999/.hta.html
403      GET        7l       11w      178c http://10.10.10.111:9999/.htaccess.html
403      GET        7l       11w      178c http://10.10.10.111:9999/.htpasswd.html
403      GET        7l       11w      178c http://10.10.10.111:9999/.hta.asp
403      GET        7l       11w      178c http://10.10.10.111:9999/.htaccess.asp
403      GET        7l       11w      178c http://10.10.10.111:9999/.htpasswd.asp
403      GET        7l       11w      178c http://10.10.10.111:9999/.htaccess.aspx
403      GET        7l       11w      178c http://10.10.10.111:9999/.hta.aspx
403      GET        7l       11w      178c http://10.10.10.111:9999/.htpasswd.aspx
403      GET        7l       11w      178c http://10.10.10.111:9999/.htaccess.jsp
403      GET        7l       11w      178c http://10.10.10.111:9999/.hta.jsp
403      GET        7l       11w      178c http://10.10.10.111:9999/.htpasswd.jsp
301      GET        7l       13w      194c http://10.10.10.111:9999/admin => http://10.10.10.111:9999/admin/
301      GET        7l       13w      194c http://10.10.10.111:9999/backup => http://10.10.10.111:9999/backup/
403      GET        7l       11w      178c http://10.10.10.111:9999/cgi-bin/.html
301      GET        7l       13w      194c http://10.10.10.111:9999/dev => http://10.10.10.111:9999/dev/
301      GET        7l       13w      194c http://10.10.10.111:9999/test => http://10.10.10.111:9999/test/
301      GET        7l       13w      194c http://10.10.10.111:9999/loop => http://10.10.10.111:9999/loop/

```
