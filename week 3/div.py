# This program reads in 2 numbers and outputs the 
# integer number and the remainder

#Author: Katie O'Brien 

x = int(input('please enter the first number: '))
y = int(input('please enter the number you want to divide this by: '))
answer = int(x//y) # // gives the integer division
remainder = x%y # % gives the remainder 

print ('{} divided by {} gives the answer {} with a remainder of {}' .format( x, y, answer, remainder))