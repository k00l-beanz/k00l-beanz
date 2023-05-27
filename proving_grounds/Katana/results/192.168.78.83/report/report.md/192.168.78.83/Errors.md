```
[*] Port scan Top TCP Ports (top-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_quick_tcp_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap SSH (tcp/22/ssh/nmap-ssh) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap FTP (tcp/21/ftp/nmap-ftp) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap HTTP (tcp/80/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp80/xml/tcp_80_http_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault


[*] Port scan All TCP Ports (all-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_full_tcp_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -180776 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -180776 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -436363 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -436363 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -436016 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -436016 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -434216 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -434216 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -435884 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -435884 microseconds.  Ignoring time.
Segmentation fault


[*] Service scan wkhtmltoimage (tcp/8715/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://192.168.78.83:8715/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
Error: Authentication Required
Error: Failed to load http://192.168.78.83:8715/, with network status code 204 and http status code 401 - Host requires authentication
[==============================>                             ] 50%
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: AuthenticationRequiredError


[*] Service scan Nmap HTTP (tcp/8088/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 8088 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/tcp_8088_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8088/xml/tcp_8088_http_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault


[*] Service scan Nmap HTTP (tcp/8715/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 8715 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/tcp_8715_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/tcp8715/xml/tcp_8715_http_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault


[*] Port scan Top 100 UDP Ports (top-100-udp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_top_100_udp_nmap.xml" 192.168.78.83
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -95241 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -95241 microseconds.  Ignoring time.
Segmentation fault



```