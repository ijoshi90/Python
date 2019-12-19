"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 19-12-2019 at 14:47
"""

a = 2500
b = 1000
c = 2500
bigger = 0

if (a > b) & (a > c):
    bigger = a
elif (b > a) & (b > c):
    bigger = b
elif (c > a) & (c > b):
    bigger = c
else:
    bigger = 0

if bigger == 0:
    print("Atlease two are same")
else:
    print("{} is biggest of all".format(bigger))