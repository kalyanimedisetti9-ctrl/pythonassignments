class Room:
    def show(self):
        print("This is a room")


class House:
    def __init__(self):
        self.room1 = Room()
        self.room2 = Room()

    def display(self):
        print("House has two rooms")
        self.room1.show()
        self.room2.show()


house = House()
house.display()