#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 122):
            conv = 32
        else:
            conv = 0
        print(chr(ord(c) - conv), end="")
    print()
