#!/usr/bin/env python3

import sys
import subprocess
from pwn import *

context.log_level = "debug"

r = remote("jupiter.challenges.picoctf.org", 35856)
rand_nums_output = subprocess.run(["./main", sys.argv[1]], capture_output=True)
rand_nums = rand_nums_output.stdout.decode().split("\n")[:-1]

print(rand_nums)

for num in rand_nums:
	r.recvuntil(b"Guess the height: ")
	num = bytes(num, 'utf-8')
	r.sendline(num)