# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

def square(start, end):
    li = [i**2 for i in range(start, end+1)]
    print(li[0:5])


square(1, 20)
