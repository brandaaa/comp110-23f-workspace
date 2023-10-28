"""Combining two lists into a dictionary."""
__author__ = "730577554"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Inputs a string list and int list that are zipped into a dictionary."""
    if len(str_list) != len(int_list) or len(str_list) == 0:
        return {}
    result_dict = {}
    for i in range(len(str_list)):
        result_dict[str_list[i]] = int_list[i]
    return result_dict