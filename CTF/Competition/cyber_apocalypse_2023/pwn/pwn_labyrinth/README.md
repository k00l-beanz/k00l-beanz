# labyrinth

Start with some basic file enumeration:

```s
$ file labyrinth 
labyrinth: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=86c87230616a87809e53b766b99987df9bf89ad8, for GNU/Linux 3.2.0, not stripped
$ pwn checksec --file labyrinth 
[*] 'labyrinth'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
    RUNPATH:  b'./glibc/'
```

Note that this app has full RELRO so you cannot overwrite the GOT. The NX bit is also enabled so if you want any kind of code execution you'll have to perform a ret2libc.

Throwing this app into Ghidra and viewing `main`

```c
undefined8 main(void)
{
  int iVar1;
  undefined8 door_input;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  char *ans;
  ulong i;
  
  setup();
  banner();
  door_input = 0;
  local_30 = 0;
  local_28 = 0;
  local_20 = 0;
  fwrite("\nSelect door: \n\n",1,16,stdout);
  for (i = 1; i < 101; i = i + 1) {
    iVar1 = (int)i;
    if (i < 10) {
      fprintf(stdout,"Door: 00%d ",iVar1);
    }
    else if (i < 100) {
      fprintf(stdout,"Door: 0%d ",iVar1);
    }
    else {
      fprintf(stdout,"Door: %d ",iVar1);
    }
    if ((i % 10 == 0) && (i != 0)) {
      putchar(10);
    }
  }
  fwrite(&DAT_0040248f,1,4,stdout);
  ans = (char *)malloc(16);
  fgets(ans,5,stdin);
  iVar1 = strncmp(ans,"69",2);
  if (iVar1 != 0) {
    iVar1 = strncmp(ans,"069",3);
    if (iVar1 != 0) goto LAB_004015da;
  }
  fwrite("\nYou are heading to open the door but you suddenly see something on the wall:\n\n\"Fly li ke a bird and be free!\"\n\nWould you like to change the door you chose?\n\n>> "
         ,1,0xa0,stdout);
  fgets((char *)&door_input,68,stdin);
LAB_004015da:
  fprintf(stdout,"\n%s[-] YOU FAILED TO ESCAPE!\n\n","\x1b[1;31m");
  return 0;
}
```

There are two times the app takes user input: For our first answer and when you are asked in you would like to change your mind. The first `fgets` looks safe as 16 bytes are allocated on the heap and the user is only allowed to input 5 bytes. The second `fgets` however is not safe.

Looking at the stack layout for stack variables:

```s
**************************************************************
*                          FUNCTION                          *
**************************************************************
undefined8 __stdcall main(void)
undefined8        RAX:8          <RETURN>
undefined8        Stack[-0x10]:8 i          
undefined8        Stack[-0x18]:8 ans                 
undefined8        Stack[-0x20]:8 local_20               
undefined8        Stack[-0x28]:8 local_28                  
undefined8        Stack[-0x30]:8 local_30          
undefined8        Stack[-0x38]:8 door_input     
```

The `door_input` variable is located 0x30 bytes (48) bytes up the stack. The user is allowed to input 68 bytes causing an overflow.

First, determine the offset to the return pointer:

```s
gef➤  pattern offset $rsp
[+] Searching for '$rsp'
[+] Found at offset 56 (little-endian search) likely
[+] Found at offset 49 (big-endian search) 
gef➤ 
```

Ok. So where do you jump to? What do you do with this power? There is a function `escape_plan` which ends up printing out the flag:

```c
void escape_plan(void)
{
  ssize_t sVar1;
  char flag_buf;
  int flag_fh;
  
  putchar(10);
  fwrite(&DAT_00402018,1,496,stdout);
  fprintf(stdout,
          "\n%sCongratulations on escaping! Here is a sacred spell to help you continue your journey : %s\n"
          ,"\x1b[1;32m","\x1b[0m");
  flag_fh = open("./flag.txt",0);
  if (flag_fh < 0) {
    perror("\nError opening flag.txt, please contact an Administrator.\n\n");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  while( true ) {
    sVar1 = read(flag_fh,&flag_buf,1);
    if (sVar1 < 1) break;
    fputc((int)flag_buf,stdout);
  }
  close(flag_fh);
  return;
}
```

Lets try jumping here. First, determine the address of `escape_plan`.

```s
gef➤  p escape_plan
$1 = {<text variable, no debug info>} 0x401255 <escape_plan>
```

However, jumping directly to the beginning of this function still doesn't get the flag:

```s
$ ./exploit.py LOCAL      
[+] Starting local process 'labyrinth': pid 6643
[*] Switching to interactive mode
 
[-] YOU FAILED TO ESCAPE!


                \O/               
                 |                 
                / \               
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒           ▒          ▒
▒-▸        ▒           ▒          ▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▲△▲△▲△▲△▲△▒
[*] Got EOF while reading in interactive
$
```

It seems the program SIGSEGV after the `fprintf` at `0x00000000004012ab`. I'm not actually sure why this occurs. The fact of the matter is that you cannot jump to the beginning of `escape_plan`. Where else can you jump then? Well, nothing says you have to jump to the beginning of the function. Lets try jumping to the `open` for the flag. You actually need to jump a few instructions before the `open` so the program can set up the `open` call correctly. I decide to jump to `0x00000000004012b0`.

When doing this, you end up SEGBUS'ing because you are trying to move EAX to an invalid memory address at instruction `0x4012c6`

```s
gef➤  x/xw $rbp-0x4
0x414141414141413d:     Cannot access memory at address 0x414141414141413d
```

As an attacker you can control where this points to. You just need to determine a valid address.

Attempted:
- static stack address - FAILED REMOTELY - I can print the flag locally but not remotely. Perhaps ASLR is enabled server side or the address space is different for the docker container
- ret2libc to leak an address - FAILED - not enough space to fully ret2libc
- There is an uncalled method `read_num` which has a partial overflow of ~2 bytes. Not enough to do anything with. 
- Jump directly to the `read` call in the while loop which causes `read` to read from stdin. Only one byte can be read however and attacker can't control file handle.