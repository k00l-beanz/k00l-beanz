# Optimistic

## Recon


- 64-bit
- PIE executable
- dynamically linked
- not stripped
```bash
file optimistic
optimistic: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=24f4b065a2eab20657772e85de2af83b2f6fe8b1, for GNU/Linux 3.2.0, not stripped
```

- No canaries
- Potentially executable stack
```bash
$ pwn checksec optimistic
[*] '/home/user/Documents/repos/k00l-beanz/hackthebox/challenges/pwn/optimistic/optimistic'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      PIE enabled
    Stack:    Executable
    RWX:      Has RWX segments
```

- Stack may be executable
```bash
$ readelf -l -W optimistic | grep "GNU_STACK"
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RWE 0x10
```

## Code Review

- A stack address is leaked 
- provide email and age
- we can provide the length of our name
    - not allowed to input anything >64
    - however, during the conditional, our input is converted into an `int` primitive
    - `int` is signed. Inputting a negative will pass validation while also causinga buffer overflow
```c
void main(void) {
  int iVar1;
  ssize_t sVar2;
  uint name_length;
  undefined4 local_80;
  undefined2 local_7c;
  char local_7a;
  undefined local_79;
  undefined email [8];
  undefined age [8];
  char target [96];
  
  initialize();
  puts("Welcome to the positive community!");
  puts("We help you embrace optimism.");
  printf("Would you like to enroll yourself? (y/n): ");
  iVar1 = getchar();
  local_7a = (char)iVar1;
  getchar();
  if (local_7a != 'y') {
    puts("Too bad, see you next time :(");
    local_79 = 110;
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  printf("Great! Here\'s a small welcome gift: %p\n",&stack0xfffffffffffffff8);
  puts("Please provide your details.");
  printf("Email: ");
  sVar2 = read(0,email,8);
  local_7c = (undefined2)sVar2;
  printf("Age: ");
  sVar2 = read(0,age,8);
  local_80 = (undefined4)sVar2;
  printf("Length of name: ");
  __isoc99_scanf(&DAT_00102104,&name_length);
  if (64 < (int)name_length) {
    puts("Woah there! You shouldn\'t be too optimistic.");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  printf("Name: ");
  sVar2 = read(0,target,(ulong)name_length);
  name_length = 0;
  while( true ) {
    if ((int)sVar2 + -9 <= (int)name_length) {
      puts("Thank you! We\'ll be in touch soon.");
      return;
    }
    iVar1 = isalpha((int)target[(int)name_length]);
    if ((iVar1 == 0) && (9 < (int)target[(int)name_length] - 0x30U)) break;
    name_length = name_length + 1;
  }
  puts("Sorry, that\'s an invalid name.");
                    /* WARNING: Subroutine does not return */
  exit(0);
}
```


## Finding offset

- Email: email
- Age: 1337
- Length of name: -1
- Name: aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaaaataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabdaaaaaabeaaaaaabfaaaaaabgaaaaaa

Offset to return pointer is 104
Offset to stack leak is 96

start of buffer 0x00007fffffffdbd0
leak address 0x7fffffffdc30

https://www.exploit-db.com/shellcodes/35205