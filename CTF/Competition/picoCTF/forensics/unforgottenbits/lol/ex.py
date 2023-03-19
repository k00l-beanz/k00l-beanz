#!/usr/bin/env python3

base_str = "yasuoaatrox"

champions_lst = [line.strip().lower() for line in open("champions.txt","r")]

for i in champions_lst:
    for j in champions_lst:
        for k in champions_lst:
            for l in champions_lst:
                pass_str = i + j + k + l 
                print(pass_str)