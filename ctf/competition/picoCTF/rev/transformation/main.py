#!/usr/bin/env python3

"""
e7 81 a9 e6 8d af e4 8d 94 e4 99 bb e3 84 b6 e5 bd a2 e6 a5 b4 e7 8d 9f e6 a5 ae e7 8d b4 e3 8c b4 e6 91 9f e6 bd a6 e5 bc b8 e5 bc b7 e3 95 a4 e3 90 b8 e3 a4 b8 e6 89 bd
"""

flag_bytes = ['e7', '81', 'a9', 'e6', '8d', 'af', 'e4', '8d', '94', 'e4', '99', 'bb', 'e3', '84', 'b6', 'e5', 'bd', 'a2', 'e6', 'a5', 'b4', 'e7', '8d', '9f', 'e6', 'a5', 'ae', 'e7', '8d', 'b4', 'e3', '8c', 'b4', 'e6', '91', '9f', 'e6', 'bd', 'a6', 'e5', 'bc', 'b8', 'e5', 'bc', 'b7', 'e3', '95', 'a4', 'e3', '90', 'b8', 'e3', 'a4', 'b8', 'e6', '89', 'bd']
flag = [bytes.fromhex(b).decode("utf-8") for b in flag_bytes]
print(flag)
#res = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
