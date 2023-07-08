# Arctic

## Information Gathering

## Enumeration

Start with a basic nmap scan:

```s
$ sudo nmap -p- -A -oN nmap/all.nmap -Pn -T4 10.10.10.11    
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-03 22:20 EDT
Nmap scan report for 10.10.10.11
Host is up (0.013s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT      STATE SERVICE VERSION
135/tcp   open  msrpc   Microsoft Windows RPC
8500/tcp  open  fmtp?
49154/tcp open  msrpc   Microsoft Windows RPC
```

### tcp/8500

Navigating to `http://10.10.10.11:8500` reveals an open directory with two directories: CFIDE and cfdocs. cfdocs seems to contain documentation pages so lets take a look at CFIDE.



## Foothold

## Privilege Escalation
