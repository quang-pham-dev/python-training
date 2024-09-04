# Sets?
# A set is an unordered collection of unique elements. Sets are defined by enclosing a comma-separated sequence of values in curly braces {}. Unlike lists or tuples, sets do not allow duplicate elements, and the order of elements is not guaranteed.
# Example of set
# We can also create a set from a list using the set() constructor
# --------------------------
my_set = set({1,5,6})
my_new_set = {1, 2, 3, 4, 5}
print(type(my_set))
print(type(my_new_set))
print(len(my_new_set))
# 👇 Accessing elements using index is not allowed because sets are unordered ❌
# print(my_set[0]) 
# --------------------------

# --------------------------
# Duplicates not allowed ❌
# Set will totally remove duplicate element and give you only unique.
unique_players = {"alex", "alex", "alex", "Quang Pham", "huxn", "michel", "michel"}
print(unique_players)
# --------------------------

# --------------------------
# Add One Element To The Existing Set
games = {"GTA 6", "Spider Man", "The Wither"}
games.add("Cyberpunk")

# Add Multiple Elements To The Existing Set
games.update(["Tekken 8", "Homeworld 3", "Prince of Persia: The Lost Crown"])
games.update(("Dragon's Dogma II", "Nightingale", "Skull & Bones"))
print(games)
# --------------------------

# --------------------------
# Deleting Elements From Set
movies = {"Deadpool 3", "Kraven the Hunter", "Kingdom of the Planet of the Apes"}
movies.remove("Kraven the Hunter")
movies.clear()
print(movies)
# --------------------------

# --------------------------
# Iterating over sets
songs = {"A lot", "Rockstar", "Houdini"}
for song in songs:
    print(song)
# --------------------------

# Create a Set:

my_set = {"apple", "banana", "cherry"}
print(my_set)

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Sets cannot have two items with the same value. 👍
# True and 1 is considered the same value:
# False and 0 is considered the same value:
# Get the Length of a Set
# To determine how many items a set has, use the len() function.

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
my_set = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(my_set)

# Access Set Items
# Loop through the set, and print the values:
my_set = {"apple", "banana", "cherry"}
for x in my_set:
    print(x)

# Check if "banana" is present in the set:
my_set = {"apple", "banana", "cherry"}
print("banana" in my_set)
# Check if "banana" is NOT present in the set:
my_set = {"apple", "banana", "cherry"}
print("banana" not in my_set)

# Add Set Items
# To add one item to a set use the add() method.
my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
print(my_set)

# To add items from another set into the current set, use the update() method.
my_set = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
my_list = ["kiwi", "orange"]
my_set.update(tropical, my_list)
print(f"my set added: {my_set}")

# Remove Set Items
my_set = {"apple", "banana", "cherry"}
my_set.remove("banana")
print(my_set)

# Remove "banana" by using the discard() method:
my_set = {"apple", "banana", "cherry"}
my_set.discard("banana")
print(my_set)

# Remove a random item by using the pop() method:
my_set = {"apple", "banana", "cherry"}
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
x = my_set.pop()
print(x)
print(my_set)

# The del keyword will delete the set completely:
my_set = {"apple", "banana", "cherry"}
del my_set
# print(my_set) # this will raise an error because the tuple no longer exists

# Loop Sets
# You can loop through the set items by using a for loop:
# Loop through the set, and print the values:
my_set = {"apple", "banana", "cherry"}
for x in my_set:
    print(x)

# Join Sets
# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Union
# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

my_set = set1.union(set2, set3, set4)
# OR
my_set = set1 | set2 | set3 | set4
print(my_set)

# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains
# the items that are present in both sets.
# Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
# You can use the & operator instead of the intersection() method, and you will get the same result.
set3 = set1 & (set2)
print(set3)  # {'apple'}

# The intersection_update() method will also keep ONLY the duplicates,
# but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0.
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

# The difference() method will return a new set that will contain only the items
# from the first set that are not present in the other set.
# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
# You can use the - operator instead of the difference() method, and you will get the same result.
set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set
# that are not in the other set, but it will change the original set instead of returning a new set.
# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set3 = set1 ^ set2
print(set3)

# The symmetric_difference_update() method will also keep all but the duplicates,
# but it will change the original set instead of returning a new set.
# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

# Set Methods Built-in
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others