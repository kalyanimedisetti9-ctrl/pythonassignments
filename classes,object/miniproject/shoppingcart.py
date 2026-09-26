class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("Product removed")
                return
        print("Product not found")

    def view_cart(self):
        for product in self.products:
            print(product.name, product.price, product.quantity)

    def checkout(self):
        total = 0
        for product in self.products:
            total += product.total()
        print("Total Bill:", total)


cart = ShoppingCart()

cart.add_product(Product("Laptop", 50000, 1))
cart.add_product(Product("Mouse", 1000, 2))
cart.add_product(Product("Keyboard", 2000, 1))

print("\nCart:")
cart.view_cart()

cart.remove_product("Mouse")

print("\nUpdated Cart:")
cart.view_cart()

print()
cart.checkout()