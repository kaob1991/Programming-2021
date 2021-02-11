# Gives hints based on guess 1 

# Author Katie O'Brien 

import random

numberToGuess = random.randrange (0, 100)

guess = int(input("Please guess the number: "))

while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
    else:
        (print("Too high!"))
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess)