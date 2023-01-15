import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])
print(arr1)
print(arr1+arr2)
print(arr2-arr1)

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[10,20,30],[40,50,60]])
print(arr1+arr2)
print(arr2-arr1)

arr1 = np.array([1,2,3])
arr2 = np.array([[10,20,30],[40,50,60]])
print(arr1+arr2)
print(arr2-arr1)

print(arr1*arr2)

num1 = np.array([1,2,3])
print(num1+0.5)
print(num1-0.5)
