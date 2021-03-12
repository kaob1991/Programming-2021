#program to create a list of 10 random numbers 

# Author: Katie O'Brien 

import numpy as np

minSalary = 20000
maxSalary = 80000
noOfEntries = 10

np.random.seed (1) # prevents the rand int from changing each time program is run

salaries = np.random.randint(minSalary,maxSalary,noOfEntries)

print (salaries)

salariesPlus = salaries +  5000
print (salariesPlus)

salariesMult = salaries * 1.05  #salaries increased by 5% ie 1.05

print (salariesMult) #This is a float array

newSalaries = salariesMult.astype (int) # converts salariesMult into int array list

print (newSalaries)