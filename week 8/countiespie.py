#Creating a pie chart of counties 

#Author : Katie O' Brien 

import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ["Cork", "Wexford", 'Dublin', 'Meath', 'Kildare']

counties = np.random.choice(possibleCounties, p = [0.1, 0.3, 0.2, 0.12, 0.28],size = (100))

unique, counts = np.unique(counties, return_counts=True)

plt.pie (counts, labels = unique)

plt.savefig ('piechart.png')