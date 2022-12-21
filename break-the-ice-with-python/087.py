# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

li1 = [1,3,6,78,35,55]
li2 = [12,24,35,24,88,120,155]

#soliton1
li_intersect = []
for i in li1:
    if i in li2:
        li_intersect.append(i)
print(li_intersect)

#solution2
set1= set(li1)
set2= set(li2)
intersection = set1 & set2
print(intersection)

