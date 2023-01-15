import numpy as np

# If datatype is not specified while creation, numpy will auto assign the datatype
li = [1,2,3,4,5]
arr = np.array(li, dtype=np.float64)
print(arr, arr.ndim, arr.shape, sep=" ")

li = [1.98,2.49,3,4.5,5]
arr = np.array(li, dtype=np.int32)
print(arr, arr.ndim, arr.shape, sep=" ")

# Casting the datatype
arr = arr.astype(np.float64)
print(arr, arr.ndim, arr.shape, sep=" ")

# Below are the ways to get the different properties of a array
arr.ndim
arr.shape
arr.size
arr.itemsize
arr.nbytes
arr.dtype