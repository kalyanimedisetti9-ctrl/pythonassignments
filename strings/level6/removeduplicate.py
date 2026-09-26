sentence = "python is easy python is useful"

words = sentence.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

print(" ".join(result))