"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 04-Nov-19 at 19:00
https://www.hackerrank.com/challenges/kangaroo/problem
"""
met = "NO"
# Complete the kangaroo function below.
def calculateNext (current,jump):
    return current + jump

def kangaroo(x1, v1, x2, v2):
    #met = "NO"
    if (x1 >= 0) and (x2 > 0):
            if (v1 >= 1) and (v1 <= 10000):
                if (v2 >= 1 ) and (v2 <= 10000):
                    if (x1 > 10000) or (x2 >= 10000):
                        globals()['met'] = "NO"
                        return met
                    else:
                        if (x2 > x1) and (v2 > v1):
                            globals()['met'] = "NO"
                            return met
                        elif x1 == x2:
                            globals()['met'] = "YES"
                            return (met)
                        else:
                            x1 = calculateNext(x1,v1)
                            x2 = calculateNext(x2,v2)
                            kangaroo(x1, v1, x2, v2)
                        return met

result1 = kangaroo(0, 3, 4, 2)
print("Result 1 : {}".format(result1))

result2 = kangaroo(0, 2, 5, 3)
print("Result 2 : {}".format(result2))