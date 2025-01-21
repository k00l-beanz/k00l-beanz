#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(prog="convert.py", description="Convert ascii hex to raw bytes")
parser.add_argument("-l", "--leaked", required=True, help="Path to leaked ascii hex file")
parser.add_argument("-o", "--output", required=True, help="Output raw bytes to file")
args = parser.parse_args()

def main()-> None:

    with open(args.leaked, 'r') as f:
        ascii_data = f.read()

    raw_data = bytes.fromhex(ascii_data)

    with open(args.output, 'wb') as f:
        f.write(raw_data)


if __name__ == "__main__":
    main()