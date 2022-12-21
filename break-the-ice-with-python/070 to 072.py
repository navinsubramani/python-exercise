# 70. lease write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

import random

li = [2,4,6,8,10]
print(random.choice(li))

# 71. Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension

import random

li = [x for x in range(10, 151) if x%5 == 0 and x%7 == 0]
# print(li)
print(random.choice(li))


# 72. Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

import random

li = [x for x in range(100,201)]
print(random.sample(li, k=5))