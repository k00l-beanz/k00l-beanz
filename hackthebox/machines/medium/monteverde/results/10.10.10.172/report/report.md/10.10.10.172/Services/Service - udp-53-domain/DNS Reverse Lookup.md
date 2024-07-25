```bash
dig -p 53 -x 10.10.10.172 @10.10.10.172
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/udp53/udp_53_dns_reverse-lookup.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/udp53/udp_53_dns_reverse-lookup.txt):

```
;; communications error to 10.10.10.172#53: timed out

; <<>> DiG 9.18.6-2-Debian <<>> -p 53 -x 10.10.10.172 @10.10.10.172
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 51642
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;172.10.10.10.in-addr.arpa.	IN	PTR

;; Query time: 4469 msec
;; SERVER: 10.10.10.172#53(10.10.10.172) (UDP)
;; WHEN: Tue Sep 20 19:24:56 EDT 2022
;; MSG SIZE  rcvd: 54



```
