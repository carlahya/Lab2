"""
SNIPPET 2 — Open/Closed Principle (OCP)

Smell: every time we add a new shape we must crack open area() and add
another 'if'. The function is NOT closed for modification.

Your job (via the AI harness):
  Refactor so a new shape can be added WITHOUT editing existing code
  (hint: polymorphism / a common interface). Then add a Triangle to prove it.
"""

# pylint: disable=too-few-public-methods

import math
from dataclasses import dataclass
from typing import Protocol


class Shape(Protocol):
    """Common interface for shapes that can calculate their area."""

    def area(self):
        """Return this shape's area."""


@dataclass
class Circle:
    """Circle shape."""

    radius: float

    def area(self):
        """Return the circle area."""
        return math.pi * self.radius**2


@dataclass
class Rectangle:
    """Rectangle shape."""

    width: float
    height: float

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height


@dataclass
class Square:
    """Square shape."""

    side: float

    def area(self):
        """Return the square area."""
        return self.side * self.side


@dataclass
class Triangle:
    """Triangle shape."""

    base: float
    height: float

    def area(self):
        """Return the triangle area."""
        return self.base * self.height / 2


def total_area(shape_items):
    """Return the combined area of all shapes."""
    return sum(shape.area() for shape in shape_items)


if __name__ == "__main__":
    shapes = [
        Circle(radius=2),
        Rectangle(width=3, height=4),
        Square(side=5),
    ]
    print("Total area:", total_area(shapes))
