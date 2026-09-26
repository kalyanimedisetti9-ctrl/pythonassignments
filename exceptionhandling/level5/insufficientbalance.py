class InsufficientBalanceError(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")

        self.balance -= amount
        print("Withdrawal successful")
        print("Remaining Balance:", self.balance)


try:
    account = BankAccount(50000)

    amount = float(input("Enter withdrawal amount: "))

    account.withdraw(amount)

except InsufficientBalanceError as e:
    print("Error:", e)