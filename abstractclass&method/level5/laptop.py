class Laptop:
    def __init__(self, brand, processor, ram, storage):
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display(self):
        print("Brand:", self.brand)
        print("Processor:", self.processor)
        print("RAM:", self.ram)
        print("Storage:", self.storage)

l = Laptop("HP", "Intel i5", "8GB", "512GB SSD")

l.display()