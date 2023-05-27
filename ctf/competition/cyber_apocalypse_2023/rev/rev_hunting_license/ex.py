#!/usr/bin/env python3

def second():
    t = ["30","77","54","64","72","30","77","73","73","34","50"]
    t.reverse()

    second_password = list()

    for i in range(len(t)):
        c = chr(int(t[i], 16))
        second_password.append(c)

    print(''.join(second_password))

def third():
    t2 = ["47","7b","7a","61","77","52","7d","77","55","7a","7d","72","7f","32","32","32","13"]

    ascii_xor_key = list()

    for t in t2:
        ascii_xor_key.append(chr(int(t, 16)))

    print(''.join(ascii_xor_key))
third()