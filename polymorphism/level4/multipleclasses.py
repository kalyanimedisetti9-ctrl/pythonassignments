class Car:
    def start(self):
        print("Car started")

class Bike:
    def start(self):
        print("Bike started")

class Bus:
    def start(self):
        print("Bus started")


def start_vehicle(vehicle):
    vehicle.start()


start_vehicle(Car())
start_vehicle(Bike())
start_vehicle(Bus())