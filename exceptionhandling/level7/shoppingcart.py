class InvalidProductError(Exception):
    pass


class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.products = ["Laptop", "Mouse", "Keyboard"]

    def add_product(self, product, quantity):
        try:
            if product not in self.products:
                raise InvalidProductError("Product not available")

            if quantity <= 0:
                raise InvalidQuantityError("Quantity must be greater than zero")

            print(quantity, product, "added to cart")

        except InvalidProductError as e:
            print("Error:", e)
        except InvalidQuantityError as e:
            print("Error:", e)


cart = ShoppingCart()
cart.add_product("Mouse", 2)
cart.add_product("Mobile", 1)
cart.add_product("Laptop", -2)