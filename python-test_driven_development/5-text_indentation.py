#!/usr/bin/python3
"""
Module to indent text based on specific punctuation.
"""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    skip_space = True
    for char in text:
        if char == " " and skip_space:
            continue

        skip_space = False
        print(char, end="")

        if char in ".?:":
            print("\n")
            skip_space = True
