#!/usr/bin/python3

def uppercase(str):
    conv = 0
    for c in str:
        """ ASCII code convert ord(c) """
        if (ord(c) >= 97 and ord(c) <= 122):
            conv = 32
        else:
            conv = 0
        print(chr(ord(c) - conv), end="")
    print()
