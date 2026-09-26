class Vehicle:
    def show_vehicle(self):
        print("This is a vehicle")


class Car(Vehicle):
    def drive(self):
        print("Car is being rented")


class Bike(Vehicle):
    def ride(self):
        print("Bike is being rented")


class Customer:
    def __init__(self, name):
        self.name = name


class PaymentService:
    def pay(self, amount):
        print("Rental payment: ₹", amount)


class Rental:
    def __init__(self):
        self.customer = Customer("Kalyani")
        self.vehicle = Car()

    def rent_vehicle(self):
        print("Customer:", self.customer.name)
        self.vehicle.drive()

        payment = PaymentService()
        payment.pay(2000)


rental = Rental()
rental.rent_vehicle()