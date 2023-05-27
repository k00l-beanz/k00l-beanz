# ctfd_plus

I did not solve this problem.

I ran `file` on the provided binary:

```bash
ctfd_plus: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e5b4c36aec894c85329590aeadb6ed7016ebc770, for GNU/Linux 3.2.0, stripped
```

I put this application into Ghidra and found the main method.

```bash

undefined8 main(void)

{
  int encoded_byte;
  size_t sVar1;
  long i;
  undefined4 *encoded_bytes;
  char user_input [256];
  
  puts("Welcome to CTFd+!");
  puts(
      "So far, we only have one challenge, which is one more than the number of databases we have.\n "
      );
  puts("Very Doable Pwn - 500 points, 0 solves");
  puts("Can you help me pwn this program?");
  puts("#include <stdio.h>\nint main(void) {\n    puts(\"Bye!\");\n    return 0;\n}\n");
  puts("Enter the flag:");
  fgets(user_input,0x100,stdin);
  sVar1 = strcspn(user_input,"\n");
  i = 0;
  encoded_bytes = &DAT_00104060;
  user_input[sVar1] = '\0';
  do {
    encoded_byte = encode(encoded_bytes[i]);
    if ((char)encoded_byte != user_input[i]) {
      puts("Incorrect flag.");
      return 0;
    }
    i = i + 1;
  } while (i != 47);
  puts("You got the flag! Unfortunately we don\'t exactly have a database to store the solve in...")
  ;
  return 0;
}


```

My intuition tells me to use one of the following approaches:
- Angr
- Create a gdb script to slowly extract the character byte-by-byte
- Create a script with pwntools

I ended up using Angr in the solution.

