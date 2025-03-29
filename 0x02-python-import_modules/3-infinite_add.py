#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    sum_result = 0
    for arg in argv[1:]:
        sum_result += int(arg)
    print(sum_result, end='')
