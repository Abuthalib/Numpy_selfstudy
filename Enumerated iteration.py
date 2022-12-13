import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
    print(idx,x)


print("2D array")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idy, y in np.ndenumerate(arr):
    print(idy, y)