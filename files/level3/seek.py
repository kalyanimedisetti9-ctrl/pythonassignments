file = open("sample.txt", "r")

print("Initial position:", file.tell())

file.seek(5)

print("New position:", file.tell())

data = file.read()
print("Data:", data)

file.close()