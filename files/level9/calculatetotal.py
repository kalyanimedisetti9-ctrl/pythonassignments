import json

with open("products.json", "r") as file:
    products = json.load(file)

total = 0

for product in products:
    value = product["price"] * product["quantity"]
    total += value

print("Total inventory value:", total)