# 85. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
remove_index = [0,4,5]
final_li = []

enumerate_li = [(i,x) for (i,x) in enumerate(li)]
for e in enumerate_li:
    if e[0] in remove_index:
        continue
    final_li.append(e[1])

print(final_li)

# 86. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

li = [12,24,35,24,88,120,155]
element = 24

while element in li:
    li.remove(element)
    print(li)