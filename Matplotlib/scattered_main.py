import matplotlib.pyplot as plt 
# pimport numpy as n 

x = [1, 2, 3, 4, 5]
y = [10, 20, 45, 63, 90]

plt.scatter(x, y , s=100, color="red", alpha= 0.2)
plt.title("Sample scattered Plot")
plt.xlabel("Items Sold")
plt.ylabel("Price")
plt.show() 