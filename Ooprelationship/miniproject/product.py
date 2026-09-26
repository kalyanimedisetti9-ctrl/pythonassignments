class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Electronics(Product):
    def show_type(self):
        print("Electronic Product")


class Clothing(Product):
    def show_type(self):
        print("Clothing Product")


class PaymentService:
    def pay(self, amount):
        print("Payment of ₹", amount, "successful")


class DeliveryService:
    def deliver(self, address):
        print("Product delivered to", address)


class ShoppingCart:
    def __init__(self):
        self.products = [
            Electronics("Laptop", 50000),
            Clothing("Shirt", 1000)
        ]

    def checkout(self):
        total = sum(product.price for product in self.products)

        payment = PaymentService()
        payment.pay(total)

        delivery = DeliveryService()
        delivery.deliver("Rajahmundry")


cart = ShoppingCart()

for product in cart.products:
    print(product.name, product.price)

cart.checkout()