# warmup

Some basic file enumeration

```s
$ file warmup    
warmup: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=ab209f3b8a3c2902e1a2ecd5bb06e258b45605a4, not stripped
$ pwn checksec --file warmup
[*] 'warmup'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Throwing application into Ghidra and exaimining the main function

```c
void main(void)

{
  char easy_func [64];
  char get_var [64];
  
  write(1,"-Warm Up-\n",10);
  write(1,&DAT_0040074c,4);
  sprintf(easy_func,"%p\n",easy);
  write(1,easy_func,9);
  write(1,&DAT_00400755,1);
  gets(get_var);
  return;
}
```

There is also the function `easy`:

```c
void easy(void)

{
  system("cat flag.txt");
  return;
}
```

The goal is to ret2function. Specifically `easy`. All we need to do is overwrite the return address with the address of `easy`.