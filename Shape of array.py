import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

print(("with ndmin"))

ar = np.array([1, 2, 3, 4], ndmin=5)

print(ar)

print('shape of array :', ar.shape)

# shape
