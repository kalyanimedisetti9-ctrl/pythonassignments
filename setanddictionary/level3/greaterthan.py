products = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000
}

print("Products above ₹1,000:")

for product, price in products.items():
    if price > 1000:
        print(product, ":", price)