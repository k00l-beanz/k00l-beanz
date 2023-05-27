```bash
[*] ftp on tcp/21

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp21/tcp_21_ftp_hydra.txt" ftp://192.168.78.83

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 21 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp21/tcp_21_ftp_medusa.txt" -M ftp -h 192.168.78.83

[*] ssh on tcp/22

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 22 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp22/tcp_22_ssh_hydra.txt" ssh://192.168.78.83

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 22 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp22/tcp_22_ssh_medusa.txt" -M ssh -h 192.168.78.83

[*] http on tcp/80

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://192.168.78.83:80 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -o /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_auth_hydra.txt" http-get://192.168.78.83/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_auth_medusa.txt" -M http -h 192.168.78.83 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_form_hydra.txt" http-post-form://192.168.78.83/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_form_medusa.txt" -M web-form -h 192.168.78.83 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (nikto) old but generally reliable web server enumeration tool:

		nikto -ask=no -h http://192.168.78.83:80 2>&1 | tee "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_nikto.txt"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://192.168.78.83:80/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_wpscan.txt"

[*] http on tcp/8088

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://192.168.78.83:8088 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -o /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 8088 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_auth_hydra.txt" http-get://192.168.78.83/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 8088 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_auth_medusa.txt" -M http -h 192.168.78.83 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 8088 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_form_hydra.txt" http-post-form://192.168.78.83/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 8088 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_form_medusa.txt" -M web-form -h 192.168.78.83 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (nikto) old but generally reliable web server enumeration tool:

		nikto -ask=no -h http://192.168.78.83:8088 2>&1 | tee "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nikto.txt"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://192.168.78.83:8088/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_wpscan.txt"

[*] http on tcp/8715

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://192.168.78.83:8715 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -o /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 8715 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_auth_hydra.txt" http-get://192.168.78.83/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 8715 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_auth_medusa.txt" -M http -h 192.168.78.83 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 8715 -o "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_form_hydra.txt" http-post-form://192.168.78.83/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 8715 -O "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_form_medusa.txt" -M web-form -h 192.168.78.83 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (nikto) old but generally reliable web server enumeration tool:

		nikto -ask=no -h http://192.168.78.83:8715 2>&1 | tee "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_nikto.txt"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://192.168.78.83:8715/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_wpscan.txt"


```