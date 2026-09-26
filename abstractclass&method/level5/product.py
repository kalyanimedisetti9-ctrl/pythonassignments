class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

p = Product("Laptop", 50000, 2)

print("Product:", p.name)
print("Price:", p.price)
print("Quantity:", p.quantity)
print("Total Price:", p.total_price())