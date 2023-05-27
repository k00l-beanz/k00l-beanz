```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 192.168.70.195
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.92 scan initiated Thu Dec  1 21:43:50 2022 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/ProvingGrounds/DC-4/results/192.168.70.195/scans/tcp22/xml/tcp_22_ssh_nmap.xml 192.168.70.195
Nmap scan report for 192.168.70.195
Host is up, received user-set (0.037s latency).
Scanned at 2022-12-01 21:43:51 EST for 1s

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|_    password
| ssh2-enum-algos: 
|   kex_algorithms: (10)
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group14-sha256
|       diffie-hellman-group14-sha1
|   server_host_key_algorithms: (5)
|       ssh-rsa
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (6)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
|       aes128-gcm@openssh.com
|       aes256-gcm@openssh.com
|   mac_algorithms: (10)
|       umac-64-etm@openssh.com
|       umac-128-etm@openssh.com
|       hmac-sha2-256-etm@openssh.com
|       hmac-sha2-512-etm@openssh.com
|       hmac-sha1-etm@openssh.com
|       umac-64@openssh.com
|       umac-128@openssh.com
|       hmac-sha2-256
|       hmac-sha2-512
|       hmac-sha1
|   compression_algorithms: (2)
|       none
|_      zlib@openssh.com
|_banner: SSH-2.0-OpenSSH_7.4p1 Debian-10+deb9u6
| ssh-hostkey: 
|   2048 8d:60:57:06:6c:27:e0:2f:76:2c:e6:42:c0:01:ba:25 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCp6/VowbK8MWfMDQsxHRV2yvL8ZO+FEkyIBPnDwTVKkJiVKaJMZ5ztAwTnkc30c3tvC/yCqDAJ5IbHzgvR3kHKS37d17K+/OLxalDutFjrWjG7mBxhMW/0gnrCqJokZBDXDuvHQonajsfSN6FmWoP0PDsfL8NQXwWIoMvTRYHtiEQqczV5CYZZtMKuOyiLCiWINUqKMwY+PTb0M9RzSGYSJvN8sZZnvIw/xU7xBCmaWuq8h2dIfsxy+FhrwZMhvhJOpBYtwZB+hos3bbV5FKHhVztxEo+Y2vyKTl6MXJ4qwCChJdaBAip/aUt1zDoF3cIb+yebteyDk8KIqmp5Ju4r
|   256 e7:83:8c:d7:bb:84:f3:2e:e8:a2:5f:79:6f:8e:19:30 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIbZ4PXPXShXCcbe25IY3SYbzB4hxP4K2BliUGtuYSABZosGlLlL1Pi214yCLs3ORpGxsRIHv8R0KFQX+5SNSog=
|   256 fd:39:47:8a:5e:58:33:99:73:73:9e:22:7f:90:4f:4b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDcvQZ2DbLqSSOzIbIXhyrDJ15duVKd9TEtxfX35ubsM
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Dec  1 21:43:52 2022 -- 1 IP address (1 host up) scanned in 1.94 seconds

```
