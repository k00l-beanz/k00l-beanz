# Switcheroo

I did not solve this challenge. 

Running `file` to see what I am working with:

```bash
switcheroo: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, BuildID[sha1]=df04d6f80111235725bda5cb27cce1a5e156e683, stripped
```

I also ran `strace` to identify system calls.

```bash
execve("./switcheroo", ["./switcheroo"], 0x7fff7b989840 /* 59 vars */) = 0
write(1, "Give me the flag: ", 18Give me the flag: )      = 18
read(0, flag
"flag\n", 100)                  = 5
write(1, "That was not the flag :(", 24That was not the flag :() = 24
write(1, "\n", 1
)                       = 1
exit(0)                                 = ?
+++ exited with 0 +++
```

No luck. Decompiling this in Ghidra was also unsuccessful:

```bash

/* WARNING: Control flow encountered bad instruction data */
/* WARNING: Removing unreachable block (ram,0x0040102d) */
/* WARNING: Removing unreachable block (ram,0x0040103b) */
/* WARNING: Removing unreachable block (ram,0x00401040) */
/* WARNING: Removing unreachable block (ram,0x00401058) */
/* WARNING: Removing unreachable block (ram,0x0040105d) */
/* WARNING: Removing unreachable block (ram,0x00401066) */
/* WARNING: Removing unreachable block (ram,0x0040106b) */
/* WARNING: Removing unreachable block (ram,0x0040106e) */
/* WARNING: Removing unreachable block (ram,0x00401073) */
/* WARNING: Removing unreachable block (ram,0x00401078) */

void FUN_00401000(void)

{
  syscall();
  syscall();
  syscall();
  syscall();
  syscall();
                    /* WARNING: Bad instruction - Truncating control flow here */
  halt_baddata();
}


```

