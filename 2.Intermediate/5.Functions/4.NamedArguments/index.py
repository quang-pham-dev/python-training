# Named Arguments
# Keyword arguments, aka named arguments, allow you to pass values to a function by explicitly specifying the parameter names along with their values.
# This can make function calls more readable and allow you to provide arguments in a different order than they appear in the function definition.


# Example 1:
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")


display_info(name="Quang", age=20)  # Output: Name: Quang, Age: 20
display_info(age=20, name="Quang")  # Output: Name: Quang, Age: 20


# Example 2:
def calculate_rectangle_area(length, width):
    return length * width

# Using keyword arguments to call the function
area = calculate_rectangle_area(length=5, width=3)
print(
    f"The area of the rectangle is: {area}"
)  # Output: The area of the rectangle is: 15
