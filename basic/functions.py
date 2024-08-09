# In Python a function is defined using the def keyword:
def hello_world():
    print("Hello from a function")


# Execute
hello_world()


# Parameters and arguments
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
def get_fullname(first_name, last_name):
    full_name = f"{first_name} {last_name}"  # full_name is a local variable
    name_length = len(full_name)
    return full_name, name_length


name, length = get_fullname("Quang", "Pham")
print(f"Your name is: {name}")
print(f"Your name length: {length} characters")


# Function with the default value
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Execute
print(greet("Quang"))  # Output "Hello, Quang!"
print(greet("Quang", "Hi"))  # Output "Hi, Quang!"


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def find_maximum(*args):
    if not args:
        return None
    return max(args)


result = find_maximum(3, 5, 9, 1, 7)
print(f"The maximum number is: {result}")


# Understand Fruitful Function and Void Function => return keyword
# "**kwargs" If the number of keyword arguments is unknown, add a double ** before the parameter name:
def get_unknown_name(**args):
    # Using .get() get value if does not exits get default value
    first_name = args.get("fname", "Quang")
    last_name = args.get("lname", "Pham")
    print(f"His first name is {first_name}, His last name is {last_name}")


get_unknown_name(fname="Quang", lname="Pham")
get_unknown_name(fname="David")
get_unknown_name()
