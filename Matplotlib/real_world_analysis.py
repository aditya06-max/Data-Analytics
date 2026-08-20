import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1, 11)  # years from 1 to 10
sales_in_cr = np.array([1, 3, 5, 6.5, 5.6, 7.9, 10, 5, 11, 20])  # creates a NumPy array (Sample Sales in cr),
plt.figure(figsize=(10,5)) #Width  = 10 inches, Height = 5 inches
plt.plot(years, sales_in_cr, label="Sales in crores", marker="o")
plt.legend()
plt.title("Sales over the years")
plt.xlabel("Years")
plt.ylabel("Sales in crores")
plt.savefig("sales_plot.pdf")  # Save the plot as a PDF file
plt.show()