"""File to define Bear class."""


class Bear:
    """Bear class."""
    age: int 
    hunger_score: int
    
    def __init__(self):
        """Initialize age and hunger."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Add age to bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Update the Bears hunger score and num fish."""
        self.hunger_score += num_fish
