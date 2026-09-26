balance = 0
transactions = []

def deposit(amount):
    global balance
    balance += amount
    transactions.append("Deposited: " + str(amount))
    print("Amount deposited.")

def withdraw(amount):
    global balance

    if amount <= balance:
        balance -= amount
        transactions.append("Withdrawn: " + str(amount))
        print("Amount withdrawn.")
    else:
        print("Insufficient balance.")

def check_balance():
    print("Balance:", balance)

def transaction_history():
    print("\n--- Transaction History ---")

    if not transactions:
        print("No transactions.")
    else:
        for transaction in transactions:
            print(transaction)


while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        deposit(float(input("Enter amount: ")))
    elif choice == 2:
        withdraw(float(input("Enter amount: ")))
    elif choice == 3:
        check_balance()
    elif choice == 4:
        transaction_history()
    elif choice == 5:
        break
    else:
        print("Invalid choice")