```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/xml/_quick_tcp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/xml/_full_tcp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/xml/_top_100_udp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.10.77

nmap -vv --reason -Pn -T4 -sV -p 25 --script="banner,(smtp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp25/tcp_25_smtp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp25/xml/tcp_25_smtp_nmap.xml" 10.10.10.77

hydra smtp-enum://10.10.10.77:25/vrfy -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" 2>&1

hydra smtp-enum://10.10.10.77:25/expn -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" 2>&1


```