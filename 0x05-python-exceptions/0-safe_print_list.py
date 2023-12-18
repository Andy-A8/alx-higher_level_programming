#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x number of elements of a list"""
    fig = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            fig = fig + 1
        except IndexError:
            break
    print("")
    return (fig)
