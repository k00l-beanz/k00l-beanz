# feedme

## Enumeration

```s
$ file feedme
feedme: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, for GNU/Linux 2.6.24, stripped
$ pwn checksec --file feedme
[*] 'feedme'
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
$ strings feedme | less
<Requires further digging>
```

To note:
- The ELF app is stripped so navigating will be "blind"
- NX bit is enabled so if you want any code execution, you'll have to ret2libc
- The app is statically linked so there are plenty of libc methods and rop-gadgets to work with

## Finding the Entry Point

Using GDB gives the entry point:

```s
$ gdb -q feedme   
iGEF for linux ready, type gef to start, gef config to configure
90 commands loaded and 5 functions added for GDB 13.1 in 0.00ms using Python engine 3.11
Reading symbols from feedme...
(No debugging symbols found in feedme)
gef➤  info file
Symbols from "feedme".
Local exec file:
        feedme, file type elf32-i386.
        Entry point: 0x8048d0a
gef➤  x/15i 0x8048d0a
   0x8048d0a:   xor    ebp,ebp
   0x8048d0c:   pop    esi
   0x8048d0d:   mov    ecx,esp
   0x8048d0f:   and    esp,0xfffffff0
   0x8048d12:   push   eax
   0x8048d13:   push   esp
   0x8048d14:   push   edx
   0x8048d15:   push   0x8049970
   0x8048d1a:   push   0x80498d0
   0x8048d1f:   push   ecx
   0x8048d20:   push   esi
   0x8048d21:   push   0x804917a <------ Probably main
   0x8048d26:   call   0x80491f0
   0x8048d2b:   hlt
   0x8048d2c:   xchg   ax,ax
gef➤  x/15i 0x804917a
   0x804917a:   push   ebp
   0x804917b:   mov    ebp,esp
   0x804917d:   and    esp,0xfffffff0
   0x8049180:   sub    esp,0x10
   0x8049183:   mov    DWORD PTR [esp+0x4],0x8048e24
   0x804918b:   mov    DWORD PTR [esp],0xe
   0x8049192:   call   0x804e010
   0x8049197:   mov    DWORD PTR [esp],0x96
   0x804919e:   call   0x806cc50
   0x80491a3:   mov    eax,ds:0x80ea4c0
   0x80491a8:   mov    DWORD PTR [esp+0xc],0x0
   0x80491b0:   mov    DWORD PTR [esp+0x8],0x2
   0x80491b8:   mov    DWORD PTR [esp+0x4],0x0
   0x80491c0:   mov    DWORD PTR [esp],eax
   0x80491c3:   call   0x804fde0
```