```bash
feroxbuster -u https://10.10.10.239:443/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_feroxbuster_dirbuster.txt"
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_feroxbuster_dirbuster.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_feroxbuster_dirbuster.txt):

```
WLD      GET        9l       30w      303c Got 403 for https://10.10.10.239/956bfd0c996e4e0d8633d5ca5be1a397 (url length: 32)
403      GET       11l       47w      422c https://10.10.10.239/licenses
403      GET       11l       47w      422c https://10.10.10.239/server-info
403      GET       11l       47w      422c https://10.10.10.239/server-status

```
