#!/usr/bin/python3

def uppercase(str):
        for c in str:
                if (ord(c) >= 97 and ord(c) <= 122):
                        print(chr(ord(c) - 32), end="")
                else:
                        print(c, end="")
        print()

uppercase("best")
uppercase("Best School 98 Battery street")

