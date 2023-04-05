#!/usr/bin/env python3

import os
import re
import argparse
import xml.etree.ElementTree as ET

def main(args: argparse.Namespace)-> None:

    """ tree = ET.parse(args.file)
    root = tree.getroot()
    for child in root:
        print(child[0][2].tag) """

    for line in open(args.file,'r'):
        line = line.strip()

        match = re.search(r"/<Binary>([^<]+)<\/Binary>/", line)


    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a series of XML files")
    parser.add_argument("-f", "--file", required=True)
    args = parser.parse_args()
    main(args)