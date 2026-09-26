from abc import ABC, abstractmethod

class Delivery(ABC):
    @abstractmethod
    def deliver(self):
        pass

class BikeDelivery(Delivery):
    def deliver(self):
        print("Food delivered by Bike")

class CarDelivery(Delivery):
    def deliver(self):
        print("Food delivered by Car")

class DroneDelivery(Delivery):
    def deliver(self):
        print("Food delivered by Drone")

deliveries = [BikeDelivery(), CarDelivery(), DroneDelivery()]

for delivery in deliveries:
    delivery.deliver()