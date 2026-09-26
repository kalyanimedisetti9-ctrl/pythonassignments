class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Kalyani", 50000)

account.display_balance()

account.withdraw(20000)
account.display_balance()

account.withdraw(40000)
account.display_balance()