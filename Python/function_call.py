"""
Author: Akshay Joshi
GitHub: https://github.com/ijoshi90
Creation Date: 15.01.25

Description: [Add a description here]
"""
# Usage
# python3 function_call.py myfunction <String>
# python3 function_call.py myfunction HelloWorld

import sys

def myfunction1(mystring):
    print("My Function 1 - Normal String")
    print(mystring)

def myfunction2(mystring):
    print("My Function 2 - Reverse String")
    print(mystring[::-1])

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])