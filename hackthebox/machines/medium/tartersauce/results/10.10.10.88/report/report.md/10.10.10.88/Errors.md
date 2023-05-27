```
[*] Port scan Top TCP Ports (top-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_quick_tcp_nmap.xml" 10.10.10.88
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -697518 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -697518 microseconds.  Ignoring time.
Segmentation fault


[*] Service scan Nmap HTTP (tcp/80/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.10.88
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Bug in http-security-headers: no string output.
Segmentation fault


[*] Port scan All TCP Ports (all-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_full_tcp_nmap.xml" 10.10.10.88
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -624302 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -624302 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -628445 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -628445 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -307055 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -307055 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -588141 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -588141 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -479520 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -479520 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -472409 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -472409 microseconds.  Ignoring time.
Segmentation fault


[*] Port scan Top 100 UDP Ports (top-100-udp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/tartersauce/results/10.10.10.88/scans/xml/_top_100_udp_nmap.xml" 10.10.10.88
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -107651 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -107651 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -324961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -324961 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -493999 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -493999 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -524752 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -524752 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -183537 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -183537 microseconds.  Ignoring time.
Segmentation fault



```