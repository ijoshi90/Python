"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 30-Oct-19 at 08:06
"""

# Complete the staircase function below.
"""def staircase(n):
    for stairs in range(1, n + 1):
        print(('#' * stairs).rjust(n))
"""
def staircase(n):
    for i in range(n-1,-1,-1):
        for j in range(i):
            print (" ",end="")
        for k in range(n-i):
            print("#",end="")
        print("")

if __name__ == '__main__':
    staircase(6)