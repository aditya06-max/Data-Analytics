import pandas as pd

# df = pd.read_csv('sample_products.csv')
# print(df)

# stocked = df[(df["In Stock"] == "Yes") & (df["Launch Year"] == 2022)]
# print(stocked)

# df.head()
# df.info()

# pd.read_csv("sample_products.csv", sep=";") 
# df1 = pd.read_csv("sample_products.csv", skiprows=2)  # Skip the first row of the CSV file
# print(df1)

# df2 = pd.read_csv("sample_products.csv", sep=";", skiprows=2)  # Skip the first row of the CSV file and use semicolon as separator
# print(df2)

# df3 = pd.read_csv("sample_products.csv",usecols=["Product Name", "Launch Year"])  # Read only specific columns from the CSV file
# print(df3)

# df4 = pd.read_excel("sample_two_sheet_data.xlsx")
# print(df4)

 # df5 = pd.read_excel("sample_two_sheet_data.xlsx", sheet_name="Sheet2")  # Read a specific sheet from the Excel file
# print(df5)

# df6 = pd.ExcelFile("sample_two_sheet_data.xlsx").sheet_names  # Get the names of all sheets in the Excel file
# print(df6)

# df7 = pd.read_csv(
# "sample_products.csv",
# dtype={"price": float, "quantity": int}
# )
# print(df7)