# Default Param Values
# You can also pass a default value for a parameter in a function.
# If a value is provided for that parameter when the function is called, it will use the provided value. If no value is provided, the function will use the default value.


# Example 1:
def greet(name="World"):
    print(f"Hello, {name}!")


greet()  # Output: Hello, World!
greet("Quang")  # Output: Hello, Quang!


# Example 2:
def calculate_area(length, width=10):
    return length * width


area = calculate_area(5)
print(
    f"The area of the rectangle is: {area}"
)  # Output: The area of the rectangle is: 50
