```
[*] Port scan Top TCP Ports (top-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/xml/_quick_tcp_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -392845 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -392845 microseconds.  Ignoring time.
Segmentation fault


[*] Service scan Nmap SSH (tcp/22/ssh/nmap-ssh) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Port scan All TCP Ports (all-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/xml/_full_tcp_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -592513 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -592513 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -594629 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -594629 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -241918 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -241918 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -443928 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -443928 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -110008 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -110008 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -562223 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -562223 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -519663 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -519663 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -520689 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -520689 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -515075 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -515075 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -514496 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -514496 microseconds.  Ignoring time.
Segmentation fault


[*] Service scan wkhtmltoimage (tcp/1880/http/wkhtmltoimage) ran a command which returned a non-zero exit code (1).
[-] Command: wkhtmltoimage --format png http://10.10.10.111:1880/ /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp1880/tcp_1880_http_screenshot.png
[-] Error Output:
QStandardPaths: XDG_RUNTIME_DIR not set, defaulting to '/tmp/runtime-root'
Loading page (1/2)
[>                                                           ] 0%
[=============>                                              ] 23%
[===========================>                                ] 45%
[=======================================>                    ] 65%
Error: Failed to load http://10.10.10.111:1880/settings?_=1668634990534, with network status code 204 and http status code 401 - Host requires authentication
[============================================================] 100%
Rendering (2/2)
[>                                                           ] 0%
[===============>                                            ] 25%
[============================================================] 100%
Done
Exit with code 1 due to network error: AuthenticationRequiredError


[*] Service scan Nmap HTTP (tcp/9999/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 9999 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp9999/tcp_9999_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp9999/xml/tcp_9999_http_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault


[*] Service scan Nmap HTTP (tcp/1880/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 1880 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp1880/tcp_1880_http_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp1880/xml/tcp_1880_http_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault


[*] Port scan Top 100 UDP Ports (top-100-udp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/xml/_top_100_udp_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap SMB (udp/137/netbios-ns/nmap-smb) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/udp_137_smb_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/xml/udp_137_smb_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap SMB (tcp/445/netbios-ssn/nmap-smb) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 445 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/tcp_445_smb_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp445/xml/tcp_445_smb_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap SMB (tcp/139/netbios-ssn/nmap-smb) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 139 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp139/tcp_139_smb_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp139/xml/tcp_139_smb_nmap.xml" 10.10.10.111
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault



```