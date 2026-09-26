from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle:", 10 * 5)

    def perimeter(self):
        print("Perimeter of Rectangle:", 2 * (10 + 5))

class Circle(Shape):
    def area(self):
        print("Area of Circle:", 3.14 * 5 * 5)

    def perimeter(self):
        print("Perimeter of Circle:", 2 * 3.14 * 5)

r = Rectangle()
c = Circle()

r.area()
r.perimeter()
c.area()
c.perimeter()