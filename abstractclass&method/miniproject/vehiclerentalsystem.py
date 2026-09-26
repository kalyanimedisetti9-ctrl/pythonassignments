from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def rent(self):
        pass

class Car(Vehicle):
    def rent(self):
        print(self.brand, "Car rented for ₹2000 per day")

class Bike(Vehicle):
    def rent(self):
        print(self.brand, "Bike rented for ₹800 per day")

class Scooter(Vehicle):
    def rent(self):
        print(self.brand, "Scooter rented for ₹600 per day")

vehicles = [
    Car("Toyota"),
    Bike("Yamaha"),
    Scooter("Honda")
]

for vehicle in vehicles:
    vehicle.rent()