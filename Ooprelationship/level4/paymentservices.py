class PaymentService:
    def process_payment(self, amount):
        print(f"Payment of ₹{amount} processed")


class Order:
    def __init__(self, amount):
        self.amount = amount

    def place_order(self):
        payment = PaymentService()
        payment.process_payment(self.amount)
        print("Order placed successfully")


order = Order(1500)
order.place_order()