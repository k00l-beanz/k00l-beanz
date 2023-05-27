```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_full_tcp_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_full_tcp_nmap.xml" 192.168.78.83
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_full_tcp_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_full_tcp_nmap.txt):

```
# Nmap 7.92 scan initiated Wed Dec  7 20:14:15 2022 as: nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/_full_tcp_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/Katana/results/192.168.78.83/scans/xml/_full_tcp_nmap.xml 192.168.78.83
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
Nmap scan report for 192.168.78.83
Host is up, received user-set (0.021s latency).
Scanned at 2022-12-07 20:14:15 EST for 63s
Not shown: 65529 closed tcp ports (reset)
PORT     STATE SERVICE       REASON         VERSION
21/tcp   open  ftp           syn-ack ttl 63 vsftpd 3.0.3
22/tcp   open  ssh           syn-ack ttl 63 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 89:4f:3a:54:01:f8:dc:b6:6e:e0:78:fc:60:a6:de:35 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDp0J8d7K55SuQO/Uuh8GyKm2xlwCUG3/Jb6+7RlfgbwrCIOzuKXICcMHq4i8z52l/0x0JnN0GUIeNu6Ek/ZGEMK4y+zvAs0R6oPNlScpx0IaLDXTGrjPOcutmx+fy6WDW3/jJGLxwu+55d6pAjzzQR37P1eqH8k9F6fbv6YUFbU+i68x9p5bXCC1m17PDO98Che+q32N6yM26CrQMOl5t1OzO3t1pbvMd3VOQA8Qd+fhz5tpxtRBTSM9ylQj2B+z6XjJnbMPhnO3C1oaYHjjL6KiTfD5YabDqsBf+ZHIdZpM+7fOqKkgHa4bbIWPUXB/OuOJnORvEeRCALOzjcSrxr
|   256 dd:ac:cc:4e:43:81:6b:e3:2d:f3:12:a1:3e:4b:a3:22 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDBsZi0z31ChZ3SWO/gDe+8WyFVPrFX7KgZNp8u/1vlhOSrmdZ32WAZZhTT8bblwgv83FeXPvH7btjDMzTuoYA8=
|   256 cc:e6:25:c0:c6:11:9f:88:f6:c4:26:1e:de:fa:e9:8b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICo+dAzFw2csa366udGUkSre2W0qWWGoyWXwKiHk3YQc
80/tcp   open  http          syn-ack ttl 63 Apache httpd 2.4.38 ((Debian))
|_http-title: Katana X
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache/2.4.38 (Debian)
7080/tcp open  ssl/empowerid syn-ack ttl 63 LiteSpeed
|_http-title: Did not follow redirect to https://192.168.78.83:7080/
| http-methods: 
|_  Supported Methods: GET HEAD POST
| ssl-cert: Subject: commonName=katana/organizationName=webadmin/countryName=US/X509v3 Subject Alternative Name=DNS.1=1.55.254.232
| Issuer: commonName=katana/organizationName=webadmin/countryName=US/X509v3 Subject Alternative Name=DNS.1=1.55.254.232
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-05-11T13:57:36
| Not valid after:  2022-05-11T13:57:36
| MD5:   0443 4a65 9ba1 0b75 ea8d d1b8 c855 e495
| SHA-1: f89e f85e e6b3 6b10 4ebc 5354 80a0 0ae3 7e10 50cc
| -----BEGIN CERTIFICATE-----
| MIIDfTCCAmWgAwIBAgIUAXyRP1qy58OWLRWfP6CNoErg93wwDQYJKoZIhvcNAQEL
| BQAwTjEPMA0GA1UEAwwGa2F0YW5hMREwDwYDVQQKDAh3ZWJhZG1pbjELMAkGA1UE
| BhMCVVMxGzAZBgNVHREMEkROUy4xPTEuNTUuMjU0LjIzMjAeFw0yMDA1MTExMzU3
| MzZaFw0yMjA1MTExMzU3MzZaME4xDzANBgNVBAMMBmthdGFuYTERMA8GA1UECgwI
| d2ViYWRtaW4xCzAJBgNVBAYTAlVTMRswGQYDVR0RDBJETlMuMT0xLjU1LjI1NC4y
| MzIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUrg/knoyr6L8pJhlZ
| bEp2vj/1S/2lEiYzl3CbBtCDcNnSQLB2b7hC5vkzIFT5XOHcboXGSWWZ7g1Mlo/U
| irtoeuFYH0KyqYqKH6cJIUCUuIvsKFvEuSpcLB5oHMH1bNYHl8gk2uxnXDRHfxL1
| mhhV+tDewjGu7TzjWcGapvZmJKCQYJto6X4JagN/Xx7bWZQYKb22E/K/17PPg1Wg
| szg2C8a/sj/GWBiw5HADUx5FnQY0FfljwBBSQr10nGiex+w/NAYK8obUTsvUz1P7
| h2aG1V/9FtXHa6HK7YrApieVVTyBZTf4adj5OvmIT5w43vEBZXgCTUMLcf6JmiGy
| OMmdAgMBAAGjUzBRMB0GA1UdDgQWBBRpfqzDB3dS6IMabVgYjX+nQE8xZzAfBgNV
| HSMEGDAWgBRpfqzDB3dS6IMabVgYjX+nQE8xZzAPBgNVHRMBAf8EBTADAQH/MA0G
| CSqGSIb3DQEBCwUAA4IBAQCGCOYvcHj7XrE0fnuDbc4rdQzSVOCOK31F4aV4pWEh
| a6h/WQX9wQBHcs5XPl9D4JVDFQvtxBPWsmnzqqXm8CbeZ7cfAjzPGd994jFBeom6
| 3gnAXmCFSlRsPuqvKkGhBaSDDtzrWE4eZC0H2g9BJp0f6w4sRJSjCH1wZ30Jvgm+
| 9Hkcw9cG0WxkHEBk3SPB7d9iG6rFLJvZE4dcVbA6jtkhQZDrCAqaH69exWtKSQpV
| oBu7+tHFy/8uv7yRuC4fQY7Nmc0JD5otoax1yOpGN/eSz8zRFh+jl5VzdONtXQCO
| H8o8x5fxVi65kRQYil6UcG3lX56V51h/33dxWIDw+lAE
|_-----END CERTIFICATE-----
| tls-alpn: 
|   h2
|   spdy/3
|   spdy/2
|_  http/1.1
|_http-server-header: LiteSpeed
|_ssl-date: TLS randomness does not represent time
8088/tcp open  http          syn-ack ttl 63 LiteSpeed httpd
|_http-title: Katana X
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: LiteSpeed
8715/tcp open  http          syn-ack ttl 63 nginx 1.14.2
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=Restricted Content
|_http-title: 401 Authorization Required
|_http-server-header: nginx/1.14.2
Aggressive OS guesses: Linux 2.6.32 (91%), Linux 3.4 (91%), Linux 3.5 (91%), Linux 4.2 (91%), Linux 4.4 (91%), Synology DiskStation Manager 5.1 (91%), WatchGuard Fireware 11.8 (91%), Linux 2.6.35 (90%), Linux 3.10 (90%), Linux 2.6.32 or 3.10 (90%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/7%OT=21%CT=1%CU=36068%PV=Y%DS=2%DC=T%G=Y%TM=63913AA
OS:6%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=109%TI=Z%II=I%TS=A)OPS(O1=M
OS:54EST11NW7%O2=M54EST11NW7%O3=M54ENNT11NW7%O4=M54EST11NW7%O5=M54EST11NW7%
OS:O6=M54EST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%
OS:DF=Y%T=40%W=FAF0%O=M54ENNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=
OS:0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
OS:T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%
OS:RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 44.120 days (since Mon Oct 24 18:23:08 2022)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8080/tcp)
HOP RTT      ADDRESS
1   20.86 ms 192.168.49.1
2   21.30 ms 192.168.78.83

Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Dec  7 20:15:18 2022 -- 1 IP address (1 host up) scanned in 63.18 seconds

```
