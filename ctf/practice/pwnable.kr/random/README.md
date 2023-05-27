
# random

```c
#include <stdio.h>

int main(){
	unsigned int random;
	random = rand();	// random value!

	unsigned int key=0;
	scanf("%d", &key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Good!\n");
		system("/bin/cat flag");
		return 0;
	}

	printf("Wrong, maybe you should try 2^32 cases.\n");
	return 0;
}
```

In order to obtain pseudo-random numbers (PRN) in a determined machine such as a computer, you'll need some outside random value known as a **seed**. This can be anything that's difficult to predit. Typically, most PRN are seeded with UNIX epoch time. Something like:

```c
srand(time(0));
unsigned int random = rand();
```

This is not done in the application though. When the pseudo-random number generate (PRNG) is not seeded by the program, it will seed itself with with a constant value of 1. Essentially, anyone can predict the number. There are a number of ways to do this such as writing a program to produce the number or look at the number in GDB.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int random = rand();
    printf("%d\n", random);
    return 0;
}
```

This produces `1804289383` = `0x6B8B4567`

To find the key, you can XOR the random number by 0xdeadbeef

`python3 -c "print(0xdeadbeef ^ 0x6B8B4567)"`

Use the result from the operation as the key.