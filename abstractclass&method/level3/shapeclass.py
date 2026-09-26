from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        r = 5
        print("Area of Circle:", 3.14 * r * r)

c = Circle("Red")

print("Color:", c.color)
c.area()