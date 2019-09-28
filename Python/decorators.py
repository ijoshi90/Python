"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 10-Sep-19 at 21:02
"""

# Add extra features to existing functions

def div (a,b):
    print (a/b)

def smart_div (func):
    def inner (a,b):
        if b > a:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(4,8)
div(12,5)