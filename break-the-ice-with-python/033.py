# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def square(start, end):
    li = []
    for i in range(start, end+1):
        li.append(i**2)
    print(li)


square(1, 20)
