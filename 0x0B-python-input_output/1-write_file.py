#!/usr/bin/python3
"""
    Task 1 - Mandatory
"""


def write_file(filename="", text=""):
    """
        Write text into filename
        Returns:
            number of characters written
    """
    num_chars = 0
    with open(filename, mode="w", encoding="utf-8") as dest_file:
        num_chars = dest_file.write(text)
    dest_file.close()

    return (num_chars)
