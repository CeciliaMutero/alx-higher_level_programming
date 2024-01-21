#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        char_upper = chr(ord(char) - ord('a') + ord('A'))
        if 'a' <= char <= 'z':
            result += char_upper
        else:
            result += char
    print("{}".format(result))
