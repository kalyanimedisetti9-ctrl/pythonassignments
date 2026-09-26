sentence = input("Enter a sentence: ")

words = sentence.split()

characters = 0
digits = 0
vowels = 0
spaces = 0

for char in sentence:
    if char.isalpha():
        characters += 1

    if char.isdigit():
        digits += 1

    if char.lower() in "aeiou":
        vowels += 1

    if char == " ":
        spaces += 1

print("Words:", len(words))
print("Characters:", characters)
print("Digits:", digits)
print("Vowels:", vowels)
print("Spaces:", spaces)