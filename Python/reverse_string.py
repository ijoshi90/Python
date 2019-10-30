"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 29-Oct-19 at 18:45
"""

entered_string = input ("Enter the String : ")
reverse_list = []
iteration = len(entered_string)-1

while (iteration >= 0):
    reverse_list.append(entered_string[iteration])
    iteration -= 1

reverse_string=""
for each in reverse_list:
    reverse_string += each

print("Entered String : {}".format(entered_string))
print("Reversed String : {}".format(reverse_string))