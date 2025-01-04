# Yan85 Manual

## Function Descriptions

### sym.interpret_imm
arg1 = register
arg2 = value

### sym.interpret_stm
arg1 = register containing memory offset to write
arg2 = register containing value to write

### sym.interpret_ldm
arg1 = register to write to
arg2 = register containing memory offset to read

### sym.interpret_stk
arg1 = pop register
arg2 = push register

- push occurs before pop

### sym.interpret_add
arg1 = register1
arg2 = register2

- Sum is written into register1

### sym.interpret_cmp
arg1 = reg1
arg2 = reg2

### sym.interpret_sys
op = 0x08
arg1 = syscall id
arg2 = return value register

- read_code
- read_memory
    - 'a' register contains fd to read from
    - 'b' register contains offset in memory to read into
    - 'c' register contains the number of bytes to read
- write
    - 'a' register contains the fd to write to
    - 'b' register contains the *buf which will be written to fd
    - 'c' register contains the number of bytes to write
- open
    - 'a' register contains the offset in memory to read the path to the file being opened
    - 'b' register contains the flags
    - 'b' register contains the mode
- sleep


### sym.sys_read
rdi = baseAddr
rsi = file descriptor
rdx = *buf
rcx = nbyte

### sym.sys_write
### sym.sys_open


### sym.interpret_jmp
arg1 = flag
arg2 = jmp location

### sym.describe_flags
rdi = flags
0x0     *
0x1     L - larger
0x2     Z - zero
0x4     E - equal
0x8     G - greater
0x10    N - not equal



