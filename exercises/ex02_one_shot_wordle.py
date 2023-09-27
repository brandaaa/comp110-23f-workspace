"""Exercise 3. The wordle."""
__author__ = "730577554"

secret_word = "python"  # Secret word
i: int = len(secret_word)  # Length of word
# Initialized Variables
index: int = 0
result: str = ""
guess: str = input(f"what is your {i}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):  # Loops to check if guess has correct length of characters
    guess = input(f"That was not {i} letters! Try again: ") 

while index < len(secret_word):  # Loops through each character of the guess
    if guess[index] == secret_word[index]:
        result += GREEN_BOX
    else:
        char_exist = False  # Initialize variable to check if there is an existing character
        alt_indices = 0
        while not char_exist and alt_indices < len(secret_word):  # Loops to check if there is a character existing in another position
            if secret_word[alt_indices] == guess[index]: 
                char_exist = True  # True when there is a existing character in another position
            else:
                alt_indices += 1 
        if char_exist:
            result += YELLOW_BOX  # Yellow box if there is a letter in the wrong position
        else:
            result += WHITE_BOX  # White box if guess does not contain a letter within the secret word
    index += 1  # Increases the increment of the index
print(result)  # Prints final results of emojis

if guess == secret_word:  # Checks the guess is correct
    print("Woo! You got it!")
else:  # Correct length but wrong guess
    print("Not quite. Play again soon!")