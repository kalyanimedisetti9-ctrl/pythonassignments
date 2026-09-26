class BankAccount:
    bank_name = "State Bank of India"

    def __init__(self, account_number, holder, balance):
        self.account_number = account_number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

    def display(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


account = None

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Account Details")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        number = input("Enter Account Number: ")
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Initial Balance: "))
        account = BankAccount(number, name, balance)
        print("Account created")

    elif choice == 2:
        amount = float(input("Enter amount: "))
        account.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount: "))
        account.withdraw(amount)

    elif choice == 4:
        account.check_balance()

    elif choice == 5:
        account.display()

    elif choice == 6:
        break

    else:
        print("Invalid choice")