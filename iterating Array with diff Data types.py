#Iterating Array With Different Data Types
import numpy as np

arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'],op_dtypes=['S']):
    print(x)

#Iterating With Different Step Size
print("Iterating With Different Step Size")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:,::3]):
    print(x)