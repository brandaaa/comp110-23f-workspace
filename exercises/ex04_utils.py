"""Using list!"""
__author__ = "730577554"


def all(int_list: int, num_match: int ) -> bool:
    """Returns True if the numbers in the list match the number of the second parameter, target number"""
    if len(int_list) == 0:  # Checks if the list is empty
        return False
    index = 0
    while index < len(int_list):  # Goes through the indexes, check if current index is equal to num_match
        if int_list[index] != num_match:
            return False
        index += 1
    return True  # Returns True if all indexes matched with the num_match


def max(input: list[int]) -> int:
    """Returns the max number of a list"""
    if len(input) == 0:  # Checks if list is empty
        raise ValueError("max() arg is an empty list")
    max_num: int = input[0]  # Current max number is the first index
    index = 1
    while index < len(input):  # Updates max number by checking if current number is greater than current max
        if input[index] > max_num:
            max_num = input[index]
        index += 1
    return max_num  # Returns the max number


def is_equal(list1: int, list2: int) -> bool:
    """Returns True if numbers in the first list match the numbers of the second list"""
    if len(list1) != len(list2):  # Checks if both list are same length
        return False
    index = 0
    while index < len(list1):  # Check if the pairs are equal, if not, function returns false
        if list1[index] != list2[index]:
            return False
        index += 1

    return True  # Returns true if loop completes with all indexes matching
