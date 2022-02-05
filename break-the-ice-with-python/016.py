# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

li_str = input(
    "Enter a sequence of number with comman seperation: ").split(",")
li_num = [int(x) for x in li_str]

li_odd_sqr = [str(x**2) for x in li_num if x % 2 == 1]

print(",".join(li_odd_sqr))
