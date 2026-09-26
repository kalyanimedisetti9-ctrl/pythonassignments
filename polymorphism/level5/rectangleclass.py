class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        return self.length * self.width == other.length * other.width


r1 = Rectangle(10, 5)
r2 = Rectangle(2, 25)

print(r1 == r2)