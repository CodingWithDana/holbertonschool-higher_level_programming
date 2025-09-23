from abc import ABC, abstractmethod
from math import pi # has math.pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return pi * self.radius * 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

# duck-typed function
def shape_info(shape):
    # assume shape has area() and perimeter()
    print("Area: ", shape.area())
    print("Perimeter: ", shape.perimeter())

# Instantiate a Circle and Rectangle
c = Circle(5)
r = Rectangle(4, 7)

# Pass each object to the shape_info function
shape_info(c)
shape_info(r)
