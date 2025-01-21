```bash
feroxbuster -u http://10.10.10.239:5000/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_feroxbuster_dirbuster.txt):

```
WLD      GET        9l       30w      304c Got 403 for http://10.10.10.239:5000/0597cb6beed948a8a6d063cc1556ce53 (url length: 32)
403      GET       11l       47w      423c http://10.10.10.239:5000/licenses
403      GET       11l       47w      423c http://10.10.10.239:5000/server-info
403      GET       11l       47w      423c http://10.10.10.239:5000/server-status

```
