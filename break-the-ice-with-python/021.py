# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:

# 2

from math import sqrt
from turtle import distance


print("Type the robo directions:")
origin = [0, 0]
while True:
    a = input()
    if a == "":
        break

    direction, step = a.split(" ")

    if direction == "UP":
        origin[1] += int(step)

    elif direction == "DOWN":
        origin[1] -= int(step)

    elif direction == "LEFT":
        origin[0] -= int(step)

    elif direction == "RIGHT":
        origin[0] += int(step)

    else:
        break

distance = sqrt(origin[0]**2 + origin[1]**2)
print(int(distance))
