# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
from ast import Pass


lower, upper = 0, 0

for i in input("Enter a sentence: "):
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    else:
        Pass

print("UPPER CASE "+str(upper))
print("LOWER CASE "+str(lower))
