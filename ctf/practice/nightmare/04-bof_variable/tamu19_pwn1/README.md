# pwn1

Some basic file enumeration
```s
$ file pwn1
pwn1: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d126d8e3812dd7aa1accb16feac888c99841f504, not stripped
$ pwn checksec --file pwn1        
[*] 'pwn1'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

Inserting `pwn1` into Ghidra and viewing `main`

```c

/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 main(undefined param_1)

{
  int iVar1;
  char user_input [43];
  int target;
  undefined4 local_14;
  undefined1 *local_10;
  
  local_10 = &param_1;
  setvbuf(stdout,(char *)0x2,0,0);
  local_14 = 2;
  target = 0;
  puts(
      "Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other  side he see."
      );
  puts("What... is your name?");
  fgets(user_input,43,stdin);
  iVar1 = strcmp(user_input,"Sir Lancelot of Camelot\n");
  if (iVar1 != 0) {
    puts("I don\'t know that! Auuuuuuuugh!");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("What... is your quest?");
  fgets(user_input,43,stdin);
  iVar1 = strcmp(user_input,"To seek the Holy Grail.\n");
  if (iVar1 != 0) {
    puts("I don\'t know that! Auuuuuuuugh!");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("What... is my secret?");
  gets(user_input);
  if (target == -0x215eef38) {
    print_flag();
  }
  else {
    puts("I don\'t know that! Auuuuuuuugh!");
  }
  return 0;
}


```

You can see that the first two checks are statically checked against `user_input`. The first input should be `Sir Lancelot of Camelot`. The second input should be `To seek the Holy Grail.`.

Lastly, after `What... is my secret?` there is a vulnerable `gets`. Since the goal is to just call `print_flag` we don't need to perform any ret2whatever. You just need `target` to equal `0xdea110c8`.

Looking at how the stack is initialized in Ghidra

```
**************************************************************
*                          FUNCTION                          *
**************************************************************
undefined4 __cdecl main(undefined1 param_1)
undefined4        EAX:4          <RETURN>
undefined1        Stack[0x4]:1   param_1                        
undefined4        Stack[0x0]:4   local_res0                    
undefined1        Stack[-0x10]:1 local_10                      
undefined4        Stack[-0x14]:4 local_14                      
undefined4        Stack[-0x18]:4 target                        
undefined1[43]    Stack[-0x43]   user_input         
```

`target` and `user_input` have a difference of 43 bytes. You can verify this in GDB by setting a breakpoint at `0x565558b2` at by sending a pattern payload.

```
gef➤  pattern offset $ebp-0x10
[+] Searching for '$ebp-0x10'
[+] Found at offset 43 (little-endian search) likely
[+] Found at offset 42 (big-endian search)
```

The final exploit script is in `exploit.py`.