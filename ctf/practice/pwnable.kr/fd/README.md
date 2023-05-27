# fd

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}
	int fd = atoi( argv[1] ) - 0x1234;
	int len = 0;
	len = read(fd, buf, 32);
	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		system("/bin/cat flag");
		exit(0);
	}
	printf("learn about Linux file IO\n");
	return 0;

}
```

Looking at the program, the user can actually control the first parameter to `read`. A file-descriptor (fd) is like a reference or handle to a file. There are three unique file-descriptors: stdin, stdout, stderr which are 0, 1, and 2 respectivly. Since the user can control the fd being read from, then they would be able to pass a fd of 0 (by running `./fd 4660`) which would cause the program to read from stdin. After that, type `LETMEWIN` and you'll get the flag.