# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:07:21 2019

@author: akjoshi
"""

class Person:
    def name(self):
        print ("Name")
    def age(self):
        print ("Age")
        
class Student (Person):
    def course(self):
        print ("Course")
        
# Multi Layer Inheritance    
class Intern (Student):
    def company(self):
        print ("Company")

class Employee ():
    def department(self):
        print ("Department")

# Multiple Inheritance        
class Director (Person, Employee):
    def board(self):
        print ("Director")
    
intern1 = Intern()
student1 = Student()
employee1 = Employee()
director1 = Director()

intern1.age()
intern1.name()
intern1.company()
intern1.course()

employee1.department()

director1.department()
director1.board()
director1.name()