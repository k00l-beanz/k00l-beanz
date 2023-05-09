# leet_test

## Enumeration

Lets start with some basic file enumeration:

```s
$ file leet_test  
leet_test: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=c6e69bc8fc90c94520adb2fc11a0d7d7b85326f6, for GNU/Linux 3.2.0, not stripped
$ pwn checksec leet_test  
[*] 'leet_test'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Looks like the NX bit is enabled so we won't be able to inject shellcode. This application is not stripped so lets look at the `main` function in Ghidra:

```c

```

- Address of rand value: `rbp-0x134` | `0x7fffffffdb1c`
- Address of start of buffer: `rbp-0x120` | `0x7fffffffdb30`