# Common built-in functions
# Using some common built-in functions
print(abs(-10))  # Outputs 10
print(sum([1, 2, 3]))  # Outputs 6
print(max(5, 10, 15))  # Outputs 15
print(sorted([3, 1, 2]))  # Outputs [1, 2, 3]


# map, filter, and reduce
# Using map to apply a function to all items in an iterable
def square(x):
    return x * x


squares = map(square, [1, 2, 3, 4])
print(list(squares))  # Outputs [1, 4, 9, 16]


# Using filter to filter items in an iterable
def is_even(x):
    return x % 2 == 0


evens = filter(is_even, [1, 2, 3, 4, 5])
print(list(evens))  # Outputs [2, 4]

# Using reduce to reduce an iterable to a single value
from functools import reduce


def add(x, y):
    return x + y


sum_value = reduce(add, [1, 2, 3, 4, 5])
print(sum_value)  # Outputs 15


#  Using any and all
# Using any to check if any element is True
print(any([False, True, False]))  # Outputs True

# Using all to check if all elements are True
print(all([True, True, True]))  # Outputs True
print(all([True, False, True]))  # Outputs False
