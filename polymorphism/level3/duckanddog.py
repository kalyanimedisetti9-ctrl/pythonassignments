class Duck:
    def walk(self):
        print("Duck is walking")

class Dog:
    def walk(self):
        print("Dog is walking")


def make_walk(animal):
    animal.walk()


make_walk(Duck())
make_walk(Dog())