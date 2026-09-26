text = input("Enter a string: ")

for char in text:
    if text.count(char) == 1:
        print("First non-repeated character:", char)
        break