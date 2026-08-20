import matplotlib.pyplot as plt
import numpy as np #NumPy is mainly used for working with numbers, arrays and mathematical operations.

#Generate some data 
x = np.linspace(0, 10, 100) #np.linspace() creates evenly spaced numbers between two values. np.linspace(start, stop, number_of_values)

y = np.sin(x) #This calculates the sine of every value in x.

#Create a plot
plt.figure(figsize=(8,4))
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(x,y, label="sine wave", color="blue", linewidth=2)
plt.title("sine wave plot")
# plt.savefig("myplot.png")  # Save the plot as a PNG file
plt.savefig("myplot.pdf")  # Save the plot as a PDF file
plt.show()