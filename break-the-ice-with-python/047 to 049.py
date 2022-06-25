# 47 Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

from cmath import pi
from typing_extensions import Self


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 0.5*pi*self.radius*self.radius


a = Circle(10)
print(a.area())

# 48 Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width


b = Rectangle(5, 5)
print(b.area())


# 49 Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:

    def __init__(self) -> None:
        pass

    def area(self):
        return 0


class Square(Shape):

    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2


c = Square(2)
print(c.area())
