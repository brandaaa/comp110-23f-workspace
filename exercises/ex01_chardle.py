"""EX01 Chardle. Wordle but not wordle."""
__author__ = "730577554"


five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
      print("Error: Word must contain 5 characters")
      exit()

letter : str = input("Enter a single character: ")
if len(letter) != 1:
      print("Character must be a single character.")
      exit()
      
print("Searching for " + letter + " in " + five_char_word)

if five_char_word[0] == letter:
        print(letter + " found at index 0")
    
if five_char_word[1] == letter:
        print(letter + " found at index 1")

if five_char_word[2] == letter:
        print(letter + " found at index 2")

if five_char_word[3] == letter:
        print(letter + " found at index 3")

if five_char_word[4] == letter:
        print(letter + " found at index 4")

count = 0
for Lcheck in five_char_word:
    if Lcheck == letter:
        count +=1

if count == 1:
        print(str(count) + " instance of " + letter + " found in " + five_char_word)
else:
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + five_char_word)
    else:
        print("No instances of " + letter + " found in " + five_char_word)