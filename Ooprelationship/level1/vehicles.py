class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def drive(self):
        print("Car is driving")


class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


class Bus(Vehicle):
    def travel(self):
        print("Bus is travelling")


car = Car()
bike = Bike()
bus = Bus()

car.start()
car.drive()

bike.start()
bike.ride()

bus.start()
bus.travel()