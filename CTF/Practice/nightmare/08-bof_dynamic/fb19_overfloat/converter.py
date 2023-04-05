#!/usr/bin/env python3

import struct

value = struct.pack("<f", 0x400a83)

ascii_str = "".join([chr(b) for b in value])

print(ascii_str)