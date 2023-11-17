"""Example function to learn syntax"""

def my_max(num_1: int, num_2: int) -> int:
    """Returns max out of two numbers"""
    if num_1 >= num_2:
        return num_1
    else:
        return num_2

max_number: int = my_max(1,10)
