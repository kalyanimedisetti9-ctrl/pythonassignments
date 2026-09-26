class Food:
    def prepare(self):
        print("Preparing food")

class Pizza(Food):
    def prepare(self):
        print("Preparing Pizza")

class Burger(Food):
    def prepare(self):
        print("Preparing Burger")

class Biryani(Food):
    def prepare(self):
        print("Preparing Biryani")


foods = [Pizza(), Burger(), Biryani()]

for food in foods:
    food.prepare()