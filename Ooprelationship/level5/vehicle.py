class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Engine:
    def start(self):
        print("Engine started")


class Car(Vehicle):
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


car = Car()
car.move()
car.start_car()