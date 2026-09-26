words = {
    "Python": "A programming language",
    "Computer": "An electronic device",
    "Database": "A collection of data",
    "Program": "A set of instructions"
}

word = input("Enter a word: ")

if word in words:
    print("Meaning:", words[word])
else:
    print("Word not found")