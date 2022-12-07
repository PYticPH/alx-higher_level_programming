#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not key:
        return (a_dictionary)
    a_dictionary.setdefault(key, value)
    return (a_dictionary)
