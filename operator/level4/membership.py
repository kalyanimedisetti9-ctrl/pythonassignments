age = int(input("Enter age: "))
membership = input("Are you a member? (yes/no): ")

print("Eligible for discount:", age >= 60 or membership == "yes")