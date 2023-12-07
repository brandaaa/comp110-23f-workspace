"""Working with CSV data. """

from csv import DictReader 

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = Dictreader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 