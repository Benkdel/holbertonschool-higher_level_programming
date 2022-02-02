#!/usr/bin/python3
"""
   Task 7 - Mandatory 
"""

import sys
import os


save_file = __import__("5-save_to_json_file").save_to_json_file
load_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
my_list = []

if os.path.exists(filename):
    my_list = load_file(filename)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, filename)
