```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_quick_tcp_nmap.xml" 192.168.78.83

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_full_tcp_nmap.xml" 192.168.78.83

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_top_100_udp_nmap.xml" 192.168.78.83

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 192.168.78.83

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.78.83

feroxbuster -u http://192.168.78.83:80/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.78.83:80/.well-known/security.txt

curl -sSikf http://192.168.78.83:80/robots.txt

curl -sSik http://192.168.78.83:80/

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.78.83

whatweb --color=never --no-errors -a 3 -v http://192.168.78.83:80 2>&1

wkhtmltoimage --format png http://192.168.78.83:80/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_screenshot.png

feroxbuster -u http://192.168.78.83:8088/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.78.83:8088/.well-known/security.txt

curl -sSikf http://192.168.78.83:8088/robots.txt

curl -sSik http://192.168.78.83:8088/

nmap -vv --reason -Pn -T4 -sV -p 8088 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/xml/tcp_8088_http_nmap.xml" 192.168.78.83

whatweb --color=never --no-errors -a 3 -v http://192.168.78.83:8088 2>&1

wkhtmltoimage --format png http://192.168.78.83:8088/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_screenshot.png

sslscan --show-certificate --no-colour 192.168.78.83:7080 2>&1

feroxbuster -u http://192.168.78.83:8715/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_feroxbuster_dirbuster.txt"

curl -sSikf http://192.168.78.83:8715/.well-known/security.txt

curl -sSikf http://192.168.78.83:8715/robots.txt

curl -sSik http://192.168.78.83:8715/

nmap -vv --reason -Pn -T4 -sV -p 8715 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/xml/tcp_8715_http_nmap.xml" 192.168.78.83

whatweb --color=never --no-errors -a 3 -v http://192.168.78.83:8715 2>&1

wkhtmltoimage --format png http://192.168.78.83:8715/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_screenshot.png


```