"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730577554"


class Simpy:
    """Simpy Class."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Parameter of list[float], initilize values."""
        self.values = values

    def __str__(self) -> str:
        """No arguments and returns a str."""
        return f"Simpy({self.values})"
    
    def fill(self, fill_value: float, num_values: int) -> None:
        """Fill a Simpys values witha specific number of repeating values."""
        self.values = [fill_value] * num_values

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill values attribute with ranges of values."""
        assert step != 0.0, "Step cannot be 0.0"
        current_value = start
        while (step > 0 and current_value < stop) or (step < 0 and current_value > stop):
            self.values.append(current_value)
            current_value += step
    
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use of addition operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have equal lengths for addition"
            result_values = [x + y for x, y in zip(self.values, rhs.values)]
        else:
            result_values = [x + rhs for x in self.values]
        return Simpy(result_values)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Use of the power operator."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have equal lengths for exponentiation"
            result_values = [x ** y for x, y in zip(self.values, rhs.values)]
        else:
            result_values = [x ** rhs for x in self.values]
        return Simpy(result_values)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return a list[bool], filters Simpy array."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have equal lengths for equality comparison"
            result_values = [x == y for x, y in zip(self.values, rhs.values)]
        else:
            result_values = [x == rhs for x in self.values]
        return result_values
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Test for greater."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values), "Simpy objects must have equal lengths for greater than comparison"
            result_values = [x > y for x, y in zip(self.values, rhs.values)]
        else:
            result_values = [x > rhs for x in self.values]
        return result_values

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Use of subscription operator."""
        if isinstance(rhs, int):
            return self.values[rhs]
        elif isinstance(rhs, list):
            result_values = [x for i, x in enumerate(self.values) if rhs[i]]
            return Simpy(result_values)
        else:
            raise TypeError("Unsupported subscription type. Must be int or list[bool]")