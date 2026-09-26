text = input("Enter a string: ")

unique = []

for char in text:
    if text.count(char) == 1:
        unique.append(char)

print("Unique characters:", unique)