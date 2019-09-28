# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:57:17 2019

@author: akjoshi
"""

# Operators

a=11
b=5
c=6
d=9

print ("Arithmetic")
print ("A : "+str(a)+" & B : "+str(b))
print ("+ : " + str(a+b))
print ("- : " + str(a-b))
print ("* : " + str(a*b))
print ("/ : " + str(a/b))
print ("% : " + str(a%b))
print ("** : " + str(a**b)) # Exponention
print ("// : " + str(a/b)) # Floor division

print ("Assignment")
a+=3
b-=3
c*=3
d/=3
e=50
f=100

print ("+= : " + str(a))
print ("-= : " + str(b))
print ("*= : " + str(c))
print ("/= : " + str(d))
print ("+= : " + str(e))
print ("+= : " + str(f))

# Identity
print (e is f)
print (e is not f)

# Membership
str1="abcdef"
str2="bcd"
str3="zzz"

print(str2 in str1)
print(str3 in str1)