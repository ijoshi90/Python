"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 30-Oct-19 at 18:24
"""
# Return the count of biggest numbers

def birthdayCakeCandles(ar):
    ar.sort()
    max1 = max(ar)
    count = ar.count(max1)
    return (count)

ar = [1,5,2,8,4,9,3,5,6,7,9]
result = birthdayCakeCandles(ar)
print(result)