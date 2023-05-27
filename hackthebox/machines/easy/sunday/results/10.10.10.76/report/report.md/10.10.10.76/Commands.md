```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_quick_tcp_nmap.xml" 10.10.10.76

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_full_tcp_nmap.xml" 10.10.10.76

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_top_100_udp_nmap.xml" 10.10.10.76

nmap -vv --reason -Pn -T4 -sU -sV -p 111 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/xml/udp_111_rpc_nmap.xml" 10.10.10.76

nmap -vv --reason -Pn -T4 -sU -sV -p 111 --script="banner,(rpcinfo or nfs*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_nfs_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/xml/udp_111_nfs_nmap.xml" 10.10.10.76

showmount -e 10.10.10.76 2>&1

nmap -vv --reason -Pn -T4 -sV -p 111 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/tcp_111_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/xml/tcp_111_rpc_nmap.xml" 10.10.10.76

nmap -vv --reason -Pn -T4 -sV -p 111 --script="banner,(rpcinfo or nfs*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/tcp_111_nfs_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/xml/tcp_111_nfs_nmap.xml" 10.10.10.76

showmount -e 10.10.10.76 2>&1

nmap -vv --reason -Pn -T4 -sV -p 79 --script="banner,finger" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp79/tcp_79_finger_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp79/xml/tcp_79_finger_nmap.xml" 10.10.10.76

feroxbuster -u https://10.10.10.76:6787/ -t 10 -w /root/.config/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp6787/tcp_6787_https_feroxbuster_dirbuster.txt"

curl -sSikf https://10.10.10.76:6787/.well-known/security.txt

curl -sSikf https://10.10.10.76:6787/robots.txt

curl -sSik https://10.10.10.76:6787/

nmap -vv --reason -Pn -T4 -sV -p 6787 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp6787/tcp_6787_https_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp6787/xml/tcp_6787_https_nmap.xml" 10.10.10.76

sslscan --show-certificate --no-colour 10.10.10.76:6787 2>&1

whatweb --color=never --no-errors -a 3 -v https://10.10.10.76:6787 2>&1

wkhtmltoimage --format png https://10.10.10.76:6787/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp6787/tcp_6787_https_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 22022 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp22022/tcp_22022_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp22022/xml/tcp_22022_ssh_nmap.xml" 10.10.10.76


```