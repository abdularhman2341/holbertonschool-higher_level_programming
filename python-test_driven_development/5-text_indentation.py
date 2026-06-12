#!/usr/bin/python3
"""
Module to indent text based on specific punctuation marks.
"""

def text_indentation(text):
    """Prints text with 2 new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
        
    skip_space = True
    for char in text:
        if skip_space:
            if char == ' ':
                continue
            else:
                skip_space = False
                
        if not skip_space:
            if char in ".?:":
                print(char)
                print("")
                skip_space = True
            else:
                print(char, end="")
