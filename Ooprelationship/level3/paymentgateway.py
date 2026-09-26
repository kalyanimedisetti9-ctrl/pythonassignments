class PaymentGateway:
    def process_payment(self, amount):
        print(f"Payment of ₹{amount} processed successfully")


class ShoppingCart:
    def __init__(self, total):
        self.total = total

    def checkout(self):
        gateway = PaymentGateway()
        gateway.process_payment(self.total)


cart = ShoppingCart(2500)
cart.checkout()