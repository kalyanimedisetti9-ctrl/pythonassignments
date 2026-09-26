class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

c = Car("Toyota", "Innova")

c.display()
c.start()
c.stop()