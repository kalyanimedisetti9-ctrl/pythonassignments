class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append([name, price, quantity])

    def display_products(self):
        for product in self.products:
            print(
                "Product:", product[0],
                "| Price:", product[1],
                "| Quantity:", product[2]
            )

    def calculate_total(self):
        total = 0

        for product in self.products:
            total += product[1] * product[2]

        return total


cart = ShoppingCart()

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 1000, 2)
cart.add_product("Keyboard", 2000, 1)

cart.display_products()

print("Total Bill:", cart.calculate_total())