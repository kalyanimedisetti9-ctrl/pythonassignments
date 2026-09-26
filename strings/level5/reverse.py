sentence = input("Enter a sentence: ")

words = sentence.split()
result = ""

for word in words:
    reverse = ""

    for char in word:
        reverse = char + reverse

    result = result + reverse + " "

print(result)