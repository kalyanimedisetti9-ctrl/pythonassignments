class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentGateway:
    def pay(self, amount):
        print(f"Payment of ₹{amount} successful")


class ShoppingCart:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Mouse", 1000)
        ]

    def checkout(self):
        total = sum(product.price for product in self.products)

        payment = PaymentGateway()
        payment.pay(total)


cart = ShoppingCart()
cart.checkout()