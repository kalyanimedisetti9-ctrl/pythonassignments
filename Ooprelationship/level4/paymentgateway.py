class PaymentGateway:
    def make_payment(self, amount):
        print(f"Payment of ₹{amount} successful")


class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def checkout(self):
        gateway = PaymentGateway()
        gateway.make_payment(self.total)


cart = ShoppingCart(2500)
cart.checkout()