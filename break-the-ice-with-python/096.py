# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

# If the following string is given as input to the program:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

input_string = input("Enter the string input: ")
width = int(input("Enter the width: "))
index = 0

while index < len(input_string):
    print(input_string[index:index+width])
    index = index+width
