# Return Statement
# The return statement is used within a function to send a value back to the caller.
# When a function is executed and encounters the return statement, it immediately stops executing,
# and the specified value is sent back to the caller.


# Example 1:
def add(a, b):
    """This function adds two numbers and returns the result."""
    result = a + b
    return result


result = add(3, 4)
print(
    f"The result of the addition is: {result}"
)  # Output: The result of the addition is: 7


# Example 2:
def square_and_cube(num):
    """This function returns the square and cube of a number."""
    square = num**2
    cube = num**3
    return square, cube

# Calling the function and storing the returned values
square, cube = square_and_cube(5)
print(
    f"The square of the number is: {square}"
)  # Output: The square of the number is: 25
