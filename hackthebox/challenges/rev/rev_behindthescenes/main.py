#!/usr/bin/env python3

f = open("behindthescenes", "rb")
s = f.read()
for c in s:
    print(c)

f.close()
