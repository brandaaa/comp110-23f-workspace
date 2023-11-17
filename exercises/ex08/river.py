"""File to define River class."""
__author__ = "730577554"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River class."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removes animals as they age."""
        new_fish = []
        new_bears = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.fish = new_fish
        self.bears = new_bears

    def bears_eating(self):
        """Simulate Bears eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self):
        """Removes bears from river if they have 0 hunger score."""
        new_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears

    def repopulate_fish(self):
        """Repopulate Fish."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Repopulate Bears."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())   

    def view_river(self) -> None:
        """Prints fish and bear population."""
        x = self.day
        y = len(self.fish)
        z = len(self.bears)
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {y}")   
        print(f"Bear population: {z}")  

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove amount fish from river."""
        for _ in range(min(amount, len(self.fish))):
            self.fish.pop(0)

                
