#!/usr/bin/env python3

def extractEle(line: str)-> str:
    return line.split("[")[-1].split("]")[0]

def main():

    for line in open("dump1", "r"):
        line = line.strip()
        
        if ("movzx" in line):
            ele = extractEle(line)
            print(ele)


if __name__=="__main__":
    main()

"""
{
    "rbp-0x6b":[
        {
            "rbp-0x
        }
    ]{
        "rbp-0x50":"mult",
        "rbp-0x63":"cmp",
        
    },
    "rbp-0x50":{
        "rbp-0x6b":"mult"
    },
    "rbp-0x63":{
        "rbp-0x6b":"cmp"
    }
}
"""