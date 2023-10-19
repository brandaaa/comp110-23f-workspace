"""Summing the elements of a list using different loops."""
__author__ = "730577554"


def w_sum(vals: list[float]) -> float: 
    """Returns the sum of given list of float numbers."""
    total: float = 0.0
    index: int = 0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:  
    """Returns the sum of given list using for loop."""
    total: float = 0.0
    for value in vals:
        total += value 
    return total


def f_range_sum(vals: list[float]) -> float:  
    """Returns the sum of given list using for loop."""
    total: float = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total