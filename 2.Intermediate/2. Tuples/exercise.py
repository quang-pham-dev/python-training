# **Tuples in Python**
# This document explores working with tuples in Python. We'll cover creating tuples, accessing elements, immutability, and unpacking.
# **Challenge 1: Creating Tuples**
# - **Using parentheses ():** Create a tuple containing your favorite foods.
# - **Using the tuple() function:** Create a tuple from a list (e.g., `tuple(["apple", "banana", "cherry"])`).
my_favorite_foods1 = ("apple", "banana", "cherry")
print(my_favorite_foods1)
my_favorite_foods2 = tuple(["apple", "banana", "cherry"])
print(my_favorite_foods2)

# **Challenge 2: Accessing Tuple Elements**
# - Create a tuple containing different data types (string, number, boolean).
# - Access elements using their index (just like with lists).
my_favorite_foods1 = (1, 2, 3, "hello", 3.14, True)
print(my_favorite_foods1[0])
print(my_favorite_foods1[3])
print(my_favorite_foods1[-1])
print(my_favorite_foods1[2:5])

# **Challenge 3: Immutability of Tuples**
# - Try to modify an element in a tuple using indexing and assignment (e.g., `my_tuple[0] = "new value"`).
# - Observe the error message that you'll get since tuples are immutable (unchangeable).

# **Challenge 4: Unpacking Tuples**
# - Create a tuple with student information (name, age, grade).
# - Use tuple unpacking to assign these values to separate variables.˝
