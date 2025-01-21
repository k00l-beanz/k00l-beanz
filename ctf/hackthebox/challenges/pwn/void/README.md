# Void

Start with some application enumeration

```s
$ file void
void: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=a5a29f47fbeeeff863522acff838636b57d1c213, for GNU/Linux 3.2.0, not stripped
$ $ pwn checksec void             
[*] 'void'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
    RUNPATH:  b'./glibc/'
```

Looks like NX is enabled and we have partial RELRO. Tossing the application into Ghidra and viewing main:

```c
undefined8 main(void)
{
  vuln();
  return 0;
}
```

Nothing interesting but lets take a look at `vuln`.

```c
void vuln(void)
{
  undefined local_48 [64];
  
  read(0,local_48,200);
  return;
}
```