import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# print(df.head())
sns.boxplot(x = "day", y = "total_bill", data = df)
plt.show()