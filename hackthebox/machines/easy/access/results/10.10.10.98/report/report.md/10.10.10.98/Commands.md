```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/xml/_quick_tcp_nmap.xml" 10.10.10.98

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/xml/_full_tcp_nmap.xml" 10.10.10.98

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/xml/_top_100_udp_nmap.xml" 10.10.10.98

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.10.98

nmap -vv --reason -Pn -T4 -sV -p 23 --script="banner,telnet-encryption,telnet-ntlm-info" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp23/tcp_23_telnet-nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp23/xml/tcp_23_telnet_nmap.xml" 10.10.10.98

feroxbuster -u http://10.10.10.98:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.10.98:80/.well-known/security.txt

curl -sSikf http://10.10.10.98:80/robots.txt

curl -sSik http://10.10.10.98:80/

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.98

whatweb --color=never --no-errors -a 3 -v http://10.10.10.98:80 2>&1

wkhtmltoimage --format png http://10.10.10.98:80/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/access/results/10.10.10.98/scans/tcp80/tcp_80_http_screenshot.png


```