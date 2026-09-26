class DeliveryService:
    def deliver(self, order_id, address):
        print(f"Order {order_id} will be delivered to {address}")


class FoodOrder:
    def __init__(self, order_id):
        self.order_id = order_id

    def place_delivery(self, address):
        delivery = DeliveryService()
        delivery.deliver(self.order_id, address)


order = FoodOrder(501)
order.place_delivery("Rajahmundry")