'''Write a Python program that accepts a string and calculate the number of digits and letters.

Input

Hello321Bye360
Output

Digit - 6
Letter - 8'''

in_string = input("Enter the input string: ")
Digit = 0
Letter = 0

for i in in_string:
    if i.isdigit():
        Digit+= 1
    elif i.isalpha():
        Letter+= 1

print(f'Digit - {Digit}\nLetter - {Letter}')
