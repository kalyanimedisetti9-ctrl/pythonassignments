class Car:
    def start(self):
        print("Car started")

class Bike:
    def start(self):
        print("Bike started")

class Bus:
    def start(self):
        print("Bus started")

class Truck:
    def start(self):
        print("Truck started")


def start_vehicle(vehicle):
    vehicle.start()


vehicles = [Car(), Bike(), Bus(), Truck()]

for vehicle in vehicles:
    start_vehicle(vehicle)