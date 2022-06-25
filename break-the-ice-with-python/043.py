# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

INPUT = range(1, 21)
OUTPUT = list(filter(lambda x: x % 2 == 0, INPUT))

print(OUTPUT)
