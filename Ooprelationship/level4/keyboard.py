class Keyboard:
    def type_text(self):
        print("Typing using keyboard")


class Laptop:
    def __init__(self):
        self.keyboard = Keyboard()

    def use_laptop(self):
        self.keyboard.type_text()
        print("Laptop is being used")


laptop = Laptop()
laptop.use_laptop()