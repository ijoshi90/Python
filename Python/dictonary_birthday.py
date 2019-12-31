"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 19-12-2019 at 15:07
"""

names = {
    '1' : "Akshay",
    '2' : "Sangeetha",
    '3' : "Aadi Shankara"
}

birthdays = {
    "Akshay" : "27 April 1990",
    "Sangeetha" : "24 May 1991",
    "Aadi Shankara" : "27 April 2021"
}

print("DOB's we know .. ")

for each in names:
    print("{} : {}".format(each,names[each]))

selection = input("Whose Birthday do you want to see : ")

try:
    print("DOB of {} is {}".format(names[selection], birthdays[names[selection]]))
except:
    print("Invalid value selected, input should be a number from the displayed set")