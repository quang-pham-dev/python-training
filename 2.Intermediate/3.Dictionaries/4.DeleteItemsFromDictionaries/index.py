# Deleting In Dictionaries
# We can delete items from dictionaries using the del statement or the pop() method.
# del Statement
# pop() Method
# popitem() Method
# clear() Method to Remove All Items

# del Statement
my_dict = {"name": "John", "age": 25, "city": "New York"}
del my_dict["age"]
# print(my_dict)


# pop() Method
my_dict = {"name": "John", "age": 25, "city": "New York"}


my_dict.pop("age")
# print(my_dict)


# popitem() Method -> remove last element
my_dict = {"name": "John", "age": 25, "city": "New York"}
my_dict.popitem()
print(my_dict)


# clear() Method
my_dict = {"name": "John", "age": 25, "city": "New York"}
my_dict.clear()
