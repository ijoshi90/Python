"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 10-Sep-19 at 21:31
"""
print (__name__)

def add (*num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum

def sub (*num):
    diff = 0
    for i in num:
        diff = diff - i
    return diff

def mul (*num):
    res = 1
    for i in num:
        res = res * i
    return res

def div (*num):
    res = 1
    for i in num:
        res = res / i
    return res