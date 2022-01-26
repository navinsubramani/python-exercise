# Write a program that accepts a sentence and calculate the number of letters and digits.

# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

from ast import Pass

digits, letters = 0, 0

for i in input("Enter a sentence: "):
    if i.isalpha():
        letters += 1

    elif i.isdecimal():
        digits += 1

    elif i.isspace():
        Pass

    else:
        Pass

print("LETTERS "+str(letters))
print("DIGITS "+str(digits))
