# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(my_dict)

# Dictionary Items
# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Duplicate values will overwrite existing values:
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print(my_dict)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

my_dict = dict(name="John", age=36, country="Norway")
print(my_dict)


# Accessing Items
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = my_dict["model"]
# There is also a method called get() that will give you the same result:
x = my_dict.get("model")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
x = my_dict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# The values() method will return a list of all the values in the dictionary.
print(x)
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in my_dict:
    print("Yes, 'model' is one of the keys in the my_dict dictionary")

# Change Values
# You can change the value of a specific item by referring to its key name:
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict["year"] = 2018
# The update() method will update the dictionary with the items from the given argument.
my_dict.update({"year": 2020})
print(my_dict)

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict["color"] = "red"
# Add a color item to the dictionary by using the update() method:
my_dict.update({"color": "red"})
print(my_dict)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:

my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict.pop("model")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
my_dict.popitem()
# The del keyword removes the item with the specified key name:
del my_dict["brand"]
# print(my_dict)

# The clear() method empties the dictionary:
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict.clear()
print(my_dict)

# Loop Dictionaries
# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in my_dict:
    print(x)

# You can also use the values() method to return values of a dictionary:
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in my_dict.values():
    print(x)
# You can use the keys() method to return the keys of a dictionary:
for x in my_dict.keys():
    print(x)
# Loop through both keys and values, by using the items() method:
for x, y in my_dict.items():
    print(x, y)

# Copy Dictionaries
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be
# a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy()
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
new_dict = my_dict.copy()
# Make a copy of a dictionary with the dict() function:
new_dict1 = dict(my_dict)
print(new_dict)
print(new_dict1)

# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.
my_family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

child1 = {"name": "Emil", "year": 2004}
child2 = {"name": "Tobias", "year": 2007}
child3 = {"name": "Linus", "year": 2011}

my_family = {"child1": child1, "child2": child2, "child3": child3}

print(my_family)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
my_family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

print(my_family["child2"]["name"])

# Loop Through Nested Dictionaries
# You can loop through a dictionary by using the items() method like this:
my_family = {
    "child1": {"name": "Emil", "year": 2004},
    "child2": {"name": "Tobias", "year": 2007},
    "child3": {"name": "Linus", "year": 2011},
}

for x, obj in my_family.items():
    print(x)

    for y in obj:
        print(y + ":", obj[y])

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.
# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary
