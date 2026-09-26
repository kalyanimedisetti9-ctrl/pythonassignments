class Pizza:
    def calculate_price(self):
        return 250

class Burger:
    def calculate_price(self):
        return 150

class Biryani:
    def calculate_price(self):
        return 200

class Sandwich:
    def calculate_price(self):
        return 120


def show_price(food):
    print("Food Price:", food.calculate_price())


foods = [Pizza(), Burger(), Biryani(), Sandwich()]

for food in foods:
    show_price(food)