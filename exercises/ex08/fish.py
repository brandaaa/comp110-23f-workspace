"""File to define Fish class."""


class Fish:
    """Fish class."""
    age: int

    def __init__(self):
        """Initialize fish age."""
        self.age: int = 0
    
    def one_day(self):
        """Adds fish age."""
        self.age += 1