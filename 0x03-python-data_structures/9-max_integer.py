#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if len(my_list) == 0:
        return (None)

    big_num = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big_num:
            big_num = my_list[i]

    return (big_num)
