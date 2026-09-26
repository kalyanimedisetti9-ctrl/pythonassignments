class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentService:
    def pay(self, amount):
        print(f"Payment of ₹{amount} successful")


class DeliveryService:
    def deliver(self, address):
        print(f"Order delivered to {address}")


class OnlineOrder:
    def __init__(self):
        self.products = [
            Product("Laptop", 50000),
            Product("Keyboard", 1500)
        ]

    def place_order(self):
        total = sum(product.price for product in self.products)

        payment = PaymentService()
        payment.pay(total)

        delivery = DeliveryService()
        delivery.deliver("Rajahmundry")


order = OnlineOrder()
order.place_order()