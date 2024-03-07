#!/usr/bin/env python3

while True:
    user_input = input("> ")
    if "win" in user_input:
        print("filter")
        continue

    try:
        eval(user_input + "()")
    except Exception as e:
        print(e)