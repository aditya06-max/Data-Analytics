import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sample data.csv")
print(df.head())
print(df.columns.tolist())

#Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

#numerical columns data cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

#categorical columns cleaning
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera": True, "not approved by rera": False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()

df = df.drop_duplicates()

print(df)
print(df.info())

#Question 1: Which is the  costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(costliest_flat)
# f = formatted string → it allows you to put variables directly inside a string using {}.

print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000} crores in {costliest_flat['society']} society.")

#Question 2: Which locality has the highest average price?

highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(highest_avg_price_locality)
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

# Question 3: Which locality has the highest rate per square foot?

highest_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(highest_rate_per_sqft)
print(f"The locality with highest rate per sqft is {highest_rate_per_sqft}.")

#Question 4: Do ready-to-move properties cost more than under-construction properties?

ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
underconstruction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > underconstruction_avg_price:
    print("Ready to move in properties are more costlier than under construction properties. ")

else:
    print("underconstruction properties are more expensive than ready to move in properties.")

# Question 5: Do RERA-approved properties command a price premium?

rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_unapproved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_unapproved_avg_price:
    print("RERA-approved properties command a price premium.")

else:
    print("RERA-unapproved properties doesnot charge a premium.")

# Question 6: How does area (sqft) impact property price?

sns.scatterplot(x = 'area', y = 'price', data = df)
plt.show()

#Question 7: Which BHK configuration is the most expensive on average?

most_expensive_bhk = df.groupby('bhk_count')['price'].mean().idxmax()

print(f"the most expensive BHK configuration is {most_expensive_bhk}.")

#Question 8: Which property type (Apartment, Floor, Plot) is the costliest?

expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive property type is {expensive_property_type}. ")

#Question 9: Do certain builders or companies consistently price higher?

print(df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5))
print("The top 5 builders that price are:", end=" ")
top_5_builders = df.groupby("company_name")['rate_per_sqft'].mean().sort_values(ascending=False).head(5)
for builders in top_5_builders:
    print(builders, end=", ")

#Question 10: Are larger homes always more expensive per square foot?

sns.scatterplot(x = 'area', y = 'rate_per_sqft', data = df)
plt.show()