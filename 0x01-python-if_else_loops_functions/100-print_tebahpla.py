#!/usr/bin/python3

lower = 122
upper = 89

for i in range(0, 26):
    if (i % 2 == 0):
        print(chr(lower), end="")
        lower -= 2
    else:
        print(chr(upper), end="")
        upper -= 2
