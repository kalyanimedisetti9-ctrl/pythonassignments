class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price


product1 = Product("Laptop", 50000)
product2 = Product("Mouse", 1000)

total = product1 + product2

print("Combined Price:", total)