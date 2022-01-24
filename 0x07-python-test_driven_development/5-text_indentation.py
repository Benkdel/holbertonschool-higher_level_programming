#!/usr/bin/python3
"""
    Task 5 - Mandatory
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of the characters:
        ".", "?", ":"
    """
    if type(text) is not str:
        TypeError("text must be a string")
    line = ""
    for _char in text:
        line = line + _char
        if (_char) in [".", "?", ":"]:
            print(line.strip(), end="\n\n")
            line = ""
    print(line.strip())
