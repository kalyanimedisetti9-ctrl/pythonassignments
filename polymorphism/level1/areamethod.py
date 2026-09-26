class Rectangle:
    def area(self):
        length = 10
        width = 5
        return length * width

class Circle:
    def area(self):
        radius = 7
        return 3.14 * radius * radius


shapes = [Rectangle(), Circle()]

for shape in shapes:
    print("Area:", shape.area())