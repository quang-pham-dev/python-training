# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol,
# which consist of the methods __iter__() and __next__().
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
# Basic iterator example tuple
my_tuple = ("apple", "banana", "cherry")
my_iter = iter(my_tuple)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# Strings are also iterable objects, containing a sequence of characters:
my_str = "banana"

my_iter = iter(my_str)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# List
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

print(next(my_iterator))  # Outputs 1
print(next(my_iterator))  # Outputs 2
print(next(my_iterator))  # Outputs 3
print(next(my_iterator))  # Outputs 4


# Creating a custom iterator
# Define a custom iterator class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_class = MyNumbers()
my_iter = iter(my_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current


# Use the custom iterator
my_range = MyRange(1, 5)
for num in my_range:
    print(num)  # Outputs 1, 2, 3, 4


# Using Generators
# Simple generator function
def my_generator():
    yield 1
    yield 2
    yield 3


# Call the generator function
for value in my_generator():
    print(value)  # Outputs 1, 2, 3


# Generator example: Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


for num in fibonacci(10):
    print(num)  # Outputs 0, 1, 1, 2, 3, 5, 8

# Generator expressions
# Simple generator expression
squares = (x * x for x in range(5))

for square in squares:
    print(square)  # Outputs 0, 1, 4, 9, 16


# StopIteration
# The example above would continue forever if you had enough next() statements,
# or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error
# if the iteration is done a specified number of times:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


my_class = MyNumbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)
