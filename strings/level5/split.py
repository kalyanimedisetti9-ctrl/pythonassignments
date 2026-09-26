sentence = input("Enter a sentence: ")

count = 0
inside_word = False

for char in sentence:
    if char != " " and inside_word == False:
        count += 1
        inside_word = True
    elif char == " ":
        inside_word = False

print("Number of words:", count)