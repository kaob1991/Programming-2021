# Program that prints out a random number between 1 and 10 

import random

x = int(input('please input a number: '))
y = int(input('please input another number: '))

number = random.randint(x,y)
print('here is a random number between the 2 numbers you picked: {}'.format(number))