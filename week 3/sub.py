#this is a program that subtracts one number from another.

# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations

#Author: Katie O'Brien 

x = int(input("enter first number please: "))
y = int(input('enter second number please:'))
answer = x - y
print('{} minus {} is {} ' .format(x,y,answer))