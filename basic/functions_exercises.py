# Here's how you can write a function named right_justify that takes a string s as a parameter
# and prints it with enough leading spaces so that the last letter of the string is in column 70
# of the display:
def right_justify(s):
    # Calculate the number of leading spaces needed
    leading_spaces = 70 - len(s)

    # Print the string with leading spaces
    print(" " * leading_spaces + s)


# Example usage
right_justify("Hello, world!")


# A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
# f()
# f()
def do_twice(func, arg):
    """Runs a function twice.

    func: function object
    arg: argument passed to the function
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """Prints the argument twice.

    arg: anything printable
    """
    print(arg)
    print(arg)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, "spam")
print("")

do_four(print, "spam")


# Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print("+ - - - -", end=" ")


def print_post():
    print("|        ", end=" ")


def print_beams():
    do_twice(print_beam)
    print("+")


def print_posts():
    do_twice(print_post)
    print("|")


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()

def one_four_one(f, g, h):
    f()
    do_four(g)
    h()

def print_plus():
    print('+', end=' ')

def print_dash():
    print('-', end=' ')

def print_bar():
    print('|', end=' ')

def print_space():
    print(' ', end=' ')

def print_end():
    print()

def nothing():
    "do nothing"

def print1beam():
    one_four_one(nothing, print_dash, print_plus)

def print1post():
    one_four_one(nothing, print_space, print_bar)

def print4beams():
    one_four_one(print_plus, print1beam, print_end)

def print4posts():
    one_four_one(print_bar, print1post, print_end)

def print_row():
    one_four_one(nothing, print4posts, print4beams)

def print_grid():
    one_four_one(print4beams, print_row, nothing)

print_grid()