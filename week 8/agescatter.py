# Scatterplot of ages displayed as a scatterplot 

# Author Katie O'Brien 


import numpy as np 

import matplotlib.pyplot as plt


minSalary = 20000
maxSalary = 80000
noOfEntries = 1000

np.random.seed (1)

salaries = np.random.randint (minSalary,maxSalary,noOfEntries)
ages = np.random.randint (low = 21, high = 65, size = noOfEntries)

plt.scatter (ages, salaries, label = "salaries")



xpoints = np.array (range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = "r", label = "x-squared")

plt.title  ("random plot")
plt.xlabel ('Salaries')
plt.ylabel ("Age")
plt.legend ()


#plt.show()

plt.savefig ('Prettier-plot.png')
