"""Test my zip function."""
__author__ = "730577554"


from lessons.zip import zip


def test_edge_case() -> None:
    """Test zip function if there is an empty input lists."""
    str_list: list[str] = []
    int_list: list[int] = []
    result = zip(str_list, int_list)
    assert result == {}


def test_use_case1() -> None:
    """Test zip function if there is valid input lists."""
    str_list: list[str] = ["Python", "Java", "HTML"]
    int_list: list[int] = [1, 2, 3]
    result = zip(str_list, int_list)
    assert result == {}


def test_use_case2() -> None:
    """Test zip function with input lists of different lengths."""
    str_list: list[str] = ["Peanut", "Almond", "Walnut"]
    int_list: list[int] = [1, 2]
    result = zip(str_list, int_list)
    assert result == {}