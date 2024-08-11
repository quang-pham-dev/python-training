# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Syntax: lambda arguments : expression
x = lambda a: a + 10
print(x(5))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:
def multiple_with_prams(n):
    return lambda a: a * n


doubler = multiple_with_prams(2)
tripper = multiple_with_prams(3)

print(f"doubler : {doubler(10)}")  # 20
print(f"tripper : {tripper(10)}")  # 30

# Using a lambda function with map
squares = map(lambda x: x * x, [1, 2, 3, 4])
print(list(squares))  # Outputs [1, 4, 9, 16]

# Using a lambda function with filter
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])
print(list(evens))  # Outputs [2, 4]
