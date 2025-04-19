#!/usr/bin/python3
"""
This module takes arguments, stores them in a list
and then serializes it
"""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# initialize an empty list that will receive the args
arg_list = []

# load existing content from the file into our list
# this makes sure that if there is an existing content
# it does not get overwritten
arg_list = load_from_json_file("add_item.json")

# loop through the args
for arg in argv[1:]:
    # append the args to the list
    arg_list.append(arg)

# serialize the list of args and save them into a var
save_to_json_file(arg_list, "add_item.json")
