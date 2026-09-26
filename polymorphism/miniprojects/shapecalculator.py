class Circle:
    def calculate_area(self):
        radius = 5
        return 3.14 * radius * radius

class Rectangle:
    def calculate_area(self):
        length = 10
        width = 5
        return length * width

class Square:
    def calculate_area(self):
        side = 6
        return side * side

class Triangle:
    def calculate_area(self):
        base = 10
        height = 6
        return 0.5 * base * height


def calculate(shape):
    print("Area:", shape.calculate_area())


shapes = [Circle(), Rectangle(), Square(), Triangle()]

for shape in shapes:
    calculate(shape)