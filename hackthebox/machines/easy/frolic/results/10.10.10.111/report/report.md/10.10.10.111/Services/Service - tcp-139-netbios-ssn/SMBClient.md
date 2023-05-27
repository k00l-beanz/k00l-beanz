```bash
smbclient -L //10.10.10.111 -N -I 10.10.10.111 2>&1
```

[/home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp139/smbclient.txt](file:///home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/HacktheBox/machines/easy/frolic/results/10.10.10.111/scans/tcp139/smbclient.txt):

```

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	IPC$            IPC       IPC Service (frolic server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------
	WORKGROUP            FROLIC


```
