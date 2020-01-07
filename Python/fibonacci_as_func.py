"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 07-01-2020 at 13:51
"""
from time import *
def fibonacci(last,current):
    return last + current

fib_series = [0,1,1]
numbers = 100

print(time())

for i in range(numbers-3):
    fib_series.append(fibonacci(fib_series[-1],fib_series[-2]))

print(time())

#for each in fib_series:
#    print(each)

#print("Fibonacci Series : {}".format(fib_series))