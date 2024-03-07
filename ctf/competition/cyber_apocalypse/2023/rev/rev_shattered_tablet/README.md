# rev_shattered_tablet

Start with some file enumeration:

```s
$ file tablet
tablet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=efa8165e123acf37caf4e4b73aba0b826efae1f1, for GNU/Linux 3.2.0, not stripped
$ pwn checksec --file tablet       
[*] 'tablet'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```