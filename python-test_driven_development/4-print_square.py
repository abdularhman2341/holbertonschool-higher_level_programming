#!/usr/bin/python3
"""
Module to indent text based on specific punctuation.
"""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    skip = True
    for char in text:
        if skip and char == ' ':
            continue
        skip = False

        if char in ".?:":
            print(char)
            print("")
            skip = True
        else:
            print(char, end="")
