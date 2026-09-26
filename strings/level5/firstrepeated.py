text = input("Enter a string: ")

found = False

for char in text:
    if text.count(char) > 1:
        print("First repeated character:", char)
        found = True
        break

if found == False:
    print("No repeated character")