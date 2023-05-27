#!/usr/bin/env python3

import hpack
import binascii

with open("hpack_data.bin", "rb") as f:
    data = f.read()

decoded_data = hpack.Decoder().decode(binascii.hexlify(data))

with open("output.txt", "w") as f:
    f.write(decoded_data.decode())