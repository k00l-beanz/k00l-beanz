#!/usr/bin/env python3

java_code = """
0)  == 'd'
29) == 'a' &&
4)  == 'r'
2)  == '5'
23) == 'r' &&
3)  == 'c'
17) == '4' &&
1)  == '3'
7)  == 'b'
10) == '_' &&
5)  == '4'
9)  == '3'
11) == 't' &&
15) == 'c' &&
8)  == 'l'
12) == 'H' &&
20) == 'c' &&
14) == '_' &&
6)  == 'm'
24) == '5' &&
18) == 'r' &&
13) == '3' &&
19) == '4' &&
21) == 'T' &&
16) == 'H' &&
27) == '6' &&
30) == 'f' &&
25) == '_' &&
22) == '3' &&
28) == 'd' &&
26) == 'f' &&
31) == '4';
"""

flag = []
for _ in range(32):
    flag.append('_')

sp = java_code.split('\n')
for s in sp:
    pos = s.split(')')[0]

    ch = s.split("'")
    if len(ch) <= 1:
        continue
    
    print(pos, ch[1])
    flag[int(pos)] = ch[1]


print("picoCTF{" + ''.join(flag) + '}')