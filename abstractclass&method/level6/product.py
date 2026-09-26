class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity

p = Product("Pen", 20)

print("Total Price:", p.total_price(5))