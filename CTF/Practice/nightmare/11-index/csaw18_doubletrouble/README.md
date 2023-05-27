# doubletrouble

## Enumeration

Start with some basic file enumeration

```s
$ file doubletrouble 
doubletrouble: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b9a11827e910481da3ed76a1425d4c110fd0db97, not stripped
$ pwn checksec doubletrouble 
[*] 'doubletrouble'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```