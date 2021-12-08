# Factorial Factory
# In mathematics, the factorial of integer 'n' is written as 'n!'. 
# It is equal to the product of n and every integer preceding it. For example: 5! = 1 x 2 x 3 x 4 x 5 = 120

# Your mission is simple: write a function that takes an integer 'n' and returns 'n!'.

# Note: 0! is always equal to 1. Negative values should return None.

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return None
    else:
        return n * factorial(n - 1)

print(factorial(10))

import math

def factorial1(n):
    if n < 0:
        return None
    return math.factorial(n)

print(factorial1(10))

# Lambda Function

import functools

def factorial2(n):
    if n > 0: return functools.reduce(lambda x,y: x*y, range(1,n+1))
    if n < 0: return None
    return 1

print(factorial2(10))