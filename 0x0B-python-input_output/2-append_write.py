#!/usr/bin/python3
"""
    Task 2 - Mandatory
"""


def append_write(filename="", text=""):
    """
        Appends string "text" at end of file "filename"
        Returns:
            num chars added
    """
    with open(filename, mode="a", encoding="utf-8", ) as dest_file:
        num_chars = dest_file.write(text)
    dest_file.close()

    return (num_chars)
