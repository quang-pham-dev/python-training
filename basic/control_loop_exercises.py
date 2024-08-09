# Exercise 1: Write a function to check if a number is prime.
# A prime number is a natural number greater than 1 that has no positive divisors other than
# 1 and itself. In other words, a prime number is a number that can only be divided evenly by
# 1 and the number itself.
# For example:


# 2 is a prime number because its only divisors are 1 and 2.
# 3 is a prime number because its only divisors are 1 and 3.
# 5 is a prime number because its only divisors are 1 and 5.

import math


def is_prime_optimized(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


print(f"is_prime: {is_prime_optimized(11)}")  # Outputs True
print(f"is_prime: {is_prime_optimized(15)}")  # Outputs False


# Exercise 2: Write a function to return a list of Fibonacci numbers less than n.
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# Test the function
print(f"fibonacci : {fibonacci(10)}")  # Outputs [0, 1, 1, 2, 3, 5, 8]
