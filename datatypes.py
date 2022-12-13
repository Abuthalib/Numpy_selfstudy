import numpy as np

arr = np.array([1.1,1, 2.1, 3, 4.6, 5, 6])
newarr = arr.astype('bool')
print(newarr)
print(newarr.dtype)

# dtype
# value error
# astype()


# Below is a list of all data types in NumPy and the characters used to represent them.
#
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
