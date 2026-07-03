#!/usr/bin/python3
"""Module that returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: Dictionary representation of the object.
    """
    return obj.__dict__
