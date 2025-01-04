# buffer-overflow-3

## Description

Do you think you can bypass the protection and get the flag? 

## Enumeration

Checking the artifact type:

```bash
$ file ./vuln
./vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=880ddfdc7ef13c4139ab8a80cc3d8225251a331f, for GNU/Linux 3.2.0, not stripped
```

ELF 32-bit LSB. Dynamically linked. Not stripped

Lets check the artifact protections:

```bash
$ pwn checksec ./vuln                                                                                                                                                           
[*] './vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```

We have a partial RELRO and the NX bit is enabled. Buffer overflows will be easy but getting code execution might be tricky.

## Code Review

Reviewing some code:

```c
int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  read_canary();
  vuln();
  return 0;
}

```

`main` calls two functions: `read_canary` and `vuln`. Lets look at `read_canary`:

```c

char global_canary[CANARY_SIZE];
void read_canary() {
  FILE *f = fopen("canary.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'canary.txt' in this directory with your",
                    "own debugging canary.\n");
    fflush(stdout);
    exit(0);
  }

  fread(global_canary,sizeof(char),CANARY_SIZE,f);
  fclose(f);
}
```

This function reads 'canary.txt' into `global_canary`. 

Lets look at `vuln`

```c
void vuln(){
   char canary[CANARY_SIZE];
   char buf[BUFSIZE];
   char length[BUFSIZE];
   int count;
   int x = 0;
   memcpy(canary,global_canary,CANARY_SIZE);
   printf("How Many Bytes will You Write Into the Buffer?\n> ");
   while (x<BUFSIZE) {
      read(0,length+x,1);
      if (length[x]=='\n') break;
      x++;
   }
   sscanf(length,"%d",&count);

   printf("Input> ");
   read(0,buf,count);

   if (memcmp(canary,global_canary,CANARY_SIZE)) {
      printf("***** Stack Smashing Detected ***** : Canary Value Corrupt!\n"); // crash immediately
      fflush(stdout);
      exit(0);
   }
   printf("Ok... Now Where's the Flag?\n");
   fflush(stdout);
}
```

This function copies the canary from the global memory section (probably the .bss section) into the local stack frame. It then asks how many bytes we'd like to write. Then the program reads that many bytes from standard input.

There's a catch though. After reading in the payload, there is a `memcmp` call which compares the value of the canary in the stack frame to the value of the canary in the .bss section. If they don't equivalate, the program calls `exit`. 

## Exploit Development

Since the stack canary is a static value (loaded from the same file every time) we can simply brute force the canary.

We can accomplish this by overwriting one byte of the canary at a time.

If the program returns `***** Stack Smashing Detected ***** : Canary Value Corrupt!` we know we guessed the wrong value for one of the bytes of the canary. However, if this does not happen, then we know we guessed the correct value.

find canary offset from our buffer:

```bash
gef➤  disass vuln                                    
Dump of assembler code for function vuln:
   0x08049489 <+0>:     endbr32       
   0x0804948d <+4>:     push   ebp
   0x0804948e <+5>:     mov    ebp,esp             
   0x08049490 <+7>:     push   ebx    
   0x08049491 <+8>:     sub    esp,0x94        
   0x08049497 <+14>:    call   0x8049270 <__x86.get_pc_thunk.bx>
   0x0804949c <+19>:    add    ebx,0x2b64          
   0x080494a2 <+25>:    mov    DWORD PTR [ebp-0xc],0x0
   0x080494a9 <+32>:    mov    eax,0x804c054          
   0x080494af <+38>:    mov    eax,DWORD PTR [eax]
   0x080494b1 <+40>:    mov    DWORD PTR [ebp-0x10],eax
   0x080494b4 <+43>:    sub    esp,0xc
   0x080494b7 <+46>:    lea    eax,[ebx-0x1f40]      
   0x080494bd <+52>:    push   eax     
   0x080494be <+53>:    call   0x8049140 <printf@plt>
...
gef➤  x/s $ebp-0x10
0xffffce38:     "DEAD"

```

Looks like the compiler optimized the code a bit. Instead of making a `memcpy` call, it instead dereferences an address and moves the contents on the stack

```bash
...
   0x08049534 <+171>:   mov    eax,DWORD PTR [ebp-0x94]
   0x0804953a <+177>:   sub    esp,0x4
   0x0804953d <+180>:   push   eax
   0x0804953e <+181>:   lea    eax,[ebp-0x50]
   0x08049541 <+184>:   push   eax
   0x08049542 <+185>:   push   0x0
   0x08049544 <+187>:   call   0x8049130 <read@plt>
...
```

Remember, x86 calling convention is right-to-left (RTL) so the first push is the count (ebp-0x84), the second is the start of the buffer (ebp-0x50) and the third is the file description. 

0x50 - 0x10 = 64

We can verify by using patterns:

```bash
gef➤  pattern offset $ebp-0x10
[+] Searching for '71616161'/'61616171' with period=4
[+] Found at offset 64 (little-endian search) likely

```