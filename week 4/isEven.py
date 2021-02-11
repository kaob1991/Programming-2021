# Program to tell a user if the number they entered is even or odd

# Author: Katie O'Brien 

number = int(input ("enter an integer: "))

#This divides by 2 and checks if the remainder is 0 i.e. even
if (number % 2) == 0:

    #This is then saying if true then print
    print ((' {} is an even number').format (number))

    
#If its false, then print this:
else: 
    print ((' {} is an odd number').format (number))
