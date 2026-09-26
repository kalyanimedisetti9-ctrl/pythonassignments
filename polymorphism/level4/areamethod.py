class Rectangle:
    def area(self):
        return 10 * 5

class Circle:
    def area(self):
        return 3.14 * 7 * 7

class Triangle:
    def area(self):
        return 0.5 * 10 * 6


def calculate_area(shape):
    print("Area:", shape.area())


calculate_area(Rectangle())
calculate_area(Circle())
calculate_area(Triangle())