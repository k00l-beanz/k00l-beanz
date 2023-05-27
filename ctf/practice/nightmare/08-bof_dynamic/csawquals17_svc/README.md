# svc

Start with some basic file enumeration:

```s
$ file svc             
svc: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8585d22b995d2e1ab76bd520f7826370df71e0b6, stripped
$ pwn checksec svc        
[*] 'svc'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Looks like there are stack canaries so overflows will be interesting. The NX bit is also enabled so if we want code execution, we'll have to perform a ret2libc.

This application is also stripped, so we'll need to find the entry point. Looking in GDB:

```s
$ gdb -q svc
GEF for linux ready, type `gef' to start, `gef config' to configure
90 commands loaded and 5 functions added for GDB 13.1 in 0.00ms using Python engine 3.11
Reading symbols from svc...
(No debugging symbols found in svc)
gef➤  info file
Symbols from "csawquals17_svc/svc".
Local exec file:
        `csawquals17_svc/svc', file type elf64-x86-64.
        Entry point: 0x4009a0
...<snip>...

gef➤  x/15i $rip
=> 0x4009a0:    xor    ebp,ebp
   0x4009a2:    mov    r9,rdx
   0x4009a5:    pop    rsi
   0x4009a6:    mov    rdx,rsp
   0x4009a9:    and    rsp,0xfffffffffffffff0
   0x4009ad:    push   rax
   0x4009ae:    push   rsp
   0x4009af:    mov    r8,0x400eb0
   0x4009b6:    mov    rcx,0x400e40
   0x4009bd:    mov    rdi,0x400a96
   0x4009c4:    call   0x400910 <__libc_start_main@plt>
```

Looks like the main function is at `0x400a96`.

Next, I throw this application into Ghidra. This requires a bit of work sinced symobls are stripped. Below is the main function:

```c

undefined8 main(void)

{
  basic_ostream *pbVar1;
  ssize_t sVar2;
  long in_FS_OFFSET;
  int choice;
  int i;
  undefined4 local_bc;
  char target [168];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  choice = 0;
  i = 1;
  local_bc = 0;
  while (i != 0) {
..<snip>...
    if (choice == 2) {
...<snip>...
      puts(target);
...<snip>...
    else if (choice == 1) {
...<snip>...
      sVar2 = read(0,target,248);
      local_bc = (undefined4)sVar2;
...<snip>...
  }
  if (canary == *(long *)(in_FS_OFFSET + 0x28)) {
    return 0;
  }
    }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}
}

```

I've gone ahead and cleaned up the output to focus on the interesting parts. 

There is a read call which takes 248 bytes from stdin. This writes into a character buffer that was allocated 168 bytes hence, there is an overflow. 

Before we can exploit this vulnerability, we first need a way to defeat the stack canary. We'll need to identify some way of leaking off the stack canary.

If we were to enter `2` in as an option, the application will print off our target. If we are somehow able to append our `target` to the stack canary, the applicaiton will print off the canary. In 64-bit executables stack canareis are 7-bytes long + NULL byte. We'll need to overwrite the NULL byte in order to print off the entire stack canary. 

Let's find the offset to the stack canary. Taking a look at Ghidra

```
**************************************************************
*                          FUNCTION                          *
**************************************************************
undefined8 __stdcall main(void)
undefined8        RAX:8          <RETURN>
undefined8        Stack[-0x10]:8 canary                                  XREF[2]:     00400aaa(W), 
                                                                    00400dca(R)  
undefined1[168]   Stack[-0xb8]   target                                  XREF[2]:     00400cba(*), 
                                                                    00400d6a(*)  
undefined4        Stack[-0xbc]:4 local_bc                                XREF[2]:     00400b00(W), 
                                                                    00400cd3(W)  
undefined4        Stack[-0xc0]:4 i                                       XREF[3]:     00400af6(W), 
                                                                    00400b0a(R), 
                                                                    00400d7b(W)  
undefined4        Stack[-0xc4]:4 choice                                  XREF[3]:     00400aec(W), 
                                                                    00400bea(*), 
                                                                    00400bfe(R)  
main                                            XREF[4]:     libc_main:004009bd(*), 
                                                            libc_main:004009bd(*), 00401008, 
                                                            004010a8(*)  
00400a96 55              PUSH       RBP
```

Looks like our `target` buffer is 0xa8 (0xb8 - 0x10) bytes away from the stack canary. Let's verify:

```s
gef➤  x/gx $rbp-0x8
0x7fffffffdb38: 0x6161616161616176
gef➤  pattern offset $rbp-0x8
[+] Searching for '$rbp-0x8'
[+] Found at offset 168 (little-endian search) likely
[+] Found at offset 161 (big-endian search) 
gef➤  
```

