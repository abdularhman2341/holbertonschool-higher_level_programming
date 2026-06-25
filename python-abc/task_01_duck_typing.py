#!/usr/bin/env python3
"""Module that defines a Shape interface and uses duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a Shape."""
    
    @abstractmethod
    def area(self):
        """Abstract method to calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter."""
        pass


class Circle(Shape):
    """Class representing a Circle."""
    
    def __init__(self, radius):
        """Initialize the Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Calculate the perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Class representing a Rectangle."""
    
    def __init__(self, width, height):
        """Initialize the Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
