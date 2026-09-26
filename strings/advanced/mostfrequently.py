text = input("Enter a string: ")

most_frequent = text[0]
maximum = text.count(text[0])

for char in text:
    count = text.count(char)

    if count > maximum:
        maximum = count
        most_frequent = char

print("Most frequent character:", most_frequent)
print("Frequency:", maximum)