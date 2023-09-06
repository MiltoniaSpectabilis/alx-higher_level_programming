#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for char in names:
        if char[:2] != "__":
            print(char)
