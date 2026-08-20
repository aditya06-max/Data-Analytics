import matplotlib.pyplot as plt 
import numpy as np 

x = [1, 2, 3, 4, 5]
y = [10, 20, 45, 63, 90]

plt.plot(x, y, color="blue", linewidth=1, linestyle="--", marker="o")
plt.title("Sample Line Plot")
plt.xlabel("Items Sold")
plt.ylabel("Price")
plt.show() 