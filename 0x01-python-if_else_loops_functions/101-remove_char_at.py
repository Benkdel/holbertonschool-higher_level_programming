#!/usr/bin/python3

def remove_char_at(str, n):
        new_str = ""
        index = 0
        if (n <= 0):
                return(str)
        for c in str:
                if (index != n):
                        new_str = new_str + c
                index += 1
        return (new_str)
