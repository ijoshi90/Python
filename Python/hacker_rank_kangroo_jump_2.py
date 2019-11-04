"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 04-Nov-19 at 19:00
https://www.hackerrank.com/challenges/kangaroo/problem
"""

def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if((x1+v1)==(x2+v2)):
            return "YES"
        x1+=v1
        x2+=v2
    return "NO"

result1 = kangaroo(0, 3, 4, 2)
print("Result 1 : {}".format(result1))

result2 = kangaroo(0, 2, 5, 3)
print("Result 2 : {}".format(result2))