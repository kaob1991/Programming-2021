# Program to get the absolute value of a number 

# Author: Katie O'Brien 

# NB. In the question, number is ambiguous, but output suggests 
# we should be using floats, so I am casting the input to a float

number = float(input('Please enter a number: '))
absoluteNumber = abs(number)

print('The absolute number of {} is {}'.format(number, absoluteNumber))