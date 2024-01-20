#!/usr/bin/python3
def uppercase(str):
    for char in range str:
        if 'a' <= char <= 'z':
            char_upper = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(char_upper))
        else:
            print("{}".formst(char))
