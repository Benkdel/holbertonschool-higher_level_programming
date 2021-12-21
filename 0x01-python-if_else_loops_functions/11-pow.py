#!/usr/bin/python3

def pow(a, b):
    result = 1
    if (b == 0):
        return (result)

    # if b is negative, convert into decimal and set b into positive
    if (b < 0):
        a = 1 / a
        b *= -1

    for i in range(0, b):
        result *= a
    return (result)
