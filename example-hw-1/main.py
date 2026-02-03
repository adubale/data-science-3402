import numpy as np
import matplotlib.pyplot as plt

#data
sq_ft = np.array([600, 1576, 3882, 11396])
price = np.array([89900, 300300, 379000, 1700000])

#create scatter plot
plt.figure()
plt.scatter(sq_ft, price)

#TODO: label graph, format y-axis
#you can label axes in graphs using _label
plt.xlabel("Square Footage")
plt.ylabel("House Price ($)")
plt.title("House Price vs Square Feet")

#start plotting regression line
#fit m, b. y=mx+b
m, b = np.polyfit(sq_ft, price, 1)

print("slope", m)
print("intercept", b)

#create regression line
x_line = np.linspace(sq_ft.min(), sq_ft.max(), 100)
y_line = m * x_line + b #y = mx + b
plt.plot(x_line, y_line)


plt.show()
