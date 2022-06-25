# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.

def f(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = f(n-1)+f(n-2)
    return result


n = int(input("Enter n: "))
li = [str(f(i)) for i in range(0, n+1)]
print(",".join(li))
