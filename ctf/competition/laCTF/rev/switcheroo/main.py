#!/usr/bin/env python3

import gdb
import string

break_addr = 0x00401073
passlen = 0x40

code = ["_"]*passlen
printable = string.printable[:-5]

def gdb_run_with_stdin(pwd):
	with open('_cracking','w') as f:
		f.write(pwd)

	gdb.execute('run < _cracking')

def read_reg(reg):
	return gdb.parse_and_eval("${}".format(reg))

def gdb_continue():
	gdb.execute('continue')


gdb.execute("break *{}".format(break_addr))

errors = -1

for trial in range(passlen):

	for c in range(0x21, 0x7F):
		code[trial] = chr(c)

		print("trying: %s" % ''.join(code))
		gdb_run_with_stdin(''.join(code))
		res = int(read_reg("r12"))
		if errors == -1:
			errors = res
			continue

		if res > errors:
			errors = res

		gdb_continue()
		if res < errors:
			print("Found: %s" % ''.join(code))
			errors = res
			break

print(''.join(code))