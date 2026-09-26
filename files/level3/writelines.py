file = open("sample.txt", "w")

lines = [
    "Welcome to Python\n",
    "File Handling\n",
    "Python Programming\n"
]

file.writelines(lines)

file.close()

print("Multiple lines written successfully")