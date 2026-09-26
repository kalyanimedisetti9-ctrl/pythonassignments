balance = 50000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Invalid withdrawal amount")

    if amount > balance:
        raise Exception("Insufficient balance")

    balance -= amount

    print("Withdrawal successful")
    print("Remaining Balance:", balance)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Error:", e)

finally:
    print("Transaction completed")