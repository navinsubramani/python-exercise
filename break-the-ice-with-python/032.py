# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

def square_dict():
    a = {}
    for i in range(1, 21):
        a[i] = i**2
    print(a.keys())
    for k in a.keys():
        print(k)


square_dict()
