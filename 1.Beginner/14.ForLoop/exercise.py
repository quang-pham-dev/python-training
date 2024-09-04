# ### Challenge 1: Printing Numbers (1 to 10)
# Write a program that uses a for loop and range() to print the numbers from 1 to 10 (inclusive).
for number in range(1, 11):
    print(number)


# ### Challenge 2: Counting Down (10 to 1)
# Write a program that uses a for loop and range() to print the numbers from 10 down to 1 (in descending order).
for number in range(10, 0, -1):
    print(number)

# ### Challenge 3: Even Numbers Only (1 to 10)
# Write a program that uses a for loop and range() to print only the even numbers between 1 and 10 (inclusive).
# (Hint: use the modulo operator % to check for evenness).
for number in range(1, 11):
    if number % 2 == 0:
        print(number)

# ### Challenge 4: Sum of Numbers (1 to 100)
# Write a program that uses a for loop and range() to calculate the sum of all numbers from 1 to 100 (inclusive).
