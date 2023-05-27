# greeting

Start with some basic file enumeration:

```s
$ file greeting 
greeting: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=beb85611dbf6f1f3a943cecd99726e5e35065a63, not stripped
$ pwn checksec greeting             
[*] 'greeting'
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

Looks like there is a canary. If we want to perform an overflow, we'll have to leak this value off and use it in our final payload. The NX bit is also enabled meaning we'll have to perform a ret2libc to get code execution. 

Lets look at the `main` function:

```c

void main(void)

{
  int iVar1;
  int in_GS_OFFSET;
  char format_str_target [64];
  char user_input [64];
  int canary;
  
  canary = *(int *)(in_GS_OFFSET + 0x14);
  printf("Please tell me your name... ");
  iVar1 = getnline(user_input,64);
  if (iVar1 == 0) {
    puts("Don\'t ignore me ;( ");
  }
  else {
    sprintf(format_str_target,"Nice to meet you, %s :)\n",user_input);
    printf(format_str_target);
  }
  if (canary != *(int *)(in_GS_OFFSET + 0x14)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}


```

Looks like we have a format string vulnerability. We'll need to find an appropriate offset and initiate a write:

```s
$ ./leak.py    
1 : AABBBBCCCCDDDDEEEE80487d0
2 : AABBBBCCCCDDDDEEEEffffcd0c
3 : AABBBBCCCCDDDDEEEEe9f7f213
4 : AABBBBCCCCDDDDEEEEf7ffcff4
5 : AABBBBCCCCDDDDEEEE2c
6 : AABBBBCCCCDDDDEEEE0
7 : AABBBBCCCCDDDDEEEE6563694e
8 : AABBBBCCCCDDDDEEEE206f7420
9 : AABBBBCCCCDDDDEEEE7465656d
10 : AABBBBCCCCDDDDEEEE756f7920
11 : AABBBBCCCCDDDDEEEE4141202c
12 : AABBBBCCCCDDDDEEEE42424242
13 : AABBBBCCCCDDDDEEEE43434343
14 : AABBBBCCCCDDDDEEEE44444444
15 : AABBBBCCCCDDDDEEEE45454545
16 : AABBBBCCCCDDDDEEEE24363125
17 : AABBBBCCCCDDDDEEEE293a2078
18 : AABBBBCCCCDDDDEEEEf7ff000a
19 : AABBBBCCCCDDDDEEEE0
20 : AABBBBCCCCDDDDEEEE0
21 : AABBBBCCCCDDDDEEEE0
22 : AABBBBCCCCDDDDEEEE0
23 : AABBBBCCCCDDDDEEEE42424141
24 : AABBBBCCCCDDDDEEEE43434242
25 : AABBBBCCCCDDDDEEEE44444343
26 : AABBBBCCCCDDDDEEEE45454444
27 : AABBBBCCCCDDDDEEEE32254545
28 : AABBBBCCCCDDDDEEEE782438
29 : AABBBBCCCCDDDDEEEEf7fd9800
30 : AABBBBCCCCDDDDEEEEf7c1ca2f
31 : AABBBBCCCCDDDDEEEEf7fc14a0
```

Looks like with a prefix of 2 bytes, we can begin writing at the 12th element. Lets verify:

```s
$ ./greeting
Hello, Im nao!
Please tell me your name... AABBBB%12$p
Nice to meet you, AABBBB0x42424242 :)
```

Looks good. Now we need to decide where and what we're going to write. Looking at `main`, there aren't any libc functions being called after the `printf`. There is actually a section of memory `.fini_array` which is an array of functions that are called when the program exits. These functions are typically used for cleanp operations, such as freeing dynamically allocated memory, closing files, or releasing other resources.

Lets find where this application is located:

```s
gef➤  info file                                                              
Symbols from "greeting".
Native process:                                                            
        Using the running image of child Thread 0xf7fc2540 (LWP 16488).                                                                                        
        While running this, GDB does not access memory from...                                                                                                 
Local exec file:                                                                                                                                               
        greeting, file type elf32-i386.
        Entry point: 0x80484f0                                              
...<snip>...                         
        0x08049934 - 0x08049938 is .fini_array                              
...<snip>...
```

The `.fini_array` begins at `0x08049934`. We can overwrite this address with the address of `getnline` which contains two libc calls. Lets attempt to overwrite and jump here:

TODO