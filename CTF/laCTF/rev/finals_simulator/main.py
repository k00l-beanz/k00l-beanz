#!/usr/bin/env python3

def hexStrToDec(enc: list)-> list:
    return [int(enc[i], 16) for i in range(len(enc))]

enc = ["0E","C9", "9D", "B8", "26", "83", "26", "41", "74", "E9", "26", "A5", "83", "94", "0E", "63", "37", "37", "37"]
enc = hexStrToDec(enc)

flag = ""
for i in range(len(enc)):
    for j in range(256):
        x = (j * 17) % 253
        if x == enc[i]:
            flag += chr(j)
            break

print(flag)