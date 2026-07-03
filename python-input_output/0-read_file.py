#!/usr/bin/python3
"""Module for reading a text file and printing to stdout."""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    
    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
