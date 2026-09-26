from abc import ABC, abstractmethod

class Delivery(ABC):

    @abstractmethod
    def calculate_delivery_charge(self):
        pass


class StandardDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 50


class ExpressDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 100


class SameDayDelivery(Delivery):
    def calculate_delivery_charge(self):
        return 150


deliveries = [
    StandardDelivery(),
    ExpressDelivery(),
    SameDayDelivery()
]

for delivery in deliveries:
    print("Delivery Charge:", delivery.calculate_delivery_charge())