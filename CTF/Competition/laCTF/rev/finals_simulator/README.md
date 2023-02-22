# finals-simulator

This was a pretty straight-forward reversing challenge. 

First, we are given `finals_simulator` which is an `ELF 64-bit` executable:

```bash
file finals_simulator
finals_simulator: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=48a8db43abba37f8eedf3cc4c9a5d4fee28be7cb, for GNU/Linux 3.2.0, not stripped
```

Putting this in Ghidra returns the following decompiled code:
```C
undefined8 main(void)

{
  int iVar1;
  size_t sVar2;
  int user_input_q2;
  char user_input_q1 [264];
  char *char;
  
  puts("Welcome to Finals Simulator 2023: Math Edition!");
  printf("Question #1: What is sin(x)/n? ");
  fflush(stdout);
  fgets(user_input_q1,0x100,stdin);
  sVar2 = strcspn(user_input_q1,"\n");
  user_input_q1[sVar2] = '\0';
  iVar1 = strcmp(user_input_q1,"six");
  if (iVar1 == 0) {
    printf("Question #2: What\'s the prettiest number? ");
    fflush(stdout);
    __isoc99_scanf(&DAT_001020c3,&user_input_q2);
    if ((user_input_q2 + 88) * 42 == 561599850) {
      printf("Question #3: What\'s the integral of 1/cabin dcabin? ");
      fflush(stdout);
      getchar();
      fgets(user_input_q1,0x100,stdin);
      sVar2 = strcspn(user_input_q1,"\n");
      user_input_q1[sVar2] = '\0';
      for (char = user_input_q1; *char != '\0'; char = char + 1) {
        *char = (char)((long)(*char * 17) % 253);
      }
      putchar(10);
      iVar1 = strcmp(user_input_q1,&enc);
      if (iVar1 == 0) {
        puts("Wow! A 100%! You must be really good at math! Here, have a flag as a reward.");
        print_flag();
      }
      else {
        puts("Wrong! You failed.");
      }
    }
    else {
      puts("Wrong! You failed.");
    }
  }
  else {
    puts("Wrong! You failed.");
  }
  return 0;
}
```

The first two questions are pretty easy to solve.

The answer to the first question is: `six`

The second answer can be solved with basic algebra:

`(x + 88) * 42 = 561599850`

The anser to the second question is: `13371337`

At first I thought the last question involved some cryptography and finding the modular inverse of blah, blah, blah...

But the final string is actually `strcmp` afterwards. The solution is "hard coded" into the binary somewhere. Taking a look at `enc`:

```
                     enc                                             XREF[2]:     Entry Point(*), main:001013f8(*)  
00104080 0e              ??         0Eh
00104081 c9              ??         C9h
00104082 9d              ??         9Dh
00104083 b8              ??         B8h
00104084 26              ??         26h    &
00104085 83              ??         83h
00104086 26              ??         26h    &
00104087 41              ??         41h    A
00104088 74              ??         74h    t
00104089 e9              ??         E9h
0010408a 26              ??         26h    &
0010408b a5              ??         A5h
0010408c 83              ??         83h
0010408d 94              ??         94h
0010408e 0e              ??         0Eh
0010408f 63              ??         63h    c
00104090 37              ??         37h    7
00104091 37              ??         37h    7
00104092 37              ??         37h    7
00104093 00              ??         00h
```

Since every character can only be 1 of 256 characters and you know what the result should be, you can brute force the solution pretty quickly. 

```python
def hexStrToDec(enc: list)-> list:
    return [int(enc[i], 16) for i in range(len(enc))]

enc = ["0E","C9", "9D", "B8", "26", "83", "26", "41", "74", "E9", "26", "A5", "83", "94", "0E", "63", "37", "37", "37"]
enc = hexStrToDec(enc)

flag = ""
for i in range(len(enc)):
    for j in range(256):
        x = (j * 17) % 253
        if x == enc[i]:
            flag += chr(j)
            break

print(flag)
```

Flag: `lactf{im_n0t_qu1t3_sur3_th4ts_h0w_m4th_w0rks_bu7_0k}`