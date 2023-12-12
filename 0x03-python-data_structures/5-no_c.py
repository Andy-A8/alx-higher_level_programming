#!/usr/bin/pyhton3
def no_c(my_string):
    new_str = ""
    """Remove all c and C characters from a string"""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_str += i

    return (new_str)
