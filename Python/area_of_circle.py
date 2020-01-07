"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 27-Oct-19 at 20:35
"""

#from math import pi
from math import pi

def calculate_area():
    radius = float(input("Enter Radius of Circle : "))
    print ("Area of the Circle with Radius {} is {}".format(radius,pi*radius*radius))

calculate_area()