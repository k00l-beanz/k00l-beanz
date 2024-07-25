```bash
enum4linux -a -M -l -d 10.10.10.172 2>&1
```

[/home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp139/enum4linux.txt](file:///home/Default/Documents/Repos/Default_/Platforms/HacktheBox/machines/medium/monteverde/results/10.10.10.172/scans/tcp139/enum4linux.txt):

```
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Tue Sep 20 18:59:04 2022

[34m =========================================( [0m[32mTarget Information[0m[34m )=========================================

[0mTarget ........... 10.10.10.172
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


[34m ============================( [0m[32mEnumerating Workgroup/Domain on 10.10.10.172[0m[34m )============================

[0m[33m
[E] [0m[31mCan't find workgroup/domain

[0m

[34m ================================( [0m[32mNbtstat Information for 10.10.10.172[0m[34m )================================

[0mLooking up status of 10.10.10.172
No reply from 10.10.10.172

[34m ===================================( [0m[32mSession Check on 10.10.10.172[0m[34m )===================================

[0m[33m
[+] [0m[32mServer 10.10.10.172 allows sessions using username '', password ''

[0m
[34m ===========================( [0m[32mGetting information via LDAP for 10.10.10.172[0m[34m )===========================

[0m[33m
[+] [0m[32m10.10.10.172 appears to be a child DC

[0m
[34m ================================( [0m[32mGetting domain SID for 10.10.10.172[0m[34m )================================

[0mDomain Name: MEGABANK
Domain Sid: S-1-5-21-391775091-850290835-3566037492
[33m
[+] [0m[32mHost is part of a domain (not a workgroup)

[0m
[34m ===================================( [0m[32mOS information on 10.10.10.172[0m[34m )===================================

[0m[33m
[E] [0m[31mCan't get OS info with smbclient

[0m[33m
[+] [0m[32mGot OS info for 10.10.10.172 from srvinfo:
[0mdo_cmd: Could not initialise srvsvc. Error was NT_STATUS_ACCESS_DENIED


[34m =======================================( [0m[32mUsers on 10.10.10.172[0m[34m )=======================================

[0mindex: 0xfb6 RID: 0x450 acb: 0x00000210 Account: AAD_987d7f2f57d2	Name: AAD_987d7f2f57d2	Desc: Service account for the Synchronization Service with installation identifier 05c97990-7587-4a3d-b312-309adfc172d9 running on computer MONTEVERDE.
index: 0xfd0 RID: 0xa35 acb: 0x00000210 Account: dgalanos	Name: Dimitris Galanos	Desc: (null)
index: 0xedb RID: 0x1f5 acb: 0x00000215 Account: Guest	Name: (null)	Desc: Built-in account for guest access to the computer/domain
index: 0xfc3 RID: 0x641 acb: 0x00000210 Account: mhope	Name: Mike Hope	Desc: (null)
index: 0xfd1 RID: 0xa36 acb: 0x00000210 Account: roleary	Name: Ray O'Leary	Desc: (null)
index: 0xfc5 RID: 0xa2a acb: 0x00000210 Account: SABatchJobs	Name: SABatchJobs	Desc: (null)
index: 0xfd2 RID: 0xa37 acb: 0x00000210 Account: smorgan	Name: Sally Morgan	Desc: (null)
index: 0xfc6 RID: 0xa2b acb: 0x00000210 Account: svc-ata	Name: svc-ata	Desc: (null)
index: 0xfc7 RID: 0xa2c acb: 0x00000210 Account: svc-bexec	Name: svc-bexec	Desc: (null)
index: 0xfc8 RID: 0xa2d acb: 0x00000210 Account: svc-netapp	Name: svc-netapp	Desc: (null)

user:[Guest] rid:[0x1f5]
user:[AAD_987d7f2f57d2] rid:[0x450]
user:[mhope] rid:[0x641]
user:[SABatchJobs] rid:[0xa2a]
user:[svc-ata] rid:[0xa2b]
user:[svc-bexec] rid:[0xa2c]
user:[svc-netapp] rid:[0xa2d]
user:[dgalanos] rid:[0xa35]
user:[roleary] rid:[0xa36]
user:[smorgan] rid:[0xa37]
	User Name   :	roleary
	Full Name   :	Ray O'Leary
	Home Drive  :	\\monteverde\users$\roleary
	Dir Drive   :	H:
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 08:08:06 EST
	Password can change Time :	Sat, 04 Jan 2020 08:08:06 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa36
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	smorgan
	Full Name   :	Sally Morgan
	Home Drive  :	\\monteverde\users$\smorgan
	Dir Drive   :	H:
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 08:09:22 EST
	Password can change Time :	Sat, 04 Jan 2020 08:09:22 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa37
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	AAD_987d7f2f57d2
	Full Name   :	AAD_987d7f2f57d2
	Home Drive  :
	Dir Drive   :
	Profile Path:
	Logon Script:
	Description :	Service account for the Synchronization Service with installation identifier 05c97990-7587-4a3d-b312-309adfc172d9 running on computer MONTEVERDE.
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Tue, 20 Sep 2022 18:52:30 EDT
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 31 Dec 1969 19:00:00 EST
	Password last set Time   :	Thu, 02 Jan 2020 17:53:25 EST
	Password can change Time :	Fri, 03 Jan 2020 17:53:25 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0x450
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x0000000a
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	dgalanos
	Full Name   :	Dimitris Galanos
	Home Drive  :	\\monteverde\users$\dgalanos
	Dir Drive   :	H:
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 08:06:11 EST
	Password can change Time :	Sat, 04 Jan 2020 08:06:11 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa35
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	svc-netapp
	Full Name   :	svc-netapp
	Home Drive  :
	Dir Drive   :
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 08:01:43 EST
	Password can change Time :	Sat, 04 Jan 2020 08:01:43 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa2d
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	SABatchJobs
	Full Name   :	SABatchJobs
	Home Drive  :
	Dir Drive   :
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Mon, 06 Jan 2020 05:27:19 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 07:48:46 EST
	Password can change Time :	Sat, 04 Jan 2020 07:48:46 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa2a
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	svc-ata
	Full Name   :	svc-ata
	Home Drive  :
	Dir Drive   :
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 07:58:31 EST
	Password can change Time :	Sat, 04 Jan 2020 07:58:31 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa2b
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	mhope
	Full Name   :	Mike Hope
	Home Drive  :	\\monteverde\users$\mhope
	Dir Drive   :	H:
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Fri, 03 Jan 2020 08:29:59 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Thu, 02 Jan 2020 18:40:06 EST
	Password can change Time :	Fri, 03 Jan 2020 18:40:06 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0x641
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000002
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	svc-bexec
	Full Name   :	svc-bexec
	Home Drive  :
	Dir Drive   :
	Profile Path:
	Logon Script:
	Description :
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Fri, 03 Jan 2020 07:59:56 EST
	Password can change Time :	Sat, 04 Jan 2020 07:59:56 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0xa2c
	group_rid:	0x201
	acb_info :	0x00000210
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : False
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False

	User Name   :	Guest
	Full Name   :
	Home Drive  :
	Dir Drive   :
	Profile Path:
	Logon Script:
	Description :	Built-in account for guest access to the computer/domain
	Workstations:
	Comment     :
	Remote Dial :
	Logon Time               :	Wed, 31 Dec 1969 19:00:00 EST
	Logoff Time              :	Wed, 31 Dec 1969 19:00:00 EST
	Kickoff Time             :	Wed, 13 Sep 30828 22:48:05 EDT
	Password last set Time   :	Wed, 31 Dec 1969 19:00:00 EST
	Password can change Time :	Wed, 31 Dec 1969 19:00:00 EST
	Password must change Time:	Wed, 13 Sep 30828 22:48:05 EDT
	unknown_2[0..31]...
	user_rid :	0x1f5
	group_rid:	0x202
	acb_info :	0x00000215
	fields_present:	0x00ffffff
	logon_divs:	168
	bad_password_count:	0x00000000
	logon_count:	0x00000000
	padding1[0..7]...
	logon_hrs[0..21]...
	Account Disabled         : True
	Password does not expire : True
	Account locked out       : False
	Password expired         : False
	Interdomain trust account: False
	Workstation trust account: False
	Server trust account     : False
	Trusted for delegation   : False


[34m ================================( [0m[32mMachine Enumeration on 10.10.10.172[0m[34m )================================

[0m[33m
[E] [0m[31mNot implemented in this version of enum4linux.

[0m
[34m =================================( [0m[32mShare Enumeration on 10.10.10.172[0m[34m )=================================

[0mdo_connect: Connection to 10.10.10.172 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

	Sharename       Type      Comment
	---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available
[33m
[+] [0m[32mAttempting to map shares on 10.10.10.172

[0m
[34m ============================( [0m[32mPassword Policy Information for 10.10.10.172[0m[34m )============================

[0m

[+] Attaching to 10.10.10.172 using a NULL share

[+] Trying protocol 139/SMB...

	[!] Protocol failed: Cannot request session (Called Name:10.10.10.172)

[+] Trying protocol 445/SMB...

[+] Found domain(s):

	[+] MEGABANK
	[+] Builtin

[+] Password Info for Domain: MEGABANK

	[+] Minimum password length: 7
	[+] Password history length: 24
	[+] Maximum password age: 41 days 23 hours 53 minutes
	[+] Password Complexity Flags: 000000

		[+] Domain Refuse Password Change: 0
		[+] Domain Password Store Cleartext: 0
		[+] Domain Password Lockout Admins: 0
		[+] Domain Password No Clear Change: 0
		[+] Domain Password No Anon Change: 0
		[+] Domain Password Complex: 0

	[+] Minimum password age: 1 day 4 minutes
	[+] Reset Account Lockout Counter: 30 minutes
	[+] Locked Account Duration: 30 minutes
	[+] Account Lockout Threshold: None
	[+] Forced Log off Time: Not Set


[33m
[+] [0m[32mRetieved partial password policy with rpcclient:


[0mPassword Complexity: Disabled
Minimum Password Length: 7


[34m =======================================( [0m[32mGroups on 10.10.10.172[0m[34m )=======================================

[0m[33m
[+] [0m[32mGetting builtin groups:

[0mgroup:[Pre-Windows 2000 Compatible Access] rid:[0x22a]
group:[Incoming Forest Trust Builders] rid:[0x22d]
group:[Windows Authorization Access Group] rid:[0x230]
group:[Terminal Server License Servers] rid:[0x231]
group:[Users] rid:[0x221]
group:[Guests] rid:[0x222]
group:[Remote Desktop Users] rid:[0x22b]
group:[Network Configuration Operators] rid:[0x22c]
group:[Performance Monitor Users] rid:[0x22e]
group:[Performance Log Users] rid:[0x22f]
group:[Distributed COM Users] rid:[0x232]
group:[IIS_IUSRS] rid:[0x238]
group:[Cryptographic Operators] rid:[0x239]
group:[Event Log Readers] rid:[0x23d]
group:[Certificate Service DCOM Access] rid:[0x23e]
group:[RDS Remote Access Servers] rid:[0x23f]
group:[RDS Endpoint Servers] rid:[0x240]
group:[RDS Management Servers] rid:[0x241]
group:[Hyper-V Administrators] rid:[0x242]
group:[Access Control Assistance Operators] rid:[0x243]
group:[Remote Management Users] rid:[0x244]
group:[Storage Replica Administrators] rid:[0x246]
[33m
[+] [0m[32m Getting builtin group memberships:

[0m[35mGroup: [0mUsers' (RID: 545) has member: Couldn't lookup SIDs
[35mGroup: [0mWindows Authorization Access Group' (RID: 560) has member: Couldn't lookup SIDs
[35mGroup: [0mRemote Management Users' (RID: 580) has member: Couldn't lookup SIDs
[35mGroup: [0mIIS_IUSRS' (RID: 568) has member: Couldn't lookup SIDs
[35mGroup: [0mPre-Windows 2000 Compatible Access' (RID: 554) has member: Couldn't lookup SIDs
[35mGroup: [0mGuests' (RID: 546) has member: Couldn't lookup SIDs
[33m
[+] [0m[32mGetting detailed info for group Remote Desktop Users (RID: 555)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Users (RID: 545)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Incoming Forest Trust Builders (RID: 557)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Terminal Server License Servers (RID: 561)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Certificate Service DCOM Access (RID: 574)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Cryptographic Operators (RID: 569)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Network Configuration Operators (RID: 556)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Performance Log Users (RID: 559)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Windows Authorization Access Group (RID: 560)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Performance Monitor Users (RID: 558)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group RDS Management Servers (RID: 577)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Distributed COM Users (RID: 562)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Remote Management Users (RID: 580)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Storage Replica Administrators (RID: 582)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group IIS_IUSRS (RID: 568)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Pre-Windows 2000 Compatible Access (RID: 554)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group RDS Remote Access Servers (RID: 575)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Hyper-V Administrators (RID: 578)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group RDS Endpoint Servers (RID: 576)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Event Log Readers (RID: 573)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Access Control Assistance Operators (RID: 579)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Guests (RID: 546)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32m Getting local groups:

[0mgroup:[Cert Publishers] rid:[0x205]
group:[RAS and IAS Servers] rid:[0x229]
group:[Allowed RODC Password Replication Group] rid:[0x23b]
group:[Denied RODC Password Replication Group] rid:[0x23c]
group:[DnsAdmins] rid:[0x44d]
group:[SQLServer2005SQLBrowserUser$MONTEVERDE] rid:[0x44f]
group:[ADSyncAdmins] rid:[0x451]
group:[ADSyncOperators] rid:[0x452]
group:[ADSyncBrowse] rid:[0x453]
group:[ADSyncPasswordSet] rid:[0x454]
[33m
[+] [0m[32m Getting local group memberships:

[0m[35mGroup: [0mADSyncAdmins' (RID: 1105) has member: Couldn't lookup SIDs
[35mGroup: [0mDenied RODC Password Replication Group' (RID: 572) has member: Couldn't lookup SIDs
[33m
[+] [0m[32mGetting detailed info for group Cert Publishers (RID: 517)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group ADSyncAdmins (RID: 1105)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group ADSyncOperators (RID: 1106)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group RAS and IAS Servers (RID: 553)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group ADSyncBrowse (RID: 1107)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group SQLServer2005SQLBrowserUser$MONTEVERDE (RID: 1103)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Allowed RODC Password Replication Group (RID: 571)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group Denied RODC Password Replication Group (RID: 572)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group ADSyncPasswordSet (RID: 1108)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32mGetting detailed info for group DnsAdmins (RID: 1101)

[0m[33m
[E] [0m[31mNo info found


[0m[33m
[+] [0m[32m Getting domain groups:

[0mgroup:[Enterprise Read-only Domain Controllers] rid:[0x1f2]
group:[Domain Users] rid:[0x201]
group:[Domain Guests] rid:[0x202]
group:[Domain Computers] rid:[0x203]
group:[Group Policy Creator Owners] rid:[0x208]
group:[Cloneable Domain Controllers] rid:[0x20a]
group:[Protected Users] rid:[0x20d]
group:[DnsUpdateProxy] rid:[0x44e]
group:[Azure Admins] rid:[0xa29]
group:[File Server Admins] rid:[0xa2e]
group:[Call Recording Admins] rid:[0xa2f]
group:[Reception] rid:[0xa30]
group:[Operations] rid:[0xa31]
group:[Trading] rid:[0xa32]
group:[HelpDesk] rid:[0xa33]
group:[Developers] rid:[0xa34]
[33m
[+] [0m[32m Getting domain group memberships:

[0m[35mGroup: [0m'Trading' (RID: 2610) has member: MEGABANK\dgalanos
[35mGroup: [0m'Domain Guests' (RID: 514) has member: MEGABANK\Guest
[35mGroup: [0m'HelpDesk' (RID: 2611) has member: MEGABANK\roleary
[35mGroup: [0m'Azure Admins' (RID: 2601) has member: MEGABANK\Administrator
[35mGroup: [0m'Azure Admins' (RID: 2601) has member: MEGABANK\AAD_987d7f2f57d2
[35mGroup: [0m'Azure Admins' (RID: 2601) has member: MEGABANK\mhope
[35mGroup: [0m'Operations' (RID: 2609) has member: MEGABANK\smorgan
[35mGroup: [0m'Group Policy Creator Owners' (RID: 520) has member: MEGABANK\Administrator
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\Administrator
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\krbtgt
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\AAD_987d7f2f57d2
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\mhope
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\SABatchJobs
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\svc-ata
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\svc-bexec
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\svc-netapp
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\dgalanos
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\roleary
[35mGroup: [0m'Domain Users' (RID: 513) has member: MEGABANK\smorgan
[33m
[+] [0m[32mGetting detailed info for group Trading (RID: 2610)

[0m	Group Name:	Trading
	Description:
	Group Attribute:7
	Num Members:1

[33m
[+] [0m[32mGetting detailed info for group Domain Guests (RID: 514)

[0m	Group Name:	Domain Guests
	Description:	All domain guests
	Group Attribute:7
	Num Members:1

[33m
[+] [0m[32mGetting detailed info for group HelpDesk (RID: 2611)

[0m	Group Name:	HelpDesk
	Description:
	Group Attribute:7
	Num Members:1

[33m
[+] [0m[32mGetting detailed info for group Domain Computers (RID: 515)

[0m	Group Name:	Domain Computers
	Description:	All workstations and servers joined to the domain
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Reception (RID: 2608)

[0m	Group Name:	Reception
	Description:
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group File Server Admins (RID: 2606)

[0m	Group Name:	File Server Admins
	Description:
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Cloneable Domain Controllers (RID: 522)

[0m	Group Name:	Cloneable Domain Controllers
	Description:	Members of this group that are domain controllers may be cloned.
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Protected Users (RID: 525)

[0m	Group Name:	Protected Users
	Description:	Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Developers (RID: 2612)

[0m	Group Name:	Developers
	Description:
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Azure Admins (RID: 2601)

[0m	Group Name:	Azure Admins
	Description:
	Group Attribute:7
	Num Members:3

[33m
[+] [0m[32mGetting detailed info for group Call Recording Admins (RID: 2607)

[0m	Group Name:	Call Recording Admins
	Description:
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group DnsUpdateProxy (RID: 1102)

[0m	Group Name:	DnsUpdateProxy
	Description:	DNS clients who are permitted to perform dynamic updates on behalf of some other clients (such as DHCP servers).
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Operations (RID: 2609)

[0m	Group Name:	Operations
	Description:
	Group Attribute:7
	Num Members:1

[33m
[+] [0m[32mGetting detailed info for group Enterprise Read-only Domain Controllers (RID: 498)

[0m	Group Name:	Enterprise Read-only Domain Controllers
	Description:	Members of this group are Read-Only Domain Controllers in the enterprise
	Group Attribute:7
	Num Members:0

[33m
[+] [0m[32mGetting detailed info for group Group Policy Creator Owners (RID: 520)

[0m	Group Name:	Group Policy Creator Owners
	Description:	Members in this group can modify group policy for the domain
	Group Attribute:7
	Num Members:1

[33m
[+] [0m[32mGetting detailed info for group Domain Users (RID: 513)

[0m	Group Name:	Domain Users
	Description:	All domain users
	Group Attribute:7
	Num Members:11


[34m ==================( [0m[32mUsers on 10.10.10.172 via RID cycling (RIDS: 500-550,1000-1050)[0m[34m )==================

[0m[33m
[E] [0m[31mCouldn't get SID: NT_STATUS_ACCESS_DENIED.  RID cycling not possible.

[0m
[34m ===============================( [0m[32mGetting printer info for 10.10.10.172[0m[34m )===============================

[0mdo_cmd: Could not initialise spoolss. Error was NT_STATUS_ACCESS_DENIED


enum4linux complete on Tue Sep 20 19:01:08 2022



```
