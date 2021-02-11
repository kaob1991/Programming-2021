# This program reads in a student's percentage
# and prints out the corresponding grade

#Author: Katie O'Brien 

import math

percentage = float(input("Enter the percentage: "))
percentageceil = math.ceil(percentage)  #Not 100% accurate as will round up regardless of decimal point
                                        #Must try figure out way to get correct rounding

if percentageceil < 0 or percentageceil > 100: # This is to make sure the range entered is between 0 and 100
    print ('Please enter a number between 0 and 100')

elif percentageceil < 40: #As this is between 0 and 40 we are printing fail
    print ("Fail")

elif percentageceil < 50: # If it's between 40 and 49 printing Pass
    print ("Pass")

elif percentageceil < 60: # If it's between 50 and 59 printing Merit 2 
    print ("Merit 2")

elif percentageceil < 70: # Between 60 and 69 Merit 1 
    print ("Merit 1")

else: # This is the only other option so will print Distinction
    print ("Distinction")

print("Congratulations on your result! ")