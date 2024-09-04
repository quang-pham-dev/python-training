# Lambda Function
# Lambda function is a small anonymous function defined using the lambda keyword.
# It is often referred to as a "lambda expression." Lambda functions are used when you need a simple function for
# a short period and don't want to formally define a full function using the def keyword.

# lambda arguments: expression
# --------------------------
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8

x = lambda a: a + 10
print(x(5))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
# --------------------------


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
# --------------------------
# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)


# Example of using a lambda function as an argument
result_addition = apply_operation(5, 3, lambda a, b: a + b)
print("Result of addition:", result_addition)

result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
print("Result of multiplication:", result_multiplication)
# --------------------------

# --------------------------
# Sorting a list of tuples by the second element
points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points.sort(key=lambda x: x[1])
print(points)  # Output: [(5, -1), (1, 2), (10, 4), (15, 1)]
# --------------------------

# --------------------------
# Filtering a list of numbers to only include even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
# --------------------------
