file = open("sample.txt", "r")

print("Initial Position:", file.tell())

file.read(7)
print("Position after reading 7 characters:", file.tell())

file.seek(0)
print("Position after seek(0):", file.tell())

file.seek(5)
print("Position after seek(5):", file.tell())

data = file.read()
print("Remaining Data:", data)

file.close()