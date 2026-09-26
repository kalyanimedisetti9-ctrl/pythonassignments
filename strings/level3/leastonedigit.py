password = input("Enter password: ")

has_digit = False

for char in password:
    if char.isdigit():
        has_digit = True
        break

if has_digit:
    print("Password contains at least one digit")
else:
    print("Password does not contain a digit")