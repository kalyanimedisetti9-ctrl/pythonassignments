text = input("Enter a string: ")

duplicates = []

for char in text:
    if text.count(char) > 1 and char not in duplicates:
        duplicates.append(char)

print("Duplicate characters:", duplicates)