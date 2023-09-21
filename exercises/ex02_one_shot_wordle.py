"""Exercise 3. The wordle."""
__author__="730577554"

secret_word = "python"
i: int = len(secret_word)
guess: str = input(f"what is your {i}-letter guess? ")

while i != len(guess):
    guess = input(f"That was not {i} letters! Try again: ")
    if (guess) == (secret_word):
         print(f"Woo! You got it!") 
    if (guess) != (secret_word) and i == len(guess):
        print(f"Not quite. Play again soon!")
    
    


    
    

