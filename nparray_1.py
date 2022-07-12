# 0-D arrays
import numpy as np
arr = np.array(45)
print(arr)


#1-D arrays

arr = np.array([1,2,3,4,5])
print(arr)


#2-D arrays : often used to represent matrix or 2nd order tensors

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


#3-D arrays : an array that has 2-D arrays(matrices) as its elements
# often used to represent 3rd order tensors

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# check number of dimensions

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



# output
#0
#1
#2
#3

# An array can have any number of dimensions, you can set it with the ndim argument


arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print('number of dimensions:', arr.ndmin)

"""
In this array the innermost dimension (5th dim) has 4 elements,
the 4th dim element that is the vector the 3rd dim has 1 element that is the matrix
with the vector, the 2nd dim has 1 element that is 3D array and the 1st dimension
has 1 element that is a 4D array

"""

