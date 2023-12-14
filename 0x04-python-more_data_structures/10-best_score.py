#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if a_dictionary is None:
        return (None)

    biggest = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == biggest:
            return (key)
