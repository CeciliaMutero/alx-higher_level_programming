#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for str in my_string:
        if str.lower() not in ('c', 'C'):
            result += str
    return result
