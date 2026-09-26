from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def calculate_charge(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

class StandardDelivery(Delivery):
    def calculate_charge(self):
        print("Standard Delivery Charge: 50")

    def deliver(self):
        print("Delivered by Standard Delivery")

class ExpressDelivery(Delivery):
    def calculate_charge(self):
        print("Express Delivery Charge: 100")

    def deliver(self):
        print("Delivered by Express Delivery")

s = StandardDelivery()
e = ExpressDelivery()

s.calculate_charge()
s.deliver()
e.calculate_charge()
e.deliver()