"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 27-Oct-19 at 21:00
"""

number = int(input("Enter range for which sum of squares needs to be calculated : "))
sum = 0
list = ""
for i in range(number+1):
    sum += i*i
print ("Sum of Squares of {} numbers is {}".format(number,sum))