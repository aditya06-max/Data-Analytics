import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "age": [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    "marks": [85, 90, 95, 80, 75, 70, 65, 60, 55, 50],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
} 
df = pd.DataFrame(data)
print(df)

# print(df.head(5))  # Display the first 5 rows of the DataFrame
# print(df.tail(5))  # Display the last 5 rows of the DataFrame
# print(df.describe())  # Display summary statistics of the DataFrame
print(df[["name", "age"]])  # Display only the 'name' and 'age' columns of the DataFrame