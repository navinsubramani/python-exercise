'''
Given a number N.Find Sum of 1 to N Using Recursion

Input

5
Output

15'''

in_num = int(input("Input: "))

sum = 0
for i in range(1, in_num+1):
    sum+=i

print(f'Output: {sum}')

'''
def rec(n):
    if n == 0:
        return n
    return rec(n-1) + n


n = int(input())
sum = rec(n)
print(sum)'''