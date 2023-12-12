#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if len(my_list) == "":
        return (None)

    big_int = my_list[0]
    for i in my_list:
        if my_list[i] > big_int:
            big_int = my_list[i]

            return (big_int)
