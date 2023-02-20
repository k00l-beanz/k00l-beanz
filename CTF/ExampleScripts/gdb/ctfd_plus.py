#!/usr/bin/env python3

import gdb

def gdb_run(flag: str)-> None:
	with open('_cracking', 'w') as f:
		f.write(flag)

	gdb.execute("run < _cracking")

breakAddress = 0x555555555110

flagLength = 0x2f
flag = [" "] * flagLength

gdb.execute("break *{}".format(breakAddress))

for i in range(flagLength):
	print("Flag: {}".format(''.join(flag)))
	gdb_run(''.join(flag))
	val = int(gdb.parse_and_eval("${}".format("al")))
	flag[i] = chr(val)
