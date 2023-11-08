
"""Function skeletons."""
__author__ = "730577554"


def invert(input_dict: dict[str, str]) -> dict[str, str]: 
    """Initialize empty dictionary."""
    output_dict = {}
    for key, value in input_dict.items():
        if value in output_dict:
            raise KeyError(f"Duplicate key encountered: {value}")
        output_dict[value] = key
    return output_dict


def favorite_color(color_dict: dict[str, str]) -> str:  
    """Dictionary to store color."""
    color_count: dict[str, int] = {}
    for color in color_dict.values():
        color_count[color] = color_count.get(color, 0) + 1
    most_popular_color = max(color_count, key=color_count.get)
    return most_popular_color


def count(input_list: list[str]) -> dict[str, int]:  
    """Establish an empty dictionary to store the counts."""
    result_dict: dict[str, int] = {}
    for item in input_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict  


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]: 
    """Initialize an empty dictionary to store the categorized words."""
    alphabet_dict: dict[str, list[str]] = {} 
    for word in words_list:
        first_letter = word[0].lower()
        if first_letter in alphabet_dict:
            alphabet_dict[first_letter].append(word)
        else:
            alphabet_dict[first_letter] = [word]
    return alphabet_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance dictionary with the given day and student."""
    if day in attendance_dict:
        attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict