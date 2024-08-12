import pandas as pd  # alias pd

# A Pandas DataFrame is a 2 dimensional data structure,
# like a 2 dimensional array, or a table with rows and columns.
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# Create a DataFrame
data = {
    "Name": ["Quang", "Toan", "Nguyen"],
    "Age": [30, 31, 28],
    "City": ["Da Nang", "Da Nang", "Ho Chi Minh City"],
}
# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
#      Name  Age              City
# 0   Quang   30           Da Nang
# 1    Toan   31           Da Nang
# 2  Nguyen   28  Ho Chi Minh City


# Locate Row
# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)
# refer to the row index:
# return row 0
print(df.loc[0])  # Note: This example returns a Pandas Series.

# Return row 0 and 1:
# use a list of indexes:
print(df.loc[[0, 1]])
# Note: When using [], the result is a Pandas DataFrame.

# Named Indexes
# With the index argument, you can name your own indexes.
df = pd.DataFrame(data, index=["dev1", "dev2", "dev3"])
print(df)
# Locate Named Indexes
# Use the named index in the loc attribute to return the specified row(s).
print(df.loc["dev1  "])
