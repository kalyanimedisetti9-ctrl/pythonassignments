class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a key")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()