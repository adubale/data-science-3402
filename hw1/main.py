import numpy as np
import matplotlib.pyplot as plt

# AI disclosure:
# ChatGPT (OpenAI) was used to help clarify how to compare FRED vs Zillow medians
# using absolute difference, relative difference, and ratio. No code was generated.

#data. source: Zillow
my_sqft = np.array([1000, 1120, 1145, 1200, 1272, 1400, 1400, 1472, 1740, 1810, 1827, 2000, 2152, 2233, 2588, 2712, 3252, 3882, 4555, 7156]) 
my_price = np.array([200000, 85000, 195000, 249000, 89000, 184000, 124900, 328000, 195000, 279000, 170000, 275000, 288900, 200000, 270000, 318000, 399000, 420000, 689000, 1225000])

#SECTION 1: plot data

#create scatter plot
plt.figure()
plt.scatter(my_sqft, my_price)

plt.xlabel("Square Footage")
plt.ylabel("House Price ($)") 
plt.title("House Price vs. Square Feet")

#start plotting regression line
m, b = np.polyfit(my_sqft, my_price, 1)

x_line = np.linspace(my_sqft.min(), my_sqft.max(), 100)
y_line = m * x_line + b
plt.plot(x_line, y_line)

plt.show()

#SECTION 2: find median
ppersqft = my_price[:20] / my_sqft[:20]
z_med = np.median(ppersqft) #127.06114918292039

#SECTION 3: compare zillow median vs FRED median
f_med = 149
diff_med = f_med - z_med
abs_diff = abs(diff_med)
rel_diff = abs_diff/f_med
ratio = z_med / f_med

#SECTION 4: output comparisons

print(f"Zillow median $/sqft:   {z_med:.4f}")
print(f"FRED median $/sqft:     {f_med:.4f}")
print(f"Diff (FRED - Zillow):   {diff_med:.4f}")
print(f"Absolute diff:          {abs_diff:.4f}")
print(f"Relative diff:          {rel_diff:.4f}")
print(f"Ratio (Zillow/FRED):    {ratio:.4f}")
