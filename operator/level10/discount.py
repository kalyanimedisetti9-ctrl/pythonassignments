amount = float(input("Enter shopping amount: "))

if amount >= 5000:
    discount = 20
elif amount >= 2000:
    discount = 10
else:
    discount = 0

if discount > 0 and amount >= 2000:
    discount_amount = amount * discount / 100
    final_amount = amount - discount_amount
else:
    discount_amount = 0
    final_amount = amount

print("Discount =", discount_amount)
print("Final Amount =", final_amount)