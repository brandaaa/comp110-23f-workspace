"""Methods and functions."""

from __future__ import annotations


class Point:
    """Creating point class."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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