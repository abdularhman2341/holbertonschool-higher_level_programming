# Python - Abstract Base Classes and Advanced OOP

This directory contains various Python scripts exploring advanced Object-Oriented Programming (OOP) concepts. 

## Key Concepts Covered:
* **Abstract Base Classes (ABC):** Defining blueprints for derived classes to enforce method implementations.
* **Duck Typing & Interfaces:** Utilizing polymorphism based on object behavior rather than explicit inheritance.
* **Built-in Extension:** Subclassing and extending the behavior of built-in Python objects like `list`.
* **Custom Iterators:** Creating classes that hook into Python's iteration protocol (`__next__`) while maintaining internal state.
* **Multiple Inheritance:** Inheriting from multiple parent classes and understanding Method Resolution Order (MRO).
* **Mixins:** Modularizing functionality into dedicated mixin classes for flexible composition without rigid hierarchies.

## Files Description:
* `task_00_abc.py`: Implements an abstract `Animal` class and concrete subclasses (`Dog`, `Cat`).
* `task_01_duck_typing.py`: Explores duck typing through a `Shape` interface with `Circle` and `Rectangle` implementations.
* `task_02_verboselist.py`: Custom `VerboseList` class extending built-in lists with notifications on mutation.
* `task_03_countediterator.py`: A `CountedIterator` that tracks the number of iterated items.
* `task_04_flyingfish.py`: Demonstrates multiple inheritance using `Fish`, `Bird`, and `FlyingFish`.
* `task_05_dragon.py`: Uses `SwimMixin` and `FlyMixin` to compose a `Dragon` class.
