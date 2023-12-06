#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element at a specific position in a list
    without modifying the original list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    copy_list = my_list[:idx]
    copy_list.append(element)
    copy_list = copy_list + my_list[idx + 1:]
    return copy_list
