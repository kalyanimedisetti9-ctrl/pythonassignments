def create_bill():
    items = []
    total = 0

    while True:
        name = input("Enter product name (stop to finish): ")

        if name.lower() == "stop":
            break

        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        amount = price * quantity
        total += amount

        items.append([name, price, quantity, amount])

    with open("bill.txt", "w") as file:
        file.write("===== SHOPPING BILL =====\n")

        for item in items:
            file.write(
                f"{item[0]} - Price: {item[1]} "
                f"Qty: {item[2]} Total: {item[3]}\n"
            )

        file.write("-------------------------\n")
        file.write(f"Grand Total: {total}\n")

    print("Bill saved successfully")
    print("Grand Total:", total)


def display_bill():
    try:
        with open("bill.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Bill not found")


create_bill()
display_bill()