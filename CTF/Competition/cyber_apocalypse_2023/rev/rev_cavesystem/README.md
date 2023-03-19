# cave

Some basic file enumeration

```s
$ file cave   
cave: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=002696e9d5c508adc7b7376ceb2e012db8feb908, for GNU/Linux 3.2.0, not stripped
$ pwn checksec --file cave   
[*] 'cave'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```