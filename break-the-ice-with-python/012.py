# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

from ast import Pass


def is_all_even(num):
    num_in_str = str(num)
    all_even = True
    for i in range(len(str(num_in_str))):
        if int(num_in_str[i]) % 2 == 0:
            Pass
        else:
            all_even = False
            break
    return all_even


start = 1000
stop = 3000
even_list = []

# even_list = list(filter(is_all_even, [range(start, stop+1)]))
for x in range(start, stop+1):
    if is_all_even(x):
        even_list.append(str(x))

print(",".join(even_list))
