#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ''' initialize new dictionary '''
    b_dict = dict()
    key_list = list(a_dictionary.keys())
    for k in key_list:
        b_dict[k] = a_dictionary.get(k) * 2
    return (b_dict)
