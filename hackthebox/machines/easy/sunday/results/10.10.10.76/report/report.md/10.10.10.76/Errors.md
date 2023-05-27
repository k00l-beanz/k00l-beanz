```
[*] Port scan Top 100 UDP Ports (top-100-udp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -A --top-ports 100 -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_top_100_udp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_top_100_udp_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
RTTVAR has grown to over 2.3 seconds, decreasing to 2.0
Segmentation fault


[*] Service scan showmount (udp/111/rpcbind/showmount) ran a command which returned a non-zero exit code (1).
[-] Command: showmount -e 10.10.10.76 2>&1
[-] Error Output:


[*] Service scan Nmap MSRPC (udp/111/rpcbind/nmap-msrpc) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -sV -p 111 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/xml/udp_111_rpc_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap NFS (udp/111/rpcbind/nmap-nfs) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sU -sV -p 111 --script="banner,(rpcinfo or nfs*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/udp_111_nfs_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/udp111/xml/udp_111_nfs_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Port scan Top TCP Ports (top-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_quick_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_quick_tcp_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
adjust_timeouts2: packet supposedly had rtt of -115674 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -115674 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -139793 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -139793 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -138877 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -138877 microseconds.  Ignoring time.
Segmentation fault


[*] Service scan showmount (tcp/111/rpcbind/showmount) ran a command which returned a non-zero exit code (1).
[-] Command: showmount -e 10.10.10.76 2>&1
[-] Error Output:


[*] Service scan Nmap MSRPC (tcp/111/rpcbind/nmap-msrpc) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 111 --script="banner,msrpc-enum,rpc-grind,rpcinfo" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/tcp_111_rpc_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/xml/tcp_111_rpc_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap NFS (tcp/111/rpcbind/nmap-nfs) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 111 --script="banner,(rpcinfo or nfs*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/tcp_111_nfs_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp111/xml/tcp_111_nfs_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Port scan All TCP Ports (all-tcp-ports) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/xml/_full_tcp_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap SSH (tcp/22022/ssh/nmap-ssh) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 22022 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp22022/tcp_22022_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp22022/xml/tcp_22022_ssh_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap HTTP (tcp/6787/http/nmap-http) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 6787 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp6787/tcp_6787_https_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp6787/xml/tcp_6787_https_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault


[*] Service scan Nmap finger (tcp/79/finger/nmap-finger) ran a command which returned a non-zero exit code (139).
[-] Command: nmap -vv --reason -Pn -T4 -sV -p 79 --script="banner,finger" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp79/tcp_79_finger_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/sunday/results/10.10.10.76/scans/tcp79/xml/tcp_79_finger_nmap.xml" 10.10.10.76
[-] Error Output:
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Segmentation fault



```