"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 20-12-2019 at 11:29
"""

# Fibonacci
max = int(input("Enter the number to print Fibonacci series : "))

#max = 10
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