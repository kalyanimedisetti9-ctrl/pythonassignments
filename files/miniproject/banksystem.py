import csv


def transaction():
    account = input("Enter account number: ")
    transaction_type = input("Enter type (Deposit/Withdraw): ")
    amount = float(input("Enter amount: "))

    with open("transactions.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            account,
            transaction_type,
            amount
        ])

    print("Transaction saved successfully")


def display_transactions():
    try:
        with open("transactions.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(
                    "Account:", row[0],
                    "| Type:", row[1],
                    "| Amount:", row[2]
                )

    except FileNotFoundError:
        print("No transactions found")


while True:
    print("\n1. Add Transaction")
    print("2. Display Transactions")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        transaction()
    elif choice == "2":
        display_transactions()
    elif choice == "3":
        break
    else:
        print("Invalid choice")