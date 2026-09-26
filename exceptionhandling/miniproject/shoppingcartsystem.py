class InvalidProductError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.products = {
            "Laptop": 5,
            "Mouse": 10,
            "Keyboard": 3
        }

    def add_to_cart(self, product, quantity):
        try:
            if product not in self.products:
                raise InvalidProductError("Product not found")

            if quantity <= 0:
                raise InvalidQuantityError("Invalid quantity")

            if quantity > self.products[product]:
                raise InsufficientStockError("Insufficient stock")

            self.products[product] -= quantity

            print(quantity, product, "added to cart")
            print("Remaining stock:", self.products[product])

        except InvalidProductError as e:
            print("Error:", e)
        except InvalidQuantityError as e:
            print("Error:", e)
        except InsufficientStockError as e:
            print("Error:", e)


cart = ShoppingCart()

cart.add_to_cart("Mouse", 2)
cart.add_to_cart("Mobile", 1)
cart.add_to_cart("Laptop", -1)
cart.add_to_cart("Keyboard", 10)