import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sample data.csv")
print(df.head())
print(df.columns.tolist())

#Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# the column name has a spelling mistake in the file (socity), so I am renaming it
df = df.rename(columns={"socity": "society"})

#numerical columns data cleaning
df["price"] = df["price"].astype(str).str.replace(",", "").astype(float)
df["area"] = df["area"].astype(str).str.replace(",", "").astype(int)
df["rate_per_sqft"] = df["rate_per_sqft"].astype(str).str.replace(",", "").astype(int)

#categorical columns cleaning
df["status"] = df["status"].str.strip().str.lower()
df["rera_approval"] = df["rera_approval"].str.strip().str.lower().map({"approved by rera": True, "not approved by rera": False})
df["flat_type"] = df["flat_type"].str.strip().str.lower()
df["society"] = df["society"].str.strip()

# same builder is written as DLF and Dlf, so I am making all names capital
df["company_name"] = df["company_name"].str.strip().str.upper()

df = df.drop_duplicates()

# some rows have a wrong BHK count like 99 or 114, so I am removing them
df = df[df["bhk_count"] <= 10]

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

# some builder names are spelling mistakes with only 1-2 listings, so I am only using builders with at least 30 listings
builder_rates = df.groupby("company_name")["rate_per_sqft"].agg(["mean", "count"])
builder_rates = builder_rates[builder_rates["count"] >= 30]

top_5_builders = builder_rates.sort_values("mean", ascending=False).head(5)
print(top_5_builders)
print("The top 5 builders that price higher are:", end=" ")
for builder in top_5_builders.index:
    print(builder, end=", ")
print()

#Question 10: Are larger homes always more expensive per square foot?

sns.scatterplot(x = 'area', y = 'rate_per_sqft', data = df)
plt.show()


# Questions 11 to 16 are about problems a normal home buyer faces
# in Gurgaon. You can change the budget and BHK below to match
# what you want to buy.

budget = 20000000        # my budget = 2 crore
wanted_bhk = 3           # I want a 3 BHK

#Question 11: How many options do I have in my budget?
# Problem: buyers waste a lot of time visiting flats they cannot afford.

options_in_budget = df[(df['bhk_count'] == wanted_bhk) & (df['price'] <= budget)]

print(f"There are {len(options_in_budget)} listings of {wanted_bhk} BHK under {budget/10000000} crore.")
print("Sectors with the most options in this budget:")
print(options_in_budget['locality'].value_counts().head(5))


#Question 12: Which sectors give the best value for money?
# Problem: buyers do not know which sector is cheaper per sqft.
# I am only using sectors with at least 50 listings so the result is reliable.

sector_data = df.groupby('locality')['rate_per_sqft'].agg(['mean', 'count'])
sector_data = sector_data[sector_data['count'] >= 50]

cheapest_sectors = sector_data.sort_values('mean').head(5)
print("5 cheapest sectors per sqft:")
print(cheapest_sectors)


#Question 13: Is a flat overpriced compared to its sector?
# Problem: buyers cannot tell if the price asked is fair.
# I compare each flat's rate with the median rate of its own sector.

df['sector_median_rate'] = df.groupby('locality')['rate_per_sqft'].transform('median')
df['extra_percent'] = (df['rate_per_sqft'] - df['sector_median_rate']) / df['sector_median_rate'] * 100

overpriced = df[df['extra_percent'] > 30]
print(f"{len(overpriced)} out of {len(df)} listings are priced more than 30% above their sector median.")

# showing the top 10 only for flats inside a society, because "Outside Socity" rows are mostly plots and independent houses
overpriced_in_society = overpriced[overpriced['society'] != 'Outside Socity']
print(overpriced_in_society.sort_values('extra_percent', ascending=False)[['society', 'locality', 'rate_per_sqft', 'sector_median_rate', 'extra_percent']].head(10))


#Question 14: Which builders can I trust? (RERA approval)
# Problem: delayed or fraud projects are the biggest fear of a buyer.
# "Outside" means the flat is not inside any builder society, so I am leaving it out.
# I am only using builders with at least 30 listings.

builders = df[df['company_name'] != 'OUTSIDE']
builder_data = builders.groupby('company_name')['rera_approval'].agg(['mean', 'count'])
builder_data = builder_data[builder_data['count'] >= 30]
builder_data['rera_approved_percent'] = builder_data['mean'] * 100

print("Builders with the highest RERA approval:")
print(builder_data.sort_values('rera_approved_percent', ascending=False).head(5)[['rera_approved_percent', 'count']])

print("Builders with the lowest RERA approval (check carefully before buying):")
print(builder_data.sort_values('rera_approved_percent').head(5)[['rera_approved_percent', 'count']])


#Question 15: What EMI will I pay and how much salary do I need?
# Problem: buyers look at the price but forget the monthly loan burden.
# I assume 20% down payment, 8.5% interest and 20 years loan.
# Banks usually want EMI to be below 40% of monthly income.

typical_price = df[df['bhk_count'] == wanted_bhk]['price'].median()

loan_amount = typical_price * 0.8
monthly_rate = 8.5 / 12 / 100
total_months = 20 * 12

emi = loan_amount * monthly_rate * (1 + monthly_rate) ** total_months / ((1 + monthly_rate) ** total_months - 1)
salary_needed = emi / 0.4

print(f"The typical price of a {wanted_bhk} BHK is Rs {typical_price:.0f}.")
print(f"Down payment (20%) = Rs {typical_price * 0.2:.0f}")
print(f"Monthly EMI = Rs {emi:.0f}")
print(f"Monthly salary needed = Rs {salary_needed:.0f}")


#Question 16: Which listings look too good to be true?
# Problem: a flat priced very low can be a scam or can have legal problems.
# I treat a flat as suspicious if its rate is less than half of its sector median.

too_cheap = df[df['rate_per_sqft'] < 0.5 * df['sector_median_rate']]
not_rera_cheap = too_cheap[too_cheap['rera_approval'] == False]

print(f"{len(too_cheap)} listings are priced less than half of their sector median.")
print(f"Out of these, {len(not_rera_cheap)} are also NOT approved by RERA.")
print(too_cheap[['society', 'locality', 'rate_per_sqft', 'sector_median_rate', 'rera_approval']].head(10))

sns.boxplot(x = 'flat_type', y = 'rate_per_sqft', data = df)
plt.show()
