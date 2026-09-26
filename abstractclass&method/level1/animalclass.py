from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

d = Dog()
c = Cat()

d.sound()
c.sound()