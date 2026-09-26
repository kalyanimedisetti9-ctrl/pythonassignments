try:
    number = int(input("Enter a number: "))

    if number <= 0:
        raise ValueError("Number must be positive")

    print("Valid positive number:", number)

except ValueError as e:
    print("Error:", e)