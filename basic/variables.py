x = 10  # x is of type int
y = "Quang Pham"  # x is now of type str
z = "Quang Pham"  # Single or Double Quotes is same

# Print value
print(x)
print(y)
print(z)

# Get the type
print(type(x))
print(type(y))

# Casting
i = 10
j = "Quang Pham"
k = True

i = str(3)  # i will be '3'
j = int(3)  # j will be 3
k = float(3)  # k will be 3.0
print(i, j, k)
print(type(i))
print(type(j))
print(type(k))

# Assign multiple variables
a, b, c = 1, "String", 3.0
print(a)
print(b)
print(c)

# One Value to Multiple Variables
e = f = g = "Simple"
print(e, f, g)


# Unpack a Collection'
skills = ["Flask", "Django", "FastAPI"]
l, m, n = skills
print(l, m, n)

# Global variable
# global keyword
global o
