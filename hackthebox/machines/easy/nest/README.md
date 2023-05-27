# Nest

## Information Gathering

- SMB Users
    - `TempUser:welcome2019`
    - `c.smith:fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=`

## Enumeration

Of course, start with a basic nmap scan:
```s
# Nmap 7.93 scan initiated Mon May  8 21:04:51 2023 as: nmap -p- -A -oN nmap/all.nmap -Pn 10.10.10.178
Nmap scan report for 10.10.10.178
Host is up (0.050s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
445/tcp  open  microsoft-ds?
4386/tcp open  unknown
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|     Reporting Service V1.2
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, RTSPRequest, SIPOptions: 
|     Reporting Service V1.2
|     Unrecognised command
|   Help: 
|     Reporting Service V1.2
|     This service allows users to run queries against databases using the legacy HQK format
|     AVAILABLE COMMANDS ---
|     LIST
|     SETDIR <Directory_Name>
|     RUNQUERY <Query_ID>
|     DEBUG <Password>
|_    HELP <Command>
```

### tcp/445

- Running `smbclient` and `smbmap` with `anonymous` access

```s
$ smbclient -L \\\\10.10.10.178\\ -N                 

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        Data            Disk      
        IPC$            IPC       Remote IPC
        Secure$         Disk      
        Users           Disk      
SMB1 disabled -- no workgroup available

$ smbmap -u '' -p '' -H 10.10.10.178                   
[+] IP: 10.10.10.178:445        Name: 10.10.10.178     

$ smbmap -u "Anonymous" -p '' -H 10.10.10.178          
[+] Guest session       IP: 10.10.10.178:445    Name: 10.10.10.178                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        Data                                                    READ ONLY
        IPC$                                                    NO ACCESS       Remote IPC
        Secure$                                                 NO ACCESS
        Users                                                   READ ONLY
``` 

- Lets attempt to download `Data` and `Users`

```s
$ smbclient \\\\10.10.10.178\\Users -U "Anonymous"
Password for [WORKGROUP\Anonymous]:
Try "help" to get a list of possible commands.
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
NT_STATUS_ACCESS_DENIED listing \Administrator\*
NT_STATUS_ACCESS_DENIED listing \C.Smith\*
NT_STATUS_ACCESS_DENIED listing \L.Frost\*
NT_STATUS_ACCESS_DENIED listing \R.Thompson\*
NT_STATUS_ACCESS_DENIED listing \TempUser\*

$ smbclient \\\\10.10.10.178\\Data -U "Anonymous"
Password for [WORKGROUP\Anonymous]:
Try "help" to get a list of possible commands.
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
NT_STATUS_ACCESS_DENIED listing \IT\*
NT_STATUS_ACCESS_DENIED listing \Production\*
NT_STATUS_ACCESS_DENIED listing \Reports\*
getting file \Shared\Maintenance\Maintenance Alerts.txt of size 48 as Shared/Maintenance/Maintenance Alerts.txt (0.9 KiloBytes/sec) (average 0.9 KiloBytes/sec)
getting file \Shared\Templates\HR\Welcome Email.txt of size 425 as Shared/Templates/HR/Welcome Email.txt (7.7 KiloBytes/sec) (average 4.3 KiloBytes/sec)
```

`Welcome Email.txt` has some useful information. 

```
We would like to extend a warm welcome to our newest member of staff, <FIRSTNAME> <SURNAME>

You will find your home folder in the following location: 
\\HTB-NEST\Users\<USERNAME>

If you have any issues accessing specific services or workstations, please inform the 
IT department and use the credentials below until all systems have been set up for you.

Username: TempUser
Password: welcome2019


Thank you
HR
```

- We can re-enumerate everything with our new credentials

```s
$ smbmap -u "TempUser" -p "welcome2019" -H 10.10.10.178
[+] IP: 10.10.10.178:445        Name: 10.10.10.178                                      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        Data                                                    READ ONLY
        IPC$                                                    NO ACCESS       Remote IPC
        Secure$                                                 READ ONLY
        Users                                                   READ ONLY

$ smbclient -L \\\\10.10.10.178\\ -U "TempUser"        
Password for [WORKGROUP\TempUser]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        Data            Disk      
        IPC$            IPC       Remote IPC
        Secure$         Disk      
        Users           Disk
```

- Looks like we have read access to `Secure$` now.
- We also re-enumerate everything in the `Data` share

```s
$ smbclient \\\\10.10.10.178\\Data -U "TempUser"
Password for [WORKGROUP\TempUser]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Wed Aug  7 18:53:46 2019
  ..                                  D        0  Wed Aug  7 18:53:46 2019
  IT                                  D        0  Wed Aug  7 18:58:07 2019
  Production                          D        0  Mon Aug  5 17:53:38 2019
  Reports                             D        0  Mon Aug  5 17:53:44 2019
  Shared                              D        0  Wed Aug  7 15:07:51 2019

                5242623 blocks of size 4096. 1847587 blocks available
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
getting file \Shared\Maintenance\Maintenance Alerts.txt of size 48 as Shared/Maintenance/Maintenance Alerts.txt (0.9 KiloBytes/sec) (average 0.9 KiloBytes/sec)
getting file \IT\Configs\Adobe\editing.xml of size 246 as IT/Configs/Adobe/editing.xml (4.4 KiloBytes/sec) (average 2.7 KiloBytes/sec)
getting file \IT\Configs\Adobe\Options.txt of size 0 as IT/Configs/Adobe/Options.txt (0.0 KiloBytes/sec) (average 2.0 KiloBytes/sec)
getting file \IT\Configs\Adobe\projects.xml of size 258 as IT/Configs/Adobe/projects.xml (4.3 KiloBytes/sec) (average 2.7 KiloBytes/sec)
getting file \IT\Configs\Adobe\settings.xml of size 1274 as IT/Configs/Adobe/settings.xml (21.5 KiloBytes/sec) (average 6.8 KiloBytes/sec)
getting file \IT\Configs\Atlas\Temp.XML of size 1369 as IT/Configs/Atlas/Temp.XML (25.2 KiloBytes/sec) (average 9.9 KiloBytes/sec)
getting file \IT\Configs\Microsoft\Options.xml of size 4598 as IT/Configs/Microsoft/Options.xml (69.1 KiloBytes/sec) (average 20.1 KiloBytes/sec)
getting file \IT\Configs\NotepadPlusPlus\config.xml of size 6451 as IT/Configs/NotepadPlusPlus/config.xml (114.5 KiloBytes/sec) (average 32.1 KiloBytes/sec)
getting file \IT\Configs\NotepadPlusPlus\shortcuts.xml of size 2108 as IT/Configs/NotepadPlusPlus/shortcuts.xml (38.1 KiloBytes/sec) (average 32.7 KiloBytes/sec)
getting file \IT\Configs\RU Scanner\RU_config.xml of size 270 as IT/Configs/RU Scanner/RU_config.xml (5.1 KiloBytes/sec) (average 30.1 KiloBytes/sec)
getting file \Shared\Templates\HR\Welcome Email.txt of size 425 as Shared/Templates/HR/Welcome Email.txt (8.0 KiloBytes/sec) (average 28.1 KiloBytes/sec)
```

In `RU_config.xml`:

```xml
<?xml version="1.0"?>
<ConfigFile xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <Port>389</Port>
  <Username>c.smith</Username>
  <Password>fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=</Password>
</ConfigFile>
```

Attempting to base64 decode this reveals that it's encrypted.

```s
$ echo -n "fTEzAfYDoz1YzkqhQkH6GQFYKp1XY5hm7bjOP86yYxE=" | base64 -d | xxd
00000000: 7d31 3301 f603 a33d 58ce 4aa1 4241 fa19  }13....=X.J.BA..
00000010: 0158 2a9d 5763 9866 edb8 ce3f ceb2 6311  .X*.Wc.f...?..c.
```

### tcp/4386

## Foothold

## Privilege Escalation