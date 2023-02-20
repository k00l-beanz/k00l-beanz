#!/usr/bin/env python3

from pwn import *
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="", description="")
	parser.add_argument("-l", "--local", action="store_true")
	parser.add_argument("-r", "--remote", action="store_true")
	args = parser.parse_args()

	if args.local:
		proc = process([""])
	elif args.remote:
		proc = process(["nc", "", ""])
	else:
		print("[!] Use either --local or --remote")
		exit()

	# context.log_level = "debug"

	info("sending first payload")
	proc.sendlineafter(b"end of string", b"send line")
	proc.recvuntil(b"receive data until delim", drop=True)

	leak = int(proc.recvlineS(), 16)

	info("leaked address: %#x", leak)

	proc.sendlineafter(b"", b"")
	proc.sendlineafter(b'', flat(leak))

	warn(proc.recvlines(2)[1].decode())