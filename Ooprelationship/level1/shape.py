class Shape:
    def display(self):
        print("This is a shape")


class Rectangle(Shape):
    def area(self, length, width):
        return length * width


rectangle = Rectangle()
rectangle.display()

print("Area =", rectangle.area(10, 5))