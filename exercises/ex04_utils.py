"""Using list!"""
__author__ = "730577554"


def all(int_list: int, num_match: int ) -> bool:
    if len(int_list) == 0:
        return False
    index = 0
    while index < len(int_list):
        if int_list[index] != num_match:
            return False
        index += 1
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    max_num: int = input[0]
    index = 1
    while index < len(input):
        if input[index] > max_num:
            max_num = input[index]
        index += 1
    return max_num

def is_equal(list1: int, list2: int) -> bool:
    if len(list1) != len(list2):
        return False
    index = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            return False
        index += 1

    return True
