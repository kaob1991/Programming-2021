#plotting salaries from lab 8.1

#Author Katie O'Brien 

import numpy as np
import matplotlib.pyplot as plt 



minSalary = 20000
maxSalary = 80000
noOfEntries = 10

np.random.seed (1)

salaries = np.random.randint (minSalary,maxSalary,noOfEntries)

plt.hist (salaries)

plt.show()