"""Defining a class."""

from __future__ import annotations
class Pizza:

    size: str  
    topping: int
    gluten_free: bool

    def __init__(self, input_size: str, input_toppings: int, input_gf: bool):
        self.size = input_size
        self.toppings = input_toppings
        self.gluten_free = input_gf

    def price(self) -> float:
        if self.size == "large":
            price: float = 6.25
        else:
            price: float = 5.00
            price += .75 * self.toppings
        if self.gluten_free:
            price += 1.00
        return price

    def add_toppings(self, num_toppings: int):
        self.toppings += num_toppings

    def
