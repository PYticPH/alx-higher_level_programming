#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    max_key, max_int = None, None
    for key, value in a_dictionary.items():
        if max_int == None or value > max_int:
            max_key, max_int = key, value
    return (max_key)
