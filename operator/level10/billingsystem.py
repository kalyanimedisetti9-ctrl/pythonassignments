bill = 0

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

bill += item1
bill += item2
bill += item3

if bill >= 5000 and bill < 10000:
    discount = 10
elif bill >= 10000:
    discount = 20
else:
    discount = 0

discount_amount = bill * discount / 100
bill -= discount_amount

print("Discount =", discount_amount)
print("Final Bill =", bill)