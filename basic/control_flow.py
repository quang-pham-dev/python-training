# Conditional statements
if True:
    print("Hello Python If")

if 2 > 1:
    print("2 is greater than 1")
elif 3 > 1:
    print("1 is not greater than 3")
else:
    print("1 is not greater than 2")

a = 200
b = 33
if a > b:
    print(f"a = {a} is greater than b = {b}")
# Short hand
print("A") if a > b else print("B")

# Logical operators
# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print("At least one of the conditions is True")

# Not
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
a = 33
b = 200
# if a <= b:
if not a > b:
    print(f"a: {a}")
    print(f"b: {b}")
    print("a is NOT greater than b")

# Nested If
# You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if
# statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
    pass

#  Boolean expressions
x = 10
y = 9
if x != y:
    print("x is not equal to y")
if x > y:
    print("x is greater than y")
if x < y:
    print("x is less than y")
if x >= y:
    print("x is greater than or equal to y")
if x <= y:
    print("x is less than or equal to y")


# Recursion
def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)


countdown(3)


# Infinite recursion
def recurse():
    recurse()


# RecursionError: maximum recursion depth exceeded
# recurse()

# Prompt the user to enter their name
name = input("Enter your name: ")
# Print a greeting message
print(f"Hello, {name}!")
