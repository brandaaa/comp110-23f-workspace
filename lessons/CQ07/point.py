"""Methods and functions."""

from __future__ import annotations


class Point:
    """Creating point class."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Defining constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutating a point."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Creating new point."""
        return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:
        """Return a string representation of the Point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Overload the * operator."""
        return Point(self.x * factor, self.y * factor)

    def __add__(self, factor: int | float) -> Point:
        """Overload the + operator."""
        return Point(self.x + factor, self.y + factor)