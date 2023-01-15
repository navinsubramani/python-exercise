import numpy as np

# Creation of array: Dimesnion & hape is important during creation.

# Creation from a list
li = [1,2,3,4,5]
arr = np.array(li)
print(arr, arr.ndim, arr.shape, sep=" ")

li = [1.04,2.1,3,4.2,5.9]
arr = np.array(li)
print(arr, arr.ndim, arr.shape, sep=" ") # all element will be converted to float even one is int

multili = [[1.04,2.1,3,4.2,5.9],[1,2,3,4,5]]
arr = np.array(multili)
print(arr, arr.ndim, arr.shape, sep=" ")


# np.zeros - creates array and initializes with 0
# np.empty - cretes arrays without initialization

print(np.zeros(10))
print(np.empty((2,1,2)))