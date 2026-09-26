try:
    balance = 50000
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient balance")

    balance -= amount

    print("Withdrawal successful")
    print("Remaining Balance:", balance)

except Exception as e:
    print("Error:", e)