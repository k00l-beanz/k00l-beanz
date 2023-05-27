# shell

Start with some basic file enumeration

```s
$ file shell   
shell: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c8ab24eb713f3b6c9036da743112176b91e58f1b, for GNU/Linux 3.2.0, not stripped
$ pwn checksec --file shell   
[*] 'shell'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```