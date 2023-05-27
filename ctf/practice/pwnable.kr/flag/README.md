# flag

Cool a reversing challenge. First, some basic enumeration:

```bash
$ file flag  
flag: ELF 64-bit LSB executable, x86-64, version 1 (GNU/Linux), statically linked, no section header
```

Interesting. Taking a look at securities:

```bash
$ checksec --file=flag  
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   No Symbols        No    0               0               flag
```

Lastly, I run strings:

```
UPX!
@/x8
gX lw_
H/\_@
        Kl$
H9\$(t
[]]y
nIV,Uh
AWAVAUATS
uSL9
>t              
[A\AA;h
]A^A_*U
A4tV
bl@(
...<snip>...
```

At the very beginning, there is a string `UPX!` which is an ELF packing scheme. You can read more about it [here](https://upx.github.io/).

You can decomporess this binary using `upx`

```bash
$ upx -d flag -o flag_d
```

Afterwards, you can drop this file into Ghidra. There are a lot of text symbols but `main` is easily findable.

```c

undefined8 main(void)

{
  char *__dest;
  
  puts("I will malloc() and strcpy the flag there. take it.");
  __dest = (char *)malloc(100);
  strcpy(__dest,"UPX...? sounds like a delivery service :)");
  return 0;
}

```