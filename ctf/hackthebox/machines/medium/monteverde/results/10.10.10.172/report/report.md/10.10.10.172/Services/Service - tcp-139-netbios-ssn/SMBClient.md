```bash
smbclient -L //10.10.10.172 -N -I 10.10.10.172 2>&1
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp139/smbclient.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp139/smbclient.txt):

```
do_connect: Connection to 10.10.10.172 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available


```
