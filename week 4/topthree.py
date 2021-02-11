# This program generates 10 random numbers
# Prints them out, and then prints
# the top 3

# Author Katie O'Brien 

# I will use a list to store the numbers 

import random
# The variwables required 
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range(0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
print ("{} random numbers\t {}".format (howMany,numbers))

topOnes = numbers.copy()
topOnes.sort (reverse = True)
print ("The top {} are \t\t {}".format(topHowMany,topOnes[0:topHowMany]))


