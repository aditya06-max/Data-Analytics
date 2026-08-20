import matplotlib.pyplot as plt
import numpy as np

years = [2021, 2022, 2023, 2024, 2025]

company_A = [10, 15, 20, 25, 30]
company_B = [8, 18, 17, 28, 35]

plt.plot(years, company_A, label="Company A")
plt.plot(years, company_B, label="Company B")

plt.legend()

plt.show()