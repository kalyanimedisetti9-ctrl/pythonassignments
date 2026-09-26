class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

class Cow:
    def sound(self):
        print("Cow moos")


def animal_sound(animal):
    animal.sound()


animal_sound(Dog())
animal_sound(Cat())
animal_sound(Cow())