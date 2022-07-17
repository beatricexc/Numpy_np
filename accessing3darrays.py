
#Access the element on the first row, second column:

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column.

print('2n element on 1st row: ', arr[0,1])

#Access the element on the second row, 5th column:

print('5th element on 2nd row: ', arr[1,4])

# Access 3d arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access the third element of the second array of the first array:

print(arr[0, 1, 2])

"""
arr[0, 1, 2] prints the value 6.

And this is why:

The first number represents the first dimension, which contains two arrays:
[[1, 2, 3], [4, 5, 6]]
and:
[[7, 8, 9], [10, 11, 12]]
Since we selected 0, we are left with the first array:
[[1, 2, 3], [4, 5, 6]]

The second number represents the second dimension, which also contains two arrays:
[1, 2, 3]
and:
[4, 5, 6]
Since we selected 1, we are left with the second array:
[4, 5, 6]

The third number represents the third dimension, which contains three values:
4
5
6
Since we selected 2, we end up with the third value:
6
"""
