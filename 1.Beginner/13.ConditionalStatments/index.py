# Conditional statements are used to control the flow of a program based on certain conditions.
# They allow you to execute different blocks of code depending on whether a specified condition evaluates to True or False

x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
# ---------------------------

password = 8

if password > 8:
    print("Valid Password: Welcome")
elif password < 8:
    print("Invalid Password: Password should be at least 8 characters")
else:
    print("Please enter your password to login.")
