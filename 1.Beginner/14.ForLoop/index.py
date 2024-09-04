fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(f"x : {x}")
for x in "banana":
    print(f"x : {x}")
# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(f"x : {x}")
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(f"x : {x}")
# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(f"x : {x}")

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(f"x : {x}")
for x in range(2, 6):
    print(f"x : {x}")

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Else in For Loop
for x in range(6):
    print(x)  # 0
    break
else:  # Note: The else block will NOT be executed if the loop is stopped by a break statement.
    print("Finally finished!")
