text = input("Enter a string: ")

unique = True

for char in text:
    if text.count(char) > 1:
        unique = False
        break

if unique:
    print("String contains only unique characters")
else:
    print("String does not contain only unique characters")