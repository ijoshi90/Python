"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 27-Oct-19 at 21:00
"""

number = int(input("Enter range for which sum of squares & Cubes needs to be calculated : "))
sum_square = 0
sum_cube = 0

for i in range(number+1):
    sum_square += i*i
    sum_cube += i*i*i
print ("Number {} : Sum of Squares is {} and Sum of Cubes is {}".format(number,sum_square,sum_cube))