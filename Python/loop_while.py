# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:47:00 2019

@author: akjoshi
"""
import time
# While Loop
x = 5
y = 1
 
print (time.timezone)

while x >=1:
    print (time.localtime())
    time.sleep (1)
    print ("X is "+ str (x))
    x-=1
    while y <= 5:
        time.sleep(1)
        print ("Y is "+str(y))
        y+=1
        
# While Loop

i=0

while i <=10:
    i=i+1
    if i == 5:
        break
    print ("I is "+str(i))

j = 0
while j < 6:
    j += 1 
    if j == 3:
        continue
    print ("J is "+str(j))
    