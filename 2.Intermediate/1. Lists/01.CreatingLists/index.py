# Lists?
# A list is a data structure that can store a collection of items. It is one of the built-in data types and is commonly used to hold an ordered sequence of elements. Lists can contain elements of different data types, including numbers, strings, and even other lists.
# Key features of lists
# 👉 Lists maintain the order of elements as they are inserted, allowing you to access elements by their index.
# 👉 You can modify the contents of a list by adding or removing elements.
# 👉 Lists can grow or shrink in size as needed. You can add or remove elements without specifying the size beforehand.
# Creating Lists
# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(len(numbers))

# Creating a list of strings
fruits = ["apple", "orange", "banana", "grape"]
# print(fruits)
# print(len(fruits))

# Creating a mixed-type list
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)
print(len(mixed_list))


this_is_list = ["apple", "banana", "cherry"]
print(this_is_list)

# List items are indexed, the first item has index [0], the second item has index [1] etc.
print(this_is_list[0])
print(this_is_list[-1])  # access last index of the list

# To determine how many items a list has, use the len() function:
print(len(this_is_list))

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list1))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
my_list = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(my_list)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.
my_fruits_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(my_fruits_list[2:5])
print(my_fruits_list[:5])
print(my_fruits_list[3:])

# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
my_fruits_list = ["apple", "banana", "cherry"]
if "apple" in my_fruits_list:
    print("Yes, 'apple' is in the fruits list")

# Change Item Value
# To change the value of a specific item, refer to the index number:
my_fruits_list = ["apple", "banana", "cherry"]
my_fruits_list[1] = "blackcurrant"
print(my_fruits_list)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values:
my_fruits_list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
my_fruits_list[1:3] = ["blackcurrant", "watermelon"]
print(my_fruits_list)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
my_fruits_list = ["apple", "banana", "cherry"]
my_fruits_list.insert(2, "watermelon")
print(my_fruits_list)

# Append Items
# To add an item to the end of the list, use the append() method:
my_fruits_list = ["apple", "banana", "cherry"]
my_fruits_list.append("orange")  # push into the end of list
print(my_fruits_list)

# Extend List
# To append elements from another list to the current list, use the extend() method.
my_fruits_list = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
my_fruits_list.extend(tropical)
print(my_fruits_list)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
my_fruits_list = ["apple", "banana", "cherry"]
tuple = ("kiwi", "orange")  # round-brackets
my_fruits_list.extend(tuple)
print(my_fruits_list)

# Remove Specified Item
# The remove() method removes the specified item.
# If there are more than one item with the specified value, the remove() method removes the first occurrence:
my_fruits_list = ["apple", "banana", "cherry"]
my_fruits_list.remove("apple")
print(my_fruits_list)

# Remove Specified Index
# The pop() method removes the specified index.
my_fruits_list = ["apple", "banana", "cherry"]
my_fruits_list.pop(1)
print(my_fruits_list)
# If you do not specify the index, the pop() method removes the last item.
my_fruits_list.pop()
print(my_fruits_list)

# The del keyword also removes the specified index:
my_fruits_list = ["apple", "banana", "cherry"]
del my_fruits_list[0]
print(my_fruits_list)

# The del keyword can also delete the list completely.
del my_fruits_list

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
my_fruits_list = ["apple", "banana", "cherry"]
my_fruits_list.clear()
print(my_fruits_list)  # []

# Loop Through a List
# You can loop through the list items by using a for loop:
my_fruits_list = ["apple", "banana", "cherry"]
for x in my_fruits_list:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
my_fruits_list = ["apple", "banana", "cherry"]
for i in range(len(my_fruits_list)):
    print(my_fruits_list[i])

# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
my_fruits_list = ["apple", "banana", "cherry"]
i = 0
while i < len(my_fruits_list):
    print(my_fruits_list[i])
    i = i + 1

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:  # "a" character
        new_list.append(x)
new_list2 = [x for x in fruits if "a" in x]
new_list3 = [x for x in range(10)]
new_list4 = [x for x in range(10) if x < 5]
new_list5 = [x.upper() for x in fruits]
new_list6 = [x if x != "banana" else "orange" for x in fruits]
print(new_list)
print(new_list2)
print(new_list3)
print(new_list4)
print(new_list5)
print(new_list6)


# Sort List Alphanumerically
my_fruits_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
my_fruits_list.sort()
print(my_fruits_list)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
my_fruits_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
my_fruits_list.sort(reverse=True)
print(my_fruits_list)


def my_sort(n):
    return abs(n - 50)


my_list = [100, 50, 65, 82, 23]
my_list.sort(key=my_sort)
print(my_list)

# Copy a List
# Use the copy() method
my_fruits_list = ["apple", "banana", "cherry"]
# You can use the built-in List method copy() to copy a list.
new_list = my_fruits_list.copy()
# Make a copy of a list with the list() method:
new_list1 = list(my_fruits_list)
# Make a copy of a list with the : (slice) operator:
new_list2 = my_fruits_list[:]
new_list.append("water melon")
print(my_fruits_list)
print(new_list)
print(new_list1)
print(new_list2)

# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
