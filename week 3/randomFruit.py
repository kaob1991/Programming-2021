# this program prints out a random fruit

#Author: Katie O'Brien 

import random

fruits = ['Apple', 'Banana', 'Pear', 'Mango', 'Orange']

# We want a random number between 0 and length -1 
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print('A random fruit is: {}'.format(fruit))

