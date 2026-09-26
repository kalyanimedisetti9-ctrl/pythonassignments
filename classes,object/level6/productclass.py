class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def total_price(self, quantity):
        return self.price * quantity

product = Product("Laptop", 50000)

quantity = 2

print("Product:", product.name)
print("Price:", product.price)
print("Quantity:", quantity)
print("Total Price:", product.total_price(quantity))