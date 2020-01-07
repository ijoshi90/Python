"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 27-Oct-19 at 19:04
"""

# Example of Armstrong number 153, 371 :
# Sum of cubes of all the numbers = number
number = int(input("Enter the number to check if its Armstrong Number or Not : "))

number_list = [] # Empty list
string_number = str(number)

# Split the numbers in to list
for i in range(len(string_number)):
    number_list.append(string_number[i])

# Calculate the sum of all the numbers
total = 0
for i in number_list:
    num = int(i)
    total = total + (num*num*num)

if number == total:
    print ("{} is an Armstrong Number".format(number))
else:
    print ("{} is not an Armstrong Number".format(number))