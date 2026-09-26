class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car(Vehicle):
    def display(self):
        print("Car")
        super().display()


class Bike(Vehicle):
    def display(self):
        print("Bike")
        super().display()


class Truck(Vehicle):
    def display(self):
        print("Truck")
        super().display()


car = Car("Toyota", "Fortuner")
bike = Bike("Yamaha", "R15")
truck = Truck("Tata", "Prima")

car.display()
print()

bike.display()
print()

truck.display()