from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

class Bus(Vehicle):
    def start(self):
        print("Bus started")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()