import numpy as np

arr = np.array([1, 2, 3, 4, 5, ])
x = arr.copy()
arr[0] = 13
print("COPY OF ARRAY")
print(arr)
print(x)

print("view OF ARRAY")

arr1 = np.array([6, 7, 8, 9, 0])
y = arr1.view()
arr1[0] = 43

print(arr1)
print(y)

print("Using Base")
print(x.base)
print(y.base)

# copy()
# view()
# base
