# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
from functools import reduce


def calc(acc, a):
    # print(acc)
    # print(a)
    result = acc + (a/(a+1))
    # print(result)
    return result


try:
    n = int(input("Enter a number: "))
    print(reduce(calc, range(1, n+1), 0))

except:
    print("please enter a valid number...")
