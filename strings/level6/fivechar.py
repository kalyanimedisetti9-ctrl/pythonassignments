sentence = "Python programming is very interesting"

words = sentence.split()
result = []

for word in words:
    if len(word) > 5:
        result.append(word)

print(result)