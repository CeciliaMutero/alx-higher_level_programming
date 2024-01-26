#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        is_even_number = i % 2 == 0
        new_list.append(is_even_number)
    return new_list
