# 1. Basic Function with Parameters
# Challenge: Write a function that takes two numbers (a and b) as parameters and returns their sum.
# Call the function with different numeric arguments to test it.


def sum_of_two_numbers(a: int, b: int):
    return a + b


print(sum_of_two_numbers(1, 2))
print(sum_of_two_numbers(5, 6))


# 2. Default Parameter Values
# Challenge: Modify the function from Challenge 1 to have a default value for the second parameter (b)
# in case it's not provided during the function call. Set the default value to 10.
# Call the function with one and two arguments to see how the default value works.
def sum_of_two_numbers(a: int, b: int = 10):
    return a + b


print(sum_of_two_numbers(1))
print(sum_of_two_numbers(5, 6))

# 3. Named Arguments
# Challenge: Write a function that calculates the area of a rectangle. It should take two parameters for width and height.
# Call the function with the arguments named appropriately (e.g., area(width=5, height=10)) to demonstrate named arguments.


def area_of_rectangle(width: int, height: int):
    return width * height


print(area_of_rectangle(width=5, height=10))


# 4. Docstrings and Return Statements
# Challenge: Add a docstring to the function explaining its purpose and parameters.
# Ensure the function returns the calculated value using a return statement.
def area_of_rectangle(width: int, height: int):
    """
    Calculate the area of a rectangle.

    Parameters:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Returns:
    int: The area of the rectangle.
    """
    return width * height


# 5. Nested Functions
# Challenge: Write a function that calculates the factorial of a number (factorial of a number is the product of all
# positive integers less than or equal to that number). Define another function within the first function (nested function)
# to perform the factorial calculation recursively. The outer function can call the nested function and return the result.
# ** (Implementation for nested functions requires additional coding) **
def factorial_calculator(n: int) -> int:
    """
    Calculate the factorial of a number using a nested function.

    Args:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.

    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    def recursive_factorial(x: int) -> int:
        """
        Nested function to calculate factorial recursively.

        Args:
        x (int): The current number in the recursion.

        Returns:
        int: The factorial of x.
        """
        if x == 0 or x == 1:
            return 1
        return x * recursive_factorial(x - 1)

    return recursive_factorial(n)


# Test the function
print(factorial_calculator(5))  # Should print 120
print(factorial_calculator(0))  # Should print 1

try:
    print(factorial_calculator(-1))
except ValueError as e:
    print(f"Error: {e}")

# 6. Lambda Functions (Bonus Challenge)
# Challenge: Explore lambda functions as a concise way to write anonymous functions for simple operations.
# Write a program that uses a lambda function to calculate the square of a number.

# Define a lambda function to calculate the square of a number
square = lambda x: x ** 2

# Test the lambda function
number = 5
result = square(number)

print(f"The square of {number} is: {result}")

# Optional: Demonstrate using the lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))

print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared_numbers}")