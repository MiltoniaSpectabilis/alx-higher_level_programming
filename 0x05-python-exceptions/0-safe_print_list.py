#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        if x >= 0:
            for element in my_list[:x]:
                print(element, end='')
                count += 1
    except (ValueError, TypeError):
        pass
    print()
    return count
