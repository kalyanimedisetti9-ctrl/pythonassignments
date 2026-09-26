file = open("sample.txt", "r")

print("Initial position:", file.tell())

data = file.read(5)

print("Data:", data)
print("Current position:", file.tell())

file.close()