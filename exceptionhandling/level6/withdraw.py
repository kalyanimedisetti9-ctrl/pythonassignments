def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient balance")
        balance -= amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    except ValueError as e:
        print("Error:", e)

withdraw(5000, 2000)
withdraw(5000, 6000)