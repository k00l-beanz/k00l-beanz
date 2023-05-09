# hunting

Start with some basic file enumration:

```s
$ file hunting 
hunting: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=801f10407444c1390cae5755d9e952f3feadf3eb, for GNU/Linux 3.2.0, stripped
$ pwn checksec hunting      
[*] 'hunting'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```