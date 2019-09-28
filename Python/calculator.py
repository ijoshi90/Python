# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:02:55 2019

@author: akjoshi
"""
from unittest.main import _convert_name
print ("Module is : " + __name__)

class Calculaltor:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2
    
    def add (self):
        print (self.n1 + self.n2)
    def sub (self):
        print (self.n1 - self.n2)
    def mul (self):
        print (self.n1 * self.n2)
    def div (self):
        print (self.n1 / self.n2)

# __name__
if __name__ == '__main__':
# Object Constructor
    cal1 = Calculaltor(4,2)
    cal1.add()
    cal1.sub()
    cal1.mul()
    cal1.div()