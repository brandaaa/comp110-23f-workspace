"""Combining two lists into a dictionary"""
__author__ = "730577554"


def zip(str_list: list[str], int_list: list[int]) -> dict[str,int]:
    """Inputs a string list and int list that are zipped into a dictionary"""
    if len(str_list) != len(int_list) or not str_list:
        return ()
    result = dict(zip(str_list, int_list))
    return result