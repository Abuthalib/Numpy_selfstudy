import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print('Reshape from 1D-2D')
print(newarr)

print('From 1-D to 3D')
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr1.reshape(2, 3, 2)
print(newarr1)

print("copy or view")

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

print('Convert 1D array with 8 elements to 3D array with 2x2 elements:')

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

print('Flattening the arrays')
arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)

# flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud
