text = input("Enter a string: ")

result = ""

for char in text:
    if char.isalnum() or char.isspace():
        result += char

print("After removing punctuation:", result)