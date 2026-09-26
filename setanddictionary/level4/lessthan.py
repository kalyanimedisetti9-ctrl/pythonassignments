products = {
    "Laptop": 5,
    "Mouse": 15,
    "Keyboard": 7,
    "Monitor": 12
}

for product, quantity in products.items():
    if quantity < 10:
        print(product, quantity)