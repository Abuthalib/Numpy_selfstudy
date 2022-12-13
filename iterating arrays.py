import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

print("iterating 2-D array")

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    print(x)


print('Iterate on each scalar element of the 2-D array:')

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y)


print('Iterate on the elements of the following 3-D array:')

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print("x represent the 2d array")
    print(x)

print('To return the actual values, the scalars, we have to iterate the arrays in each dimension.')

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for z in y:
            print(z)