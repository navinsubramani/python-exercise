# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re

li = input("Enter a sentance: ").split(" ")
digits = re.compile(r"\d+")

print(list(filter(lambda x: digits.fullmatch(x) is not None, li)))
