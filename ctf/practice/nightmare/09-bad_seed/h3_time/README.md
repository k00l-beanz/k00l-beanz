# time

Start with some basic file enumeration

```s
$ file time 
time: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=4972fe3e2914c74bc97f0623f0c4643c40300dab, not stripped
$ pwn checksec time             
[*] 'time'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Some interesting observations: There is a stack canary so this may pose a challenge if we happen to exploit an overflow, the NX bit is enabled so if we want any code execution we'll have to perform a ret2libc.

Lets look at the `main` function in Ghidra.

```c

undefined8 main(void)

{
  time_t time_;
  long in_FS_OFFSET;
  uint user_input;
  uint random_number;
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  time_ = time((time_t *)0);
  srand((uint)time_);
  random_number = rand();
  puts("Welcome to the number guessing game!");
  puts("I\'m thinking of a number. Can you guess it?");
  puts("Guess right and you get a flag!");
  printf("Enter your number: ");
  fflush(stdout);
  __isoc99_scanf(&DAT_00400bbc,&user_input);
  printf("Your guess was %u.\n",user_input);
  printf("Looking for %u.\n",random_number);
  fflush(stdout);
  if (random_number == user_input) {
    puts("You won. Guess was right! Here\'s your flag:");
    giveFlag();
  }
  else {
    puts("Sorry. Try again, wrong guess!");
  }
  fflush(stdout);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}


```

Looks like there may be a bad seed. Since the PRNG is seeded with the current time we'll be able to predict all following values. I wrote the following C application which'll do this.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

int main() {
    // Generate value
    time_t t = time(0);
    srand(t);
    int r = rand();
    
    // Pipe into ./time
    printf("%d\n", r);

    return 0;
}
```

Compile this 

```s
$ gcc exploit.c -o exploit -Wall
```

And pipe the output of `exploit` into `sleep`.

```s
$ ./exploit | ./time
Welcome to the number guessing game!
Im thinking of a number. Can you guess it?
Guess right and you get a flag!
Enter your number: Your guess was 599206430.
Looking for 599206430.
You won. Guess was right! Heres your flag:
Flag file not found!  Contact an H3 admin for assistance.
```