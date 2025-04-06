#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_div = []
    i = 0
    try:
        for i in range(list_length):
            try:
                res_div.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                print("wrong type")
                res_div.append(0)
            except ZeroDivisionError:
                print('division by 0')
                res_div.append(0)
            except IndexError:
                print("out of range")
                res_div.append(0)
    finally:
        return res_div
