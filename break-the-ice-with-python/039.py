# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

from doctest import OutputChecker


INPUT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

OUTPUT = [x for x in INPUT if x % 2 == 0]
OUTPUT = tuple(OUTPUT)
print(OUTPUT)
