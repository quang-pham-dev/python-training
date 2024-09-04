import pandas as pd  # alias pd

# print(pd.__version__)

# What is a Series?
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.

# Create a Series
data = pd.Series([1, 2, 3, 4, 5])
print(data)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

# Labels
# If nothing else is specified, the values are labeled with their index number.
# First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.
a = [1, 7, 2]
myvar = pd.Series(a)

print(myvar[0])

# Create Labels
# With the index argument, you can name your own labels.
a = [1, 7, 2]
myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
print(
    myvar["y"]
)  # Now When you have created labels, you can access an item by referring to the label.


# Key/Value Objects as Series
# You can also use a key/value object, like a dictionary, when creating a Series.
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
myvar2 = pd.Series(calories, index=["day1", "day2"])
print(myvar)
print(myvar2)
