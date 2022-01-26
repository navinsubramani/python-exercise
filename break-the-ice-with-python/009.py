# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect

# Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT

li_a = []
while True:
    a = input('').upper()

    if a:
        li_a.append(a)
    else:
        break

for a in li_a:
    print(a)
