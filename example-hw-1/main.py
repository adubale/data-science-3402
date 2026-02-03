import numpy as np
import matplotlib.pyplot as plt

#data
sq_ft = np.array([600, 1576, 3882, 11396])
price = np.array([89900, 300300, 379000, 1700000])

#create scatter plot
plt.figure()
plt.scatter(sq_ft, price)

#TODO: label graph, format y-axis

plt.show()
