# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

def square(start, end):
    li = [i**2 for i in range(start, end+1)]
    print(tuple(li))


square(1, 20)
