with open("sample.txt", "r") as file:
    data = file.read()

with open("lowercase.txt", "w") as file:
    file.write(data.lower())

print("Text converted to lowercase")