class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def __add__(self, other):
        return ShoppingCart(self.total + other.total)


cart1 = ShoppingCart(1500)
cart2 = ShoppingCart(2500)

cart3 = cart1 + cart2

print("Combined Cart Total:", cart3.total)