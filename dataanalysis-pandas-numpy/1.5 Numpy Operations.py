'''

Numpy Usecases:

DataScience: in data ingestion, visualization, modeling, report in dashboard
Machine learning: scikit-learn, Scipy, TensorFlow
Others: Array libraries like DASK, Cupy, etc
Visualization: Matplotlib, Seaborn, Plotly

NumPy uses C so it is much faster and manages the memory better than native Python function. Works best with multi dimesional array.

'''



import numpy as np

# Refer to numpy.org for more functions.

# Create a numpy array from list
x = np.array([1,2,3,4,5])

# Initialize a numpy array
np.zeros(10)
np.ones(5)
np.zeros((10,10))
np.empty((2,3,2))

# Creating a array with datatype. This is different from native python where datatype can be specified during initialization.
np.array([1,2,3,4,5], dtype= np.float64)

# Casting the type of array
x = np.array([1,2,3,4], dtype=np.float64)
x.astype(dtype=np.int32)

# Arithmetic Operations
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6]])
arr = x*y
print(arr)

# Indexing & Slicing one dimension
print(arr[1:])

# Propagation & Broadcast
arr[1:] = [1,2,3]
print(arr)

# Row and Column Slicing

# Update Matrix Elements
arr[arr < 3] = 0
print(arr)

# Fanxy Indexing
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
x[1] # get first row
x[1,2] # gets first row and second column
x[[0,1]] # gets multiple rows
x[[1,2],[0,1]] # gets multiple rowns and multiple column

# Fancy Indixing using pipe
x[[0,1]][:,[1]]

# Reshape & Transponse
arr = np.ones(32).reshape(8,4)
arr.transpose()
