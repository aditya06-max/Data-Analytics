import matplotlib.pyplot as plt
import numpy as np


#pie chart is used for very small categories 

sizes = [28, 32, 34, 36]
labels = ["small", "medium", "large", "x-large"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
plt.show()