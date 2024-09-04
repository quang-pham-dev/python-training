# Tuples?
# Tuple is an ordered, immutable collection of elements. This means that once you create a tuple, you cannot modify its contents - you can't add, remove, or change elements in a tuple after it has been created. Tuples are defined by enclosing a comma-separated sequence of values in parentheses ()
# Basic Syntax
# Error
# ---------------------------
my_tuple = (1, 2, 3, "hello", 3.14)
# print(my_tuple[0])  # Output: 1
# print(my_tuple[3])  # Output: 'hello'
print(len(my_tuple))

# # This will raise an error since tuples are immutable
# # my_tuple[0] = 5

# # Creating a new tuple with modified content
# new_tuple = my_tuple + (5, 'world')
# print(new_tuple)  # Output: (1, 2, 3, 'hello', 3.14, 5, 'world')
# ---------------------------

# ---------------------------
# Weird Things About Tuples
# nums = 1,2,3,4,5
# print(type(nums)) # tuple

# notTuple = (50)
# isTuple = (50,)
# print(type(notTuple)) # number
# print(type(isTuple)) # tuple
# ---------------------------

# ---------------------------
# Iterating Over Tuple
# friends = ("alex", "michel", "Quang Pham")
# for friend in friends:
#     print(friend)


my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
# Ordered
# When we say that tuples are ordered, it means that the items have a defined order,
# and that order will not change.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change,
# add or remove items after the tuple has been created.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[2:5])
# This will return the items from position 2 to 5.
# Remember that the first item is position 0,
# and note that the item in position 5 is NOT included

# This example returns the items from the beginning to, but NOT included, "kiwi":
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[:4])

# This example returns the items from "cherry" and to the end:
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[2:])

# This example returns the items from index -4 (included) to index -1 (excluded)
my_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(my_tuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

my_tuple = ("apple", "banana", "cherry")
if "apple" in my_tuple:
    print("Yes, 'apple' is in the fruits tuple")


# UPDATE TUPLE
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable,
# or immutable as it also is called. But there is a workaround.
# You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)  # convert to list
y[1] = "kiwi"
y.append("orange")
y.remove("apple")
x = tuple(y)
print(x)
# The del keyword can delete the tuple completely:
my_tuple = ("apple", "banana", "cherry")
del my_tuple
# print(my_tuple)  # this will raise an error because the tuple no longer exists

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits  # Same destructuring in JS
print(green)
print(yellow)
print(red)

# Using Asterisk*
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Loop Tuples
# Using a for  loop
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)

    fruits = ("apple", "banana", "cherry")
for i in range(len(fruits)):
    print(fruits[i])

# Using a While Loop

fruits = ("apple", "banana", "cherry")
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# Join Two Tuples
# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
my_tuple = fruits * 2

print(my_tuple)

# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found
