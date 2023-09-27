"""Exercise 3. The wordle."""
__author__="730577554"

secret_word = "python"
i: int = len(secret_word)
index: int = 0
result: str = ""
guess: str = input(f"what is your {i}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
       guess = input(f"That was not {i} letters! Try again: ") 

while index < len(secret_word):
    if guess[index] == secret_word[index]:
        result += GREEN_BOX
    else:
        char_exist = False
        alt_indices = 0
        while not char_exist and alt_indices < len(secret_word):
            if secret_word[alt_indices] == guess[index]:
                char_exist = True
            else:
                alt_indices += 1
        if char_exist:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    index += 1
print(result)

if guess == secret_word:
    print(f"Woo! You got it!")
else:
    print(f"Not quite. Play again soon!")