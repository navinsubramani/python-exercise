# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# 34, 67, 55, 33, 12, 98
# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

while True:

    try:
        user_list = []
        user_input = input(
            "Enter a sequence of number with comma seperation: ")
        for n in user_input.split(','):
            int(n)
            user_list.append(n)
        user_tuple = tuple(user_list)

    except:
        print('Enter a valid sequence of number with comma seperation...')

    else:
        break

print(user_list)
print(user_tuple)
