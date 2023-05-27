```bash
nmap -vv --reason -Pn -T4 -sU -sV -p 137 --script="banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/udp_137_smb_nmap.txt" -oX "/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/xml/udp_137_smb_nmap.xml" 10.10.10.111
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/udp_137_smb_nmap.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/udp_137_smb_nmap.txt):

```
# Nmap 7.92 scan initiated Wed Nov 16 16:47:08 2022 as: nmap -vv --reason -Pn -T4 -sU -sV -p 137 "--script=banner,(nbstat or smb* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/udp_137_smb_nmap.txt -oX /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/udp137/xml/udp_137_smb_nmap.xml 10.10.10.111
Nmap scan report for 10.10.10.111
Host is up, received user-set (0.014s latency).
Scanned at 2022-11-16 16:47:08 EST for 0s

PORT    STATE SERVICE    REASON              VERSION
137/udp open  netbios-ns udp-response ttl 63 Samba nmbd netbios-ns (workgroup: WORKGROUP)
Service Info: Host: FROLIC

Host script results:
| nbstat: NetBIOS name: FROLIC, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   FROLIC<00>           Flags: <unique><active>
|   FROLIC<03>           Flags: <unique><active>
|   FROLIC<20>           Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   WORKGROUP<00>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
| Statistics:
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Nov 16 16:47:08 2022 -- 1 IP address (1 host up) scanned in 0.70 seconds

```
