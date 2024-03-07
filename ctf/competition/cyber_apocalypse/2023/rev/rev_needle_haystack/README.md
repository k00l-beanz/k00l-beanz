# haystack

To start, some basic file enumeration:

```s
$ file haystack 
haystack: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=4c6530f229889e6e1a1fe1e2f57add742ef51fd8, for GNU/Linux 3.2.0, not stripped
$ pwn checksec --file haystack
[*] 'haystack'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```