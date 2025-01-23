# Yan85 Specs

This document contains the reverse-engineered specifications of the Yan85 architecture.

## Architecture

The Yan85 architecture is fully initialized within the main function and operates entirely on the stack.

The architecture is divided into three key components:

- Code Segment
- Memory Segment
- Register Segment

The initialization of each component is handled within the main function.

### Code Segment

The Code Segment is analogous to the x86 .text program header section. It contains executable bytecode that executes on the machine and alters its state.

The Code Segment is created by reading the Yan85 bytecode onto the stack. The method for loading the bytecode onto the stack varies between challenges. When the bytecode is embedded within the ELF binary, a memcpy subroutine is typically used to copy the bytecode from the .data section onto the stack.

```bash
0x555555556388 <main+010d>      call   0x555555555130 <memcpy@plt>
memcpy@plt (
   $rdi = 0x00007fffffffde70 → 0x0000000000000000,
   $rsi = 0x0000555555559020 → <vm_code+0000> and BYTE PTR [rcx], al,
   $rdx = 0x000000000000027c
)
```

However, if the user needs to write and provide their own Yan85 bytecode, a read subroutine is used instead:

```bash
0x555555556374 <main+0119>      call   0x555555555110 <read@plt>
read@plt (
   $rdi = 0x0000000000000000,
   $rsi = 0x00007fffffffde70 → 0x0000000000000000,
   $rdx = 0x0000000000000300,
   $rcx = 0x0000000000000000
)
```

Both methods indicate where on the stack the bytecode will be written.

The base address of the Code Segment is regarded as the base address for the Yan85 emulator.

### Memory Segment

The Memory Segment is similar to the x86 stack segment section. It stores data to be processed by the Yan85 bytecode. The Memory Segment is typically 0x100 bytes (256 bytes) in size.

The start address of the Memory Segment can be identified by adding 0x400 bytes to the base address of the Yan85 emulator:

```bash
gef➤  x/gx 0x00007fffffffde70 + 0x400
0x7fffffffe270: 0x0000000000000000
```

If the user provides the Yan85 bytecode, it is unlikely that there will be an initial Memory Segment state within the ELF (i.e., there won't be a vm_mem .data variable to copy into the stack).

However, if an initial Memory Segment state exists, the vm_mem is copied onto the stack. This happens immediately after the memcpy subroutine call:

```bash
0x0000555555556388 <+269>:   call   0x555555555130 <memcpy@plt>
0x000055555555638d <+274>:   mov    rax,QWORD PTR [rip+0x2f4c]        # 0x5555555592e0 <vm_mem>
0x0000555555556394 <+281>:   mov    rdx,QWORD PTR [rip+0x2f4d]        # 0x5555555592e8 <vm_mem+8>
0x000055555555639b <+288>:   mov    QWORD PTR [rbp-0x110],rax
0x00005555555563a2 <+295>:   mov    QWORD PTR [rbp-0x108],rdx
```

### Register Segment

The Register Segment contains the registers used by the Yan85 emulator. There are 7 registers:

1. a - General purpose
2. b - General purpose
3. c - General purpose
4. d - General purpose
5. s - Stack counter
6. i - Instruction counter
7. f - Flags

The Register Segment consists of the first seven bytes of the Memory Segment. I've chosen to separate this section into its own component because registers have distinct functionality compared to regular memory.

The base address of the Register Segment can be determined by adding 0x400 bytes to the base address of the Yan85 emulator.

```bash
gef➤  x/7xb 0x00007fffffffde70 + 0x400
0x7fffffffe270: 0x00    0x00    0x00    0x00    0x00    0x00    0x00
```

The Registers are always at the same offsets:

```
a -> 0x400
b -> 0x401
c -> 0x402
d -> 0x403
s -> 0x404
i -> 0x405
f -> 0x406
```

### Final Architecture
The final architecture is shown in the following image:

![Yan85 Machine](Yan85-Architecture.png)

## Yan85 Bytecode

The Yan85 architecture uses three bytes per instruction. These three bytes represent:

- The type of instruction
- Argument one
- Argument two

The order of the bytecode varies depending on the level. For example:

For example, one level could have bytecode follow this format:

| inst | arg1 | arg2 |

While another level could have the bytecode follow this format:

| arg1 | arg2 | inst |

### Determining Yan85 Bytecode Order

Since the bytecode format varies with each challenge, you'll need a method to determine the correct order for interpreting the bytecode and understanding its impact on the Yan85 emulator. Each level presents the bytecode differently, and in some cases, you'll be required to write your own Yan85 bytecode.

In this section, I’ll cover a quick method to identify the bytecode format and explain how to extract the bytecode from the ELF binary, both statically and dynamically.

#### Extracting Bytecode from the ELF and Memory

In some levels, the Yan85 bytecode will be embedded within the challenge itself. For example, in level19, when dumping the symbols of the ELF:

```bash
$ objdump -t ./babyrev-level-19-0 | grep "vm_"
000000000000529c g     O .data  0000000000000004              vm_code_length
00000000000052e0 g     O .bss   0000000000000100              vm_mem
0000000000005020 g     O .data  000000000000027c              vm_code
```

This will reveal that the initial vm_mem is stored in the .bss section of the ELF, while the vm_code is located in the .data section. An indicator of the initial memory state can be found by observing which section vm_mem resides in: the .bss section stores uninitialized data (indicating no initial memory state), whereas the .data section stores initialized data. When facing a challenge like this, the first step is to dump vm_mem and vm_code into separate files.

First, you’ll need the in-memory address offsets. Using objdump, we find that the address offsets for vm_mem and vm_code are 0x52e0 and 0x5020, respectively. Next, you’ll need to determine which program header these variables are loaded into.

```bash
$ readelf -lW ./babyrev-level-19-0
Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000000040 0x0000000000000040 0x0002d8 0x0002d8 R   0x8
  INTERP         0x000318 0x0000000000000318 0x0000000000000318 0x00001c 0x00001c R   0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x000870 0x000870 R   0x1000
  LOAD           0x001000 0x0000000000001000 0x0000000000001000 0x001625 0x001625 R E 0x1000
  LOAD           0x003000 0x0000000000003000 0x0000000000003000 0x000a68 0x000a68 R   0x1000
  LOAD           0x003d70 0x0000000000004d70 0x0000000000004d70 0x000530 0x000670 RW  0x1000
  DYNAMIC        0x003d80 0x0000000000004d80 0x0000000000004d80 0x0001f0 0x0001f0 RW  0x8
  NOTE           0x000338 0x0000000000000338 0x0000000000000338 0x000020 0x000020 R   0x8
  NOTE           0x000358 0x0000000000000358 0x0000000000000358 0x000044 0x000044 R   0x4
  GNU_PROPERTY   0x000338 0x0000000000000338 0x0000000000000338 0x000020 0x000020 R   0x8
  GNU_EH_FRAME   0x00356c 0x000000000000356c 0x000000000000356c 0x0000fc 0x0000fc R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0x10
  GNU_RELRO      0x003d70 0x0000000000004d70 0x0000000000004d70 0x000290 0x000290 R   0x1
```

To locate the correct LOAD section, we examine each one until we find the range in which our addresses fall. The address range can be determined using the formula:
VirtAddr + FileSiz

- 0x0000000000000000 + 0x000870 = 0x870
- 0x0000000000001000 + 0x001625 = 0x2625
- 0x0000000000003000 + 0x000a68 = 0x3a68
- 0x0000000000004d70 + 0x000530 = 0x52a0

The fourth LOAD section contains our vm_ variables. The offset for this LOAD section is 0x003d70. Thus, the physical address in the ELF file can be calculated as:

addr. in memory - VirtMem + offset

For example:
0x5020 - 0x4d70 + 0x3d70 = 0x4020

Next, extract the data from the ELF file. The size of the section (obtained using objdump) is 0x27c (or 636 bytes).

```bash
dd if=./babyrev-level-19-0 of=./vm_code bs=1 count=636 skip=16416
```

Comparing the vm_code file I created with the vm_code in memory:

```bash
$ xxd -c 18 -g 3 ./vm_code
00000000: 200180 200227 040102 400801 020210 020110   .. .'...@........
...<snip>...

gef➤  x/3xb 0x0000555555559020
0x555555559020 <vm_code>:       0x20    0x01    0x80
```

For challenges where symbols are stripped from the ELF binary, you can locate the section based on the address referenced in the main function. This method of dumping Yan85 bytecode from the debugger is faster and works well for black-boxed challenges.

First, identify where vm_code or vm_memory is referenced in main. A reliable approach is to set a breakpoint at the memcpy call.

```bash
gef➤  x/64i 0x555555555cd8
...<snip>...
   0x555555555de2:      mov    rdi,rax
   0x555555555de5:      call   0x555555555130 <memcpy@plt>
   0x555555555dea:      mov    rax,QWORD PTR [rip+0x350f]        # 0x555555559300
...<snip>...
gef➤  b *0x555555555de5
gef➤  r
...<snip>...
memcpy@plt (
   $rdi = 0x00007fffffffde70 → 0x0000000000000000,
   $rsi = 0x0000555555559020 →  rex add DWORD PTR [rax+0x1805502], eax,
   $rdx = 0x00000000000002a9
)
...<snip>...
gef➤  x/3xb 0x0000555555559020
0x555555559020: 0x40    0x01    0x80
```

This provides both the size and the address of vm_code. Using the `dump binary memory` command in GDB, you can extract the vm_code.

```bash
gef➤  dump binary memory vm_code.bin 0x555555559020 0x555555559020+0x2a9

$ xxd -c 18 -g 3 ./vm_code.bin
00000000: 400180 025580 019580 010220 027b80 019680  @...U...... .{...
```

To retrieve vm_mem, examine the instruction following the memcpy call. This instruction contains the starting address of vm_mem, where it begins copying vm_mem onto the stack.

```bash
0x555555555de5:      call   0x555555555130 <memcpy@plt>
0x555555555dea:      mov    rax,QWORD PTR [rip+0x350f]        # 0x55555555930
...<snip>...
0x555555555f6a:      mov    rax,QWORD PTR [rip+0x347f]        # 0x5555555593f0
0x555555555f71:      mov    rdx,QWORD PTR [rip+0x3480]        # 0x5555555593f8

gef➤  p/x 0x5555555593f8 - 0x555555559300
$2 = 0xf8

# I prefer to do 0x100 since that is the amount of space objdump reports
dump binary memory vm_mem.bin 0x555555559300 0x555555559300+0x100
```

#### Determine Bytecode Order

A consistent method I've found for determining the bytecode order is to observe how the bytes are used and loaded when executing an instruction. This approach works for challenges both with and without symbols.

Returning to level 19, let's examine the first three bytes of the bytecode:

```bash
gef➤  x/3xb 0x0000555555559020
0x555555559020 <vm_code>:       0x20    0x01    0x80
```

We'll set a breakpoint at interpret_instruction and step through the execution until we reach the first and/test instructions:

```bash
0x555555556117 <interpret_instruction+00b9> movzx  eax, BYTE PTR [rbp-0x10]
0x55555555611b <interpret_instruction+00bd> movzx  eax, al
0x55555555611e <interpret_instruction+00c0> and    eax, 0x20
0x555555556121 <interpret_instruction+00c3> test   eax, eax

gef➤  x/xb $rbp-0x10
0x7fffffffde10: 0x20
```

Thus, we know that the first byte is the instruction identifier byte. Next, we'll use the interpret_imm instruction to determine arg1 and arg2. The interpret_imm function performs the following operation:

```
a = b, where a is a register identifier and b is an intermediate value.
```

Set a breakpoint at interpret_imm and step through the execution until we reach write_register, where we know that rsi corresponds to arg1 (the register) and rdx corresponds to value (the immediate).

```bash
gef➤  i r
rax            0x7fffffffde70      0x7fffffffde70
rbx            0x80                0x80
rcx            0x1                 0x1
rdx            0x80                0x80
rsi            0x1                 0x1
```

At this point, we observe that rsi is 0x01 and rdx is 0x80. This gives us the byte order for this level:

| inst | arg1 | arg2 |

## Functions and Registers

This section outlines the functions provided by the Yan85 machine. Yan85 functions and registers are represented by the following immediate values.

```
0x1
0x2
0x4
0x8
0x10
0x20
0x40
0x80 (functions only)
```

The function and register codes change with each challenge. However, consistent methods exist to examine and map these codes to their corresponding functions and registers, regardless of whether the challenge includes symbols.

### Registers

There are several techniques for mapping register codes. This section will explain how each register is used and how its behavior can help identify its corresponding code.

#### a, b, c

These are general-purpose registers, and they are also used as arguments for several functions.

For example, sys_open stores an offset in the 'a' register, which represents the distance from the start of the Memory Segment where the file path is located. The 'b' register stores the flags of the file being opened. The specific registers used for each function will be outlined below.

#### d

The 'd' register is typically used to hold the return status code for function calls. Continuing with the sys_open example, if the file is successfully opened, a file descriptor will be returned. If unsuccessful, -1 will be returned instead.

#### s

#### i

#### f

### Functions

- sym.crash
- sym.describe_flags
- sym.describe_instruction
- sym.describe_register
- sym.interpret_add
- sym.interpret_cmp
- [sym.interpret_imm](#syminterpret_imm)
- sym.interpret_instruction
- sym.interpret_jmp
- sym.interpret_ldm
- sym.interpret_stk
- sym.interpret_stm
- sym.interpret_sys
- sym.interpreter_loop
- sym.read_memory
- sym.read_register
- sym.register_tm_clones
- sym.sys_exit
- sym.sys_open
- sym.sys_read
- sym.sys_sleep
- sym.sys_write
- sym.write_memory
- sym.write_register

#### sym.crash
#### sym.deregister_tm_clones
#### sym.describe_flags
#### sym.describe_instruction
#### sym.describe_register
#### sym.interpret_add
#### sym.interpret_cmp
#### sym.interpret_imm

Assigns an immediate value (arg2) to a register (arg1).

**Psuedo Code**:
```
a = 0x30
```

**Calls**:
- sym.write_register

**Called by**:
- sym.interpret_instruction

#### sym.interpret_instruction
#### sym.interpret_jmp
#### sym.interpret_ldm
#### sym.interpret_stk
#### sym.interpret_stm
#### sym.interpret_sys
#### sym.interpreter_loop
#### sym.read_memory
#### sym.read_register
#### sym.register_tm_clones
#### sym.sys_exit
#### sym.sys_open

Calls the open libc subroutine.



#### sym.sys_read
#### sym.sys_sleep
#### sym.sys_write
#### sym.write_memory
#### sym.write_register