#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return list(map(lambda x: replace if x == search else x, my_list))

    # for i, item in enumerate(my_list):
    #     if item == search:
    #         my_list[i] = replace
    # return my_list
