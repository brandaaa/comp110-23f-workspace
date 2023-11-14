"""Game that only completes when you guess the right number."""

from random import randint 

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 3
tries_count: int = 1

while guess != secret and (tries_count < number_of_tries):
    print("Wrong!")
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    if guess > secret:
        print("Your guess was too high!")
    else:
        print(("Your guess was too low!"))
    guess = int(input("Guess again: "))
if guess == secret:
    print("You got it!")