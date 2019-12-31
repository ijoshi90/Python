"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 13-11-2019 at 19:01
"""

# Fibonacci

# 0 1 1 2 3 5 8 11...

max = 10
first = 0
second = 1
fibonacci = []

fibonacci.append(first)
fibonacci.append(second)

# Code
for i in range (max - 2):
    next = first + second
    fibonacci.append(next)
    first = second
    second = next

print(fibonacci)