#!/usr/bin/env python3

import argparse

def invokeWebRequest(args: argparse.Namespace)-> None:
    
    placeKeys = [5,25,8,7,0,14,3,21,2,22,15,16,31,28,11,26,17,23,27,29,10,1,6,24,30,18,13,19,12,9,20,4]
    placeVals = ["B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","_","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","_","l","Y","C","U"]

    decodeUrl = str()
    
    for key in placeKeys:
        decodeUrl += placeVals[key]
    
    print(decodeUrl)

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="deobf.py", description="deobfuscate the web-request from 'UrgentPayment.doc'")
    parser.add_argument("-iwr", "--iwr", required=True, action="store_true")
    args = parser.parse_args()

    if args.iwr:
        invokeWebRequest(args)
