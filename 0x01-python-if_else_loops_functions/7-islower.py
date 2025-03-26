#!/usr/bin/python3
def islower(c):
    char_code = ord(c)
    a_code = ord('a')
    z_code = ord('z')

    if a_code <= char_code <= z_code:
        return True
    else:
        return False
