# Create and write data
file = open("sample.txt", "w")
file.write("Welcome to Python\n")
file.write("Learning File Handling")
file.close()

# Read data
file = open("sample.txt", "r")
print("Original content:")
print(file.read())
file.close()

# Append new data
file = open("sample.txt", "a")
file.write("\nThis is appended content")
file.close()

# Read updated data
file = open("sample.txt", "r")
print("\nUpdated content:")
print(file.read())
file.close()