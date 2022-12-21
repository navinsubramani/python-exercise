# 80. Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

li = [5,6,77,45,22,12,24]
print([i for i in li if i%2==1])

# 81. By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
print([i for i in li if not(i%5==0 and i%7==0)])

# 82. By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
remove_index = [0,2,4,6]
final_li = []

enumerate_li = [(i,x) for (i,x) in enumerate(li)]
for e in enumerate_li:
    if e[0] in remove_index:
        continue
    final_li.append(e[1])

print(final_li)

# 83. By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
remove_index = range(2,5)
final_li = []

enumerate_li = [(i,x) for (i,x) in enumerate(li)]
for e in enumerate_li:
    if e[0] in remove_index:
        continue
    final_li.append(e[1])

print(final_li)
