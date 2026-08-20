import matplotlib.pyplot as plt
import numpy as np 

categories = ['A', 'B', 'C', 'D', 'E'] 
values = [10, 20, 45, 63, 90]

# plt.bar(categories, values, color='green', alpha=0.7)
# plt.show()

# barh is used to plot horizontal bar chart
plt.barh(categories, values, color='green', alpha=0.7)
plt.show()