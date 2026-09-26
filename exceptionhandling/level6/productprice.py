def calculate_price(price, quantity):
    try:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        total = price * quantity
        print("Total price:", total)

    except ValueError as e:
        print("Error:", e)

calculate_price(100, 5)
calculate_price(100, -2)