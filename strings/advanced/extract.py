text = input("Enter a string: ")

numbers = ""

for char in text:
    if char.isdigit():
        numbers += char

print("Numbers:", numbers)