class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                break

    def total(self):
        total = 0

        for product in self.products:
            total += product[1]

        return total

cart = ShoppingCart()

cart.add_product("Pen", 20)
cart.add_product("Book", 100)
cart.add_product("Bag", 500)

print("Total:", cart.total())

cart.remove_product("Pen")

print("Total after removing Pen:", cart.total())