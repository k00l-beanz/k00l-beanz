#!/usr/bin/env python3

def extract_offset(inst: str)-> int:
    return int(inst[5:9], 16)

def hex_to_ascii(byt: str)-> str:
    return chr(int(byt, 16))

assem = [line.strip() for line in open("dump2", "r")]
flag = ["_"] * 100

for i in range(1, len(assem), 2):
    offset_byte = extract_offset(assem[i - 1])
    ascii = hex_to_ascii(assem[i].split(",")[1])
    
    flag[offset_byte] = ascii
print(''.join(flag))