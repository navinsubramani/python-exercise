# Please write a program which accepts basic mathematic expression from console and print the evaluation result.
# Example: If the following n is given as input to the program: 35 + 3
# Then, the output of the program should be: 38

input_exp = input("Please enter a expression: ")

try:
    result = eval(input_exp)
    print(result)

except:
    print("The expression is not supported...")
