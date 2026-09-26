text = "Hello Python"

for char in text:
    if char.isalpha() and char.lower() not in "aeiou":
        print(char)