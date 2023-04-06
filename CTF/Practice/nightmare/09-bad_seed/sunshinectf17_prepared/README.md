# prepared

Lets start with some basic file enumeration:

```s
$ file prepared   
prepared: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=9cd9483ed0e7707d3addd2de44da60d2575652fb, not stripped
$ pwn checksec prepared             
[*] 'prepared'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

All securities enabled. This should be interesting.

Lets look at the `main` function in Ghidra

```c

undefined8 main(void)

{
  int rand_;
  time_t time_;
  FILE *__stream;
  char *pcVar1;
  long in_FS_OFFSET;
  int i;
  char local_448 [64];
  char user_input_ [512];
  char char_rand_ [504];
  long canary;
  
  canary = *(long *)(in_FS_OFFSET + 0x28);
  time_ = time((time_t *)0x0);
  srand((uint)time_);
  for (i = 0; i < 50; i = i + 1) {
    rand_ = rand();
    printf("%d days without an incident.\n",i);
    sprintf(char_rand_,"%d",rand_ % 100);
    __isoc99_scanf(" %10s",user_input_);
    strtok(user_input_,"\n");
    rand_ = strcmp(char_rand_,user_input_);
    if (rand_ != 0) {
      puts("Well that didn\'t take long.");
      printf("You should have used %s.\n",char_rand_);
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
  }
  puts("How very unpredictable. Level Cleared");
  __stream = fopen("flag.txt","r");
  while( true ) {
    pcVar1 = fgets(local_448,0x32,__stream);
    if (pcVar1 == (char *)0x0) break;
    printf("%s",local_448);
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}


```

The first half is where the real meat of the application is. Looks like we'll need to guess 50 numbers correctly in order. Fortunately, the PRNG is seeded with current time so these numbers become predictable. I wrote the following to just that:

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    time_t t = time(0);
    srand(t);

    int num = 0;
    for (int i = 0; i < 50; i++) {
        num = rand() % 100;
        printf("%d\n", num);
    }

    return 0;
}
```

Compile and run:

```s
$ ./exploit | ./prepared  
0 days without an incident.
1 days without an incident.
2 days without an incident.
3 days without an incident.
4 days without an incident.
5 days without an incident.
6 days without an incident.
7 days without an incident.
8 days without an incident.
9 days without an incident.
10 days without an incident.
11 days without an incident.
12 days without an incident.
13 days without an incident.
14 days without an incident.
15 days without an incident.
16 days without an incident.
17 days without an incident.
18 days without an incident.
19 days without an incident.
20 days without an incident.
21 days without an incident.
22 days without an incident.
23 days without an incident.
24 days without an incident.
25 days without an incident.
26 days without an incident.
27 days without an incident.
28 days without an incident.
29 days without an incident.
30 days without an incident.
31 days without an incident.
32 days without an incident.
33 days without an incident.
34 days without an incident.
35 days without an incident.
36 days without an incident.
37 days without an incident.
38 days without an incident.
39 days without an incident.
40 days without an incident.
41 days without an incident.
42 days without an incident.
43 days without an incident.
44 days without an incident.
45 days without an incident.
46 days without an incident.
47 days without an incident.
48 days without an incident.
49 days without an incident.
How very unpredictable. Level Cleared
isun{pr3d1ct_3very_p[]5s1bl3_scen@r10}
```