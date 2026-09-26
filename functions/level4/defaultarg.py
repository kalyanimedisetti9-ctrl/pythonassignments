def total_price(price, tax=5):
    total = price + (price * tax / 100)
    return total

print("Total Price:", total_price(1000))