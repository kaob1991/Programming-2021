# Makes the user guess a number and keeps prompting til they get it right 

# Author: Katie O'Brien 

numberToGuess = 30

guess = int(input("Please guess the number: "))

while guess != numberToGuess:
    print("Wrong!")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", numberToGuess)