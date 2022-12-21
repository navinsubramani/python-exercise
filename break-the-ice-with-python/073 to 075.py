# 73. Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random

li = [x for x in range(100,201) if x%2==0]
print(random.sample(li, k=5))

# 74. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

import random

li = [x for x in range(1,1001) if x%5 ==0 and x%7==0]
print(li)
print(random.sample(li, k=5))

# 75. Please write a program to randomly print a integer number between 7 and 15 inclusive.

import random

print(random.choice(range(7,16)))