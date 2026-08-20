import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# print(df.head())
#countplot basically tells us about the numbers. for example here we are putting days on x-axis then on y-axis we will get the numbers of person on different days.
sns.countplot(x = "day",  data = df)
plt.show()