"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 30-Oct-19 at 18:58
"""

# Convert from regular time to Military Time
def timeConversion(s):
    # If the time is in PM
    if s.find("PM") != -1:
        time_list = s.split(":",3)  #Split it at : in to 3 parts
        if time_list [0] == '12': # If its 12 PM, let it be 12 PM
            time_list [0] == "12"
        else: # Else add 12 to it and conver to 24 hours
            time_list [0] = str (int (time_list[0]) + 12)
            if int(time_list [0]) == 24:
                time_list[0] = "00"

    elif s.find("AM") != -1: # If its in AM
        time_list = s.split(":",3)
        if time_list[0] == "12": # If its 12 AM, change it 00
            time_list[0] = "00"

    # Convert the list to string
    time_str = ""
    for each in time_list:
        time_str = time_str + each + ":"
    s = time_str[:-1] # Strip the last :
    s = s[:-2]
    return s

s = "12:45:54PM"
result = timeConversion(s)
print (result)