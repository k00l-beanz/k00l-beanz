# seed-sPRiNG

Start with some basic enumeration

```bash
file seed_spring 
seed_spring: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=7df253108e1bd837fb708dfaab20362525740ccd, not stripped
```

Check compiler security

```bash
checksec --file=seed_spring 
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      No canary found   NX enabled    PIE enabled     No RPATH   No RUNPATH   77 Symbols        No    0               1               seed_spring
```

Ok. Loading this into Ghidra

```c

/* WARNING: Function: __x86.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 main(undefined param_1)

{
  uint user_input;
  uint rand_num;
  uint timer;
  int cnt;
  undefined *local_10;
  
  local_10 = &param_1;
  puts("");
  puts("");
  puts("                                                                             ");
  puts("                          #                mmmmm  mmmmm    \"    mm   m   mmm ");
  puts("  mmm    mmm    mmm    mmm#          mmm   #   \"# #   \"# mmm    #\"m  # m\"   \"");
  puts(" #   \"  #\"  #  #\"  #  #\" \"#         #   \"  #mmm#\" #mmmm\"   #    # #m # #   mm");
  puts(
      "  \"\"\"m  #\"\"\"\"  #\"\"\"\"  #   #          \"\"\"m  #      #   \"m   #    #  # # #    #"
      );
  puts(" \"mmm\"  \"#mm\"  \"#mm\"  \"#m##         \"mmm\"  #      #    \" mm#mm  #   ##  \"mmm\"");
  puts("                                                                             ");
  puts("");
  puts("");
  puts("Welcome! The game is easy: you jump on a sPRiNG.");
  puts("How high will you fly?");
  puts("");
  fflush(stdout);
  timer = time((time_t *)0);
  srand(timer);
  cnt = 1;
  while( true ) {
    if (30 < cnt) {
      puts("Congratulation! You\'ve won! Here is your flag:\n");
      fflush(stdout);
      get_flag();
      fflush(stdout);
      return 0;
    }
    printf("LEVEL (%d/30)\n",cnt);
    puts("");
    rand_num = rand();
    rand_num = rand_num & 0xf;
    printf("Guess the height: ");
    fflush(stdout);
    __isoc99_scanf(&DAT_00010caa,&user_input);
    fflush(stdin);
    if (rand_num != user_input) break;
    cnt = cnt + 1;
  }
  puts("WRONG! Sorry, better luck next time!");
  fflush(stdout);
                    /* WARNING: Subroutine does not return */
  exit(-1);
}
```

Looking at this code, you see that `srand` is seeded with the current time and then random numbers are generated based off this randomness. However, this is PRNG. If you know the time (which is now) then you can predict the numbers. You can write a program which genrates the values for you and feeds them into the program.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main(void) {
        srand(time(0));

        for (int i = 0; i < 30; i++ ) {
                printf("%d\n", rand() & 0xf);
        }
}

```

Pipe this output to the nc socket and you'll get your flag.

```bash
./main | nc jupiter.challenges.picoctf.org 35856 
```