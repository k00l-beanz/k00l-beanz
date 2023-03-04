# collision

I wrote a debug version of the application which just adds some print statements. Compile with: `gcc debug.c -o debug -m32`

```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;

unsigned long check_password(const char* p){
	int* ip = (int*)p;
	int i;
	int res=0;
	for(i=0; i<5; i++){
		res += ip[i];
	}
	return res;
}

int main(int argc, char* argv[]){
	if(argc<2){
		printf("usage : %s [passcode]\n", argv[0]);
		return 0;
	}
	if(strlen(argv[1]) != 20){
		printf("passcode length should be 20 bytes\n");
		return 0;
	}

	if(hashcode == check_password( argv[1] )){
		system("/bin/cat flag");
		return 0;
	}
	else
		printf("wrong passcode.\n");
	return 0;
}
```

This problem introduces casting pointers. In `check_password` the program casts `p` from a `char*` to `int*`. 

```bash
$ file col
col: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=05a10e253161f02d8e6553d95018bc82c7b531fe, not stripped
```

This is a 32-bit program. This means an `int` is 4 bytes. So an `int*` "points" in 4 byte intervals.

```
$ ./col AAAABBBBCCCCDDDDEEEE

Character pointer:
| 0x41 | 0x41 | 0x41 | 0x41 | 0x42 | 0x42 | 0x42 | 0x42 | 0x43 | 0x43 | 0x43 | 0x43 | 0x44 | 0x44 | 0x44 | 0x44 | 0x45 | 0x45 | 0x45 | 0x45 |

Integer pointer
| 0x41414141 | 0x42424242 | 0x43434343 | 0x44444444 | 0x45454545 | 
```

This means you need to determine five 4-byte integers which totals to 0x21DD09EC (568134124).

`568134124 // 5 = 113626824 => 0x06C5CEC8`

Because 568134124 is not divisible by 5, so you'll need to sprinkle the remainder about:

```
| 0x06C5CEC8 | 0x06C5CEC9 | 0x06C5CEC9 | 0x06C5CEC9 | 0x06C5CEC9 |
```

You can write this payload out with python3. To execute the payload as a command line argument, wrap the python3 command in $():

```bash
$ ./col $(python3 -c "import sys; sys.stdout.buffer.write(b'\xc8\xce\xc5\x06' + b'\xc9\xce\xc5\x06' * 4)")
```