# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).

n = int(input("Enter n: "))

acc = 0
for i in range(0, n+1):
    if i is 0:
        acc = 0
    else:
        acc = acc + 100
    print(f"f({i}) = {acc}")
