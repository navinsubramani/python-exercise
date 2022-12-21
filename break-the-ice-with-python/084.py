# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

x,y,z = 3,5,8

li_3D = [[[0 for i in range(x)] for j in range(y)] for k in range(z)]
print(li_3D)