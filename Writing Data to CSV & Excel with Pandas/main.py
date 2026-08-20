import pandas as pd

df_Employees = pd.DataFrame({
    "Names": ["Alice", "Bob", "Charlie", "David"],
    "Ages": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
    "Companies": ["Google", "Microsoft", "Amazon", "Facebook"],
    "Employees_ID": [11, 1, 23, 15],
    "Joining_year": [2020, 2016, 2010, 2025]
})
#Create a dataframe for products 
df_Products = pd.DataFrame({
    "Product_ID": [101, 102, 103, 104],
    "Product_Name": ["Laptop", "Smartphone", "Tablet", "Headphones"],
    "Price": [1000, 800, 600, 200],
    "Stock": [50, 100, 75, 150]
})
print(df_Employees)
print(df_Products)

# df.to_excel("employees_data.xlsx", index=False) #index=False is commonly used to avoid writing row numbers

#The with statement automatically handles opening and properly closing/saving the Excel file after you're finished writing.
# with pd.ExcelWriter("report.xlsx") as writer:
#      #ExcelWriter creates an Excel workbook that Pandas can write to.Here report.xlsx is the name of excel file we want to create. creates a variable called writer that represents that Excel workbook.
#     df_Employees.to_excel(writer, sheet_name="Employees", index=False)
#     df_Products.to_excel(writer, sheet_name="Products", index=False)

# Use this carefully to avoid duplicate data.
df_Products.to_csv("log.csv", mode="a", header=False, index=False) #mode="a" is used to append data to an existing file. 
# header=False is used to avoid writing column names again. index=False is used to avoid writing row numbers.

# Always export:
# • only required columns
# • cleaned and validated data, here is the exapmle.

df_Employees[["Names", "Ages", "City"]].to_csv("employees_data.csv", index=False) 