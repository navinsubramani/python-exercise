# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

try:
    num = int(input('Find the Factorial for the given number: '))

    result = 1
    for i in range(num):
        result = result*(i+1)
    print(result)

except:
    print('Enter a number...')
