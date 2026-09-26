sentence = input("Enter a sentence: ")
letter = input("Enter starting letter: ")

words = sentence.split()

for word in words:
    if word.lower().startswith(letter.lower()):
        print(word)