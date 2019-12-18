"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 18-12-2019 at 15:18
"""

# Iter in tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Iter in strings
string = "Akshay"
myit1 = iter(string)

print(next(myit1))
print(next(myit1))
print(next(myit1))
next(myit1)
next(myit1)
print(next(myit1))