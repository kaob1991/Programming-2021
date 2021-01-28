# This program reads a number and prints out one more than that number 
# Author: Katie O'Brien 

number = int(input("Please type in a number:"))
newNumber = number + 1
print("This is your number plus one: " + str(newNumber))
#Alternatively you can do...
print ('{} plus one is {}' .format(number, newNumber))