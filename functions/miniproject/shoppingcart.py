cart = {}

def add_product():
    product = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    cart[product] = {
        "price": price,
        "quantity": quantity
    }

    print("Product added.")

def remove_product():
    product = input("Enter product name: ")

    if product in cart:
        del cart[product]
        print("Product removed.")
    else:
        print("Product not found.")

def display_cart():
    if not cart:
        print("Cart is empty.")
    else:
        for product, details in cart.items():
            print(product, details)

def calculate_total():
    total = 0

    for details in cart.values():
        total += details["price"] * details["quantity"]

    return total

def checkout():
    print("Total Amount:", calculate_total())
    print("Checkout completed.")


while True:
    print("\n--- Shopping Cart ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Calculate Total")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_product()
    elif choice == 2:
        remove_product()
    elif choice == 3:
        display_cart()
    elif choice == 4:
        print("Total:", calculate_total())
    elif choice == 5:
        checkout()
    elif choice == 6:
        break
    else:
        print("Invalid choice")