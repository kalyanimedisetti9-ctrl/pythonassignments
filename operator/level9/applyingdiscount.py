price = float(input("Enter product price: "))
discount = float(input("Enter discount percentage: "))

price -= price * discount / 100

print("Price after discount =", price)