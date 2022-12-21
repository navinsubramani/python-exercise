# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

li = [12,24,35,24,88,120,155,88,120,155]

li_new = []

for i in li:
    if i not in li_new:
        li_new.append(i)
print(li_new)