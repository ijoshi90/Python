# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:38:46 2019

@author: akjoshi
"""

# Matrix Addition using Array

from numpy import *

mat = array (([1,2,3],[4,5,6],[7,8,9]),int)

mat1 = matrix(mat)
mat2 = matrix('1 2 3;4 5 6;7 8 9')

print ("\nMat 1")
print (mat1)

print ("\nMat 2")
print (mat2)

print ("\nMat1 Diagonal : " + str(diagonal(mat1)))
print ("\nMat2 Diagonal : " + str(diagonal(mat2)))
print ("\nMat1 Min : " + str(mat1.min()))
print ("\nMat2 Max : " + str(mat2.max()))

print ("\nAddition")
print (mat1 + mat2)

print ("\nMultiplication")
print (mat1 * mat2)