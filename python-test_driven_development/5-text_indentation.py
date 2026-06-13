#!/usr/bin/python3
"""
Module to indent text based on specific punctuation.
"""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char in "?.:":
                print(char)
                print("")
                flag = 0
            else:
                print(char, end="")
