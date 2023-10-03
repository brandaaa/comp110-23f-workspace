"""The wordle that wordles."""
__author__ = "730577554"

def contains_char(main_str: str, target_str: str ) -> bool:
    """Returns True if target character is found in any index of main string, false otherwise"""
    assert len(target_str) == 1 
    index: int = 0
    while index < len(main_str):  # Goes through main_str to find a target_str
        if main_str[index] == target_str:
            return True
        index += 1
    return False

def emojified(guess_str: str, secret_str: str) -> str:
    """Return a string of emojis if contains target letter in main string when given guess"""
    assert len(guess_str) == len(secret_str)  # Checks if guess is the same length as secret
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    index: int = 0
    while index < len(guess_str):  # Loops check if a character in guess_str is in secret_str
        if contains_char(secret_str, guess_str[index]):
            if guess_str[index] == secret_str[index]:
                result += GREEN_BOX
            else:
                result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result

def input_guess(expected_len: int) -> str:
    """Returns user guess after it ensures it is the correct amount of characters"""
    user_guess = input(f"Enter a {expected_len} character word: ")
    while expected_len != len(user_guess):
        user_guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return(user_guess)

def main() -> None:
    """Main loop of game, uses other functions"""
    secret_word: str = "codes"
    user_turns: int = 1
    max_turns: int = 6
    while user_turns <= max_turns:
        print(f"=== Turn {user_turns}/{max_turns} ===")
        user_guess = input_guess(len(secret_word))
        result = emojified(user_guess, secret_word)
        print(result)
        if user_guess == secret_word:  # When the user_guess is the same as secret_word
            print(f"You won in {user_turns}/{max_turns} turns!")
            return
        user_turns += 1
    print(f"X/{max_turns} - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
