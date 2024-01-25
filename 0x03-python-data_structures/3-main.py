#!/usr/bin/python3
from importlib import import_module

module_name = '3-print_reversed_list_integer'
module = import_module(module_name)
print_reversed_list_integer = module.print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
