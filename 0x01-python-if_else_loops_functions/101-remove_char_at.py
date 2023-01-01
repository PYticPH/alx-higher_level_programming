#!/usr/bin/python3

def remove_char_at(str, n):
    """ Function to copy a string and remove a character at n position """

    newStr = ""

    for num in range(len(str)):
        if (num != n):
            newStr += str[num]
    return (newStr)
