class Rectangle:
    def area(self, length, width):
        return length * width

rectangle = Rectangle()

length = 10
width = 5

print("Length:", length)
print("Width:", width)
print("Area:", rectangle.area(length, width))