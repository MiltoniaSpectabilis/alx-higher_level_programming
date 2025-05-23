#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    num_args = len(argv[1:])
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(argv[1:], 1):
            print("{}: {}".format(i, arg))
