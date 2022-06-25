# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

ascii_input = input("Enter a ASCII string: ")

print(ascii_input.encode("utf-8"))
