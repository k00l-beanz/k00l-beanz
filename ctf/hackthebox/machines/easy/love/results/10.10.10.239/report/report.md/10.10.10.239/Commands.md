```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/xml/_quick_tcp_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/xml/_full_tcp_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/xml/_top_100_udp_nmap.xml" 10.10.10.239

impacket-getArch -target 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 135 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/tcp_135_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp135/xml/tcp_135_rpc_nmap.xml" 10.10.10.239

impacket-rpcdump -port 135 10.10.10.239

feroxbuster -u https://10.10.10.239:443/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_feroxbuster_dirbuster.txt"

curl -sSikf https://10.10.10.239:443/.well-known/security.txt

curl -sSikf https://10.10.10.239:443/robots.txt

curl -sSik https://10.10.10.239:443/

nmap -vv --reason -Pn -T4 -sV -p 443 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/xml/tcp_443_https_nmap.xml" 10.10.10.239

sslscan --show-certificate --no-colour 10.10.10.239:443 2>&1

whatweb --color=never --no-errors -a 3 -v https://10.10.10.239:443 2>&1

wkhtmltoimage --format png https://10.10.10.239:443/ /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp443/tcp_443_https_screenshot.png

enum4linux -a -M -l -d 10.10.10.239 2>&1

nbtscan -rvh 10.10.10.239 2>&1

nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.239

smbclient -L //10.10.10.239 -N -I 10.10.10.239 2>&1

smbmap -H 10.10.10.239 -P 445 2>&1

nmap -vv --reason -Pn -T4 -sV -p 3306 --script="banner,(mysql* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/tcp_3306_mysql_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp3306/xml/tcp_3306_mysql_nmap.xml" 10.10.10.239

feroxbuster -u http://10.10.10.239:5000/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.239:5000/.well-known/security.txt

curl -sSikf http://10.10.10.239:5000/robots.txt

curl -sSik http://10.10.10.239:5000/

nmap -vv --reason -Pn -T4 -sV -p 5000 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/xml/tcp_5000_http_nmap.xml" 10.10.10.239

whatweb --color=never --no-errors -a 3 -v http://10.10.10.239:5000 2>&1

wkhtmltoimage --format png http://10.10.10.239:5000/ /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5000/tcp_5000_http_screenshot.png

smbmap -u null -p "" -H 10.10.10.239 -P 445 2>&1

smbmap -H 10.10.10.239 -P 445 -R 2>&1

smbmap -u null -p "" -H 10.10.10.239 -P 445 -R 2>&1

smbmap -H 10.10.10.239 -P 445 -x "ipconfig /all" 2>&1

smbmap -u null -p "" -H 10.10.10.239 -P 445 -x "ipconfig /all" 2>&1

feroxbuster -u http://10.10.10.239:5985/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.239:5985/.well-known/security.txt

curl -sSikf http://10.10.10.239:5985/robots.txt

curl -sSik http://10.10.10.239:5985/

nmap -vv --reason -Pn -T4 -sV -p 5985 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/xml/tcp_5985_http_nmap.xml" 10.10.10.239

whatweb --color=never --no-errors -a 3 -v http://10.10.10.239:5985 2>&1

wkhtmltoimage --format png http://10.10.10.239:5985/ /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp5985/tcp_5985_http_screenshot.png

feroxbuster -u http://10.10.10.239:47001/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp47001/tcp_47001_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.239:47001/.well-known/security.txt

curl -sSikf http://10.10.10.239:47001/robots.txt

curl -sSik http://10.10.10.239:47001/

nmap -vv --reason -Pn -T4 -sV -p 47001 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp47001/tcp_47001_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp47001/xml/tcp_47001_http_nmap.xml" 10.10.10.239

whatweb --color=never --no-errors -a 3 -v http://10.10.10.239:47001 2>&1

wkhtmltoimage --format png http://10.10.10.239:47001/ /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp47001/tcp_47001_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 49664 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49664/tcp_49664_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49664/xml/tcp_49664_rpc_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 49665 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49665/tcp_49665_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49665/xml/tcp_49665_rpc_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 49666 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49666/tcp_49666_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49666/xml/tcp_49666_rpc_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 49667 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49667/tcp_49667_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49667/xml/tcp_49667_rpc_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 49668 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49668/tcp_49668_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49668/xml/tcp_49668_rpc_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 49669 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49669/tcp_49669_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49669/xml/tcp_49669_rpc_nmap.xml" 10.10.10.239

nmap -vv --reason -Pn -T4 -sV -p 49670 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49670/tcp_49670_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/love/results/10.10.10.239/scans/tcp49670/xml/tcp_49670_rpc_nmap.xml" 10.10.10.239


```