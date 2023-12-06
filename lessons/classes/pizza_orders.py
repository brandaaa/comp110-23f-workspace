"""Instantiating a class."""
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True)
#my_pizza.size = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True

#print(my_pizza)

#print("Pizza: ")
#print(Pizza)

print("Size Attribute: ")
print(my_pizza.size)

print("Toppings: ")
print(my_pizza.toppings)

sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        price += 1.00
    return price

print(price(sals_pizza))
print(price(my_pizza))
print(sals_pizza.price)
print(my_pizza.price)

my_pizza.add_toppings(2)
print(my_pizza.toppings)
print(my_pizza.price())