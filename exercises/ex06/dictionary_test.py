"""Dictionary test."""
__author__ = "730577554"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_use_case_1():
    """Test invert function with use case."""
    input_dict = {'a': '1', 'b': '2', 'c': '3'}
    expected_output = {'1': 'a', '2': 'b', '3': 'c'}
    assert invert(input_dict) == expected_output


def test_invert_use_case_2():
    """Test invert function with different set."""
    input_dict = {'apple': 'one', 'banana': 'two', 'kiwi': 'three'}
    expected_output = {'one': 'apple', 'two': 'banana', 'three': 'kiwi'}
    assert invert(input_dict) == expected_output


def test_invert_edge_case():
    """Test invert function with unexpected use case (duplicate values)."""
    input_dict = {"a": "apple", "b": "banana", "c": "apple"}
    with pytest.raises(KeyError, match="Duplicate key encountered: apple"):
        invert(input_dict)


def test_favorite_color_use_case_1():
    """Test favorite_color function with use case."""
    color_dict = {'Owen': 'blue', 'Kennedy': 'green', 'Daniel': 'blue', 'Gabriel': 'red'}
    expected_color = 'blue'
    assert favorite_color(color_dict) == expected_color


def test_favorite_color_use_case_2():
    """Test favorite_color function with different set."""
    color_dict = {'Gabriel': 'green', 'Daniel': 'red', 'Owen': 'red', 'Kennedy': 'blue'}
    expected_color = 'red'
    assert favorite_color(color_dict) == expected_color


def test_favorite_color_edge_case():
    """Test favorite_color function with empty input."""
    color_dict = {}
    expected_output = None
    assert favorite_color(color_dict) == expected_output, "Expected output not returned for favorite_color function with empty input dict"


def test_count_use_case_1():
    """Test count function with use case."""
    input_list = ['apple', 'banana', 'apple', 'kiwi', 'banana', 'banana']
    expected_output = {'apple': 2, 'banana': 3, 'kiwi': 1}
    assert count(input_list) == expected_output


def test_count_use_case_2():
    """Test count function with different set."""
    input_list = ['red', 'green', 'blue', 'green', 'yellow', 'red']
    expected_output = {'red': 2, 'green': 2, 'blue': 1, 'yellow': 1}
    assert count(input_list) == expected_output


def test_count_edge_case():
    """Test count function with an empty list (edge case)."""
    input_list = []
    assert count(input_list) == {}


def test_alphabetizer_use_case_1():
    """Test alphabetizer function with use case."""
    words_list = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
    expected_output = {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
    assert alphabetizer(words_list) == expected_output


def test_alphabetizer_use_case_2():
    """Test alphabetizer function with different set."""
    words_list = ['cat', 'dog', 'elm', 'kangaroo', 'kiwi']
    expected_output = {'c': ['cat'], 'd': ['dog'], 'e': ['elephant'], 'k': ['kangaroo', 'kite']}
    assert alphabetizer(words_list) == expected_output


def test_alphabetizer_edge_case():
    """Test alphabetizer function with an empty list (edge case)."""
    words_list = []
    assert alphabetizer(words_list) == {}


def test_update_attendance_use_case_1():
    """Test update_attendance function with use case."""
    attendance_dict = {'Monday': ['Gabriel', 'Owen'], 'Tuesday': ['Kennedy']}
    day = 'monday'
    student = 'david'
    expected_output = {'Monday': ['Gabriel', 'Owen', 'David'], 'Tuesday': ['Kennedy']}
    assert update_attendance(attendance_dict, day, student) == expected_output


def test_update_attendance_use_case_2():
    """Test update_attendance function with different set."""
    attendance_dict = {'Monday': ['Owen'], 'Wednesday': []}
    day = 'Wednesday'
    student = 'Gabriel'
    expected_output = {'Monday': ['Owen'], 'Wednesday': ['Gabriel']}
    assert update_attendance(attendance_dict, day, student) == expected_output


def test_update_attendance_edge_case():
    """Test update_attendance function with a new day (edge case)."""
    attendance_dict = {'Monday': ['Kennedy'], 'Tuesday': []}
    day = 'Wednesday'
    student = 'Daniel'
    expected_output = {'Monday': ['Kennedy'], 'Tuesday': [], 'Wednesday': ['Daniel']}
    assert update_attendance(attendance_dict, day, student) == expected_output
