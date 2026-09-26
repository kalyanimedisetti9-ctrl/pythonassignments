class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "-", self.price)


class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 500),
            Product("Keyboard", 1000)
        ]

    def display_cart(self):
        print("Shopping Cart:")
        for product in self.products:
            product.display()


cart = ShoppingCart()
cart.display_cart()