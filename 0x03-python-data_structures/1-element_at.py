#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if (idx < 0):
        return ('None')
    if (idx > list_len):
        return ('None')
    for index in range(0, list_len - 1):
        if (index == idx):
            return (my_list[index])
