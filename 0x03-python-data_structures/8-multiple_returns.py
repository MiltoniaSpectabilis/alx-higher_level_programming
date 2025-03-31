#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == '':
        empty = (0, None)
        return empty

    my_tuple = len(sentence), sentence[0]
    return my_tuple
