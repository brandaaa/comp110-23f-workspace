"""The wordle that wordles."""
__author__ = "730577554"

def contains_char(main_str: str, target_str: str ) -> bool:
    """Returns True if target character is found in any index of main string, false otherwise"""
    assert len(target_str) == 1 
    index: int = 0
    while index < len(main_str):
        if main_str[index] == target_str:
            return True
        index += 1
    return False

def emojified(guess_str: str, secret_str: str) -> str:
    """Return a string of emojis if contains target letter in main string when given guess"""
    assert len(guess_str) == len(secret_str)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    index: int = 0
    while index < len(guess_str):
        if contains_char(secret_str, guess_str[index]):
            if guess_str[index] == secret_str[index]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
    return result

print(emojified("hello","world"))
print(emojified("elloh","hello"))
print(emojified("python","woohoo"))
print(emojified("python","python"))
print(emojified("yikyak","tiktok"))