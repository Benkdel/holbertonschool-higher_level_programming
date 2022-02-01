#!/usr/bin/python3
"""
    Task 0 - Mandatory
"""


def read_file(filename=""):
    """
        Reads file and prints it to stdout
    """
    with open(filename, mode="r", encoding="utf-8") as recFile:
        print(recFile.read())
    recFile.close()
