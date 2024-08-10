# When an error occurs, or exception as we call it,
# Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
# Using try, except, else, and finally
# Basic exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("No exceptions occurred.")
finally:
    print("This block always executes.")

# Handling multiple exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"result: {result}")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# Raising exceptions
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Your age is {age}"


try:
    print(check_age(-5))
except ValueError as e:
    print(e)  # Outputs "Age cannot be negative!"


# Custom exceptions
# Define a custom exception class
class CustomError(Exception):
    pass


def check_value(value):
    if value < 0:
        raise CustomError("Value must be positive!")
    return value


try:
    print(check_value(-1))
except CustomError as e:
    print(e)  # Outputs "Value must be positive!"
