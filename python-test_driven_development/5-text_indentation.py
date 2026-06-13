#!/usr/bin/python3
"""
Module to indent text based on specific punctuation.
"""


def text_indentation(text):
    """Prints text with 2 new lines after ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    text_len = len(text)

    
    while i < text_len and text[i] == ' ':
        i += 1

    while i < text_len:
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            
            while i < text_len and text[i] == ' ':
                i += 1
            continue
        i += 1
