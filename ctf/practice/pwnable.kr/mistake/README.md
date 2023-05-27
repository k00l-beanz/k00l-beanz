# mistake

```c
#include <stdio.h>
#include <fcntl.h>

#define PW_LEN 10
#define XORKEY 1

void xor(char* s, int len){
	int i;
	for(i=0; i<len; i++){
		s[i] ^= XORKEY;
	}
}

int main(int argc, char* argv[]){
	
	int fd;
	if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){ 
		printf("can't open password %d\n", fd);
		return 0;
	}

	printf("do not bruteforce...\n");
	sleep(time(0)%20);

	char pw_buf[PW_LEN+1];
	int len;
	if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
		printf("read error\n");
		close(fd);
		return 0;		
	}

	char pw_buf2[PW_LEN+1];
	printf("input password : ");
	scanf("%10s", pw_buf2);

	// xor your input
	xor(pw_buf2, 10);

	if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
		printf("Password OK\n");
		system("/bin/cat flag\n");
	}
	else{
		printf("Wrong Password\n");
	}

	close(fd);
	return 0;
}
```

If you think about it, all computers do is perform a series of math equations really quickly. In math there is the concept of order-of-operatoin (PEMDAS nightmares ensue). Programming langauges are no different. There is an order-of-evaluations. You can see the table of precedence [here](https://en.cppreference.com/w/c/language/operator_precedence).

You can see that relational operators (6) are evaluated before assignment operators (14). This means the line where the application calls `open` evaluates differently then you might think. According the the libc man page for `open`, `open` returns a non-negative integer when successful. The line-of-code will be evaluated like:

```
fd = (open("/home/mistake/password", O_RDONLY, 0400) < 0)
fd = (1 < 0)
fd = false
fd = 0
```

fd evaluates to 0. Later the program calls `read` from the specified file descriptor. If this value is 0 (stdin) then a user can control the value of `pw_buf` by putting whatever they want.

Next, you need to determine two values that will evaluate to true. Since you control the input and know the key (`XORKEY`), the output is predictable. I chose an easy payload of `BBBBBBBBBB` for `pw_buf2` and `CCCCCCCCCC` for `pw_buf`.