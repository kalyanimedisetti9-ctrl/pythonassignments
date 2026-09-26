class HomeDelivery:
    def deliver(self):
        print("Product delivered to home")

class StoreDelivery:
    def deliver(self):
        print("Product delivered to store")

class ExpressDelivery:
    def deliver(self):
        print("Product delivered by express service")


def process_delivery(delivery):
    delivery.deliver()


process_delivery(HomeDelivery())
process_delivery(StoreDelivery())
process_delivery(ExpressDelivery())