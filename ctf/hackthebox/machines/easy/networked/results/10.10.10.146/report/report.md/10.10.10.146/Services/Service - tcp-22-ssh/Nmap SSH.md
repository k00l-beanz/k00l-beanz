```bash
nmap -vv --reason -Pn -T4 -sV -p 22 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp22/tcp_22_ssh_nmap.txt" -oX "/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp22/xml/tcp_22_ssh_nmap.xml" 10.10.10.146
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp22/tcp_22_ssh_nmap.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp22/tcp_22_ssh_nmap.txt):

```
# Nmap 7.92 scan initiated Wed Sep 28 00:00:15 2022 as: nmap -vv --reason -Pn -T4 -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp22/tcp_22_ssh_nmap.txt -oX /home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/easy/networked/results/10.10.10.146/scans/tcp22/xml/tcp_22_ssh_nmap.xml 10.10.10.146
Nmap scan report for 10.10.10.146
Host is up, received user-set (0.014s latency).
Scanned at 2022-09-28 00:00:21 EDT for 21s

PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 63 OpenSSH 7.4 (protocol 2.0)
|_banner: SSH-2.0-OpenSSH_7.4
| ssh2-enum-algos: 
|   kex_algorithms: (12)
|       curve25519-sha256
|       curve25519-sha256@libssh.org
|       ecdh-sha2-nistp256
|       ecdh-sha2-nistp384
|       ecdh-sha2-nistp521
|       diffie-hellman-group-exchange-sha256
|       diffie-hellman-group16-sha512
|       diffie-hellman-group18-sha512
|       diffie-hellman-group-exchange-sha1
|       diffie-hellman-group14-sha256
|       diffie-hellman-group14-sha1
|       diffie-hellman-group1-sha1
|   server_host_key_algorithms: (5)
|       ssh-rsa
|       rsa-sha2-512
|       rsa-sha2-256
|       ecdsa-sha2-nistp256
|       ssh-ed25519
|   encryption_algorithms: (12)
|       chacha20-poly1305@openssh.com
|       aes128-ctr
|       aes192-ctr
|       aes256-ctr
|       aes128-gcm@openssh.com
|       aes256-gcm@openssh.com
|       aes128-cbc
|       aes192-cbc
|       aes256-cbc
|       blowfish-cbc
|       cast128-cbc
|       3des-cbc
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
| ssh-hostkey: 
|   2048 22:75:d7:a7:4f:81:a7:af:52:66:e5:27:44:b1:01:5b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDFgr+LYQ5zL9JWnZmjxP7FT1134sJla89HBT+qnqNvJQRHwO7IqPSa5tEWGZYtzQ2BehsEqb/PisrRHlTeatK0X8qrS3tuz+l1nOj3X/wdcgnFXBrhwpRB2spULt2YqRM49aEbm7bRf2pctxuvgeym/pwCghb6nSbdsaCIsoE+X7QwbG0j6ZfoNIJzQkTQY7O+n1tPP8mlwPOShZJP7+NWVf/kiHsgZqVx6xroCp/NYbQTvLWt6VF/V+iZ3tiT7E1JJxJqQ05wiqsnjnFaZPYP+ptTqorUKP4AenZnf9Wan7VrrzVNZGnFlczj/BsxXOYaRe4Q8VK4PwiDbcwliOBd
|   256 2d:63:28:fc:a2:99:c7:d4:35:b9:45:9a:4b:38:f9:c8 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAsf1XXvL55L6U7NrCo3XSBTr+zCnnQ+GorAMgUugr3ihPkA+4Tw2LmpBr1syz7Z6PkNyQw6NzC3KwSUy1BOGw8=
|   256 73:cd:a0:5b:84:10:7d:a7:1c:7c:61:1d:f5:54:cf:c4 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILMrhnJBfdb0fWQsWVfynAxcQ8+SNlL38vl8VJaaqPTL
| ssh-auth-methods: 
|   Supported authentication methods: 
|     publickey
|     gssapi-keyex
|     gssapi-with-mic
|_    password

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Sep 28 00:00:42 2022 -- 1 IP address (1 host up) scanned in 27.35 seconds

```
