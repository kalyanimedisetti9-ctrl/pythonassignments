# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Welcome to Python\n")
    file.write("File Handling Example")

print("Data written successfully")

# Reading from the file
with open("sample.txt", "r") as file:
    data = file.read()
    print("\nFile Contents:")
    print(data)