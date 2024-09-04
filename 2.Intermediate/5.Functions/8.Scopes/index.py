# Scope?
# A scope refers to the region of a program where a particular variable can be accessed or modified.
# The scope of a variable is determined by where it is defined in the code, and it plays a crucial role in understanding how variables are accessed and manipulated within a program.
# There are two main types of scope in Python:

# 1️⃣ Global Scope
# Variables defined at the top level of a module are considered to be in the global scope.
# Global variables can be accessed and modified from any part of the code, including within functions.

# Example:
global_variable = 10  # This is a global variable


def print_global_variable():
    print(global_variable)


print_global_variable()  # Outputs: 10


# 2️⃣ Local Scope
# Variables defined within a function are considered to be in the local scope of that function.
# Local variables can only be accessed within the function where they are defined.
# Example:
def print_local_variable():
    local_variable = 20  # This is a local variable
    print(local_variable)


print_local_variable()  # Outputs: 20


# 3️⃣ Nested Scope
# There's also another concept of nested scopes (not that much important).
# If a function is defined within another function, it creates a nested scope.
# Variables in the outer function can be accessed within the inner function, but not vice versa.
# Example:
def outer_function():
    outer_variable = "I'm in outer function"

    def inner_function():
        print(outer_variable)

    inner_function()  # Outputs: I'm in outer function


outer_function()  # Outputs: I'm in outer function
