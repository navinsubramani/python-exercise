# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

from ast import Pass


def print_bigword(x, y):
    if len(x) > len(y):
        print(x)
    elif len(y) > len(x):
        print(y)
    elif len(x) == len(y):
        print(x)
        print(y)
    else:
        Pass


print_bigword("Tree", "Ant")
print_bigword("Tree", "Antena")
print_bigword("Tree", "Frog")
