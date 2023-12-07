"""Dictionary related utility functions."""

__author__ = "730577554"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_vals(table, key)
    return result


def head(table: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Produce column-based table with only first parameter."""
    result: dict[str, list[str]] = {}
    for key in table:
        item_list: list[str] = []
        for elems in table[key]:
            if len(item_list) < rows:
                item_list.append(elems)
        result[key] = item_list
    return result


def select(column_data: dict[str, list[str]], selected_columns: list[str]) -> dict[str, list[str]]:
    """Produce column-based table with only specific subset."""
    result: dict[str, list[str]] = {}
    for column_name in selected_columns:
        result[column_name] = column_data[column_name]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key1 in table1:
        result[key1] = table1[key1]
    for key2 in table2:
        if key2 in result:
            result[key2] = result[key2] + table2[key2]
        else:
            result[key2] = table2[key2]
    return result


def count(values: list[str]) -> dict[str, int]:
    """Count of the number of appearance."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result