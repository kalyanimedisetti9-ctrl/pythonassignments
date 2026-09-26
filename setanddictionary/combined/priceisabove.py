products = {
    "Laptop": 45000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 7000,
    "Printer": 6000
}

expensive_products = set()

for product, price in products.items():
    if price > 5000:
        expensive_products.add(product)

print("Products above ₹5000:")

for product in expensive_products:
    print(product)