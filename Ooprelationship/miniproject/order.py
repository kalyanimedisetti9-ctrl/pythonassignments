class Order:
    def show_order(self):
        print("This is an order")


class FoodOrder(Order):
    def place_order(self):
        print("Food order placed")


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self):
        self.menu_items = [
            MenuItem("Pizza", 300),
            MenuItem("Burger", 150),
            MenuItem("Biryani", 250)
        ]

    def show_menu(self):
        for item in self.menu_items:
            print(item.name, "₹", item.price)


class PaymentService:
    def pay(self, amount):
        print("Payment successful: ₹", amount)


class DeliveryService:
    def deliver(self, address):
        print("Food delivered to", address)


class FoodOrderService:
    def checkout(self):
        payment = PaymentService()
        payment.pay(300)

        delivery = DeliveryService()
        delivery.deliver("Rajahmundry")


restaurant = Restaurant()
restaurant.show_menu()

order = FoodOrder()
order.show_order()
order.place_order()

service = FoodOrderService()
service.checkout()