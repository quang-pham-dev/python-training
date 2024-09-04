# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.
i = 1
target = 6
while i < target:
    print(f"i : {i}")
    i += 1

# The break Statement
i = 4
target = 9
while i < target:
    print(f"The break Statement: i ==> {i}")
    if i == target - 3:
        break
    i += 1
# The continue Statement
i = 0
target = 6
while i < target:
    i += 1
    if i == 3:
        continue
    print(f"The continue Statement: i ==> {i}")
# The else Statement
i = 1
while i < 6:
    print(f"i : {i}")
    i += 1
else:
    print("i is no longer less than 6")
