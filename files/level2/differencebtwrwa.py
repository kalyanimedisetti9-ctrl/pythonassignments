# r mode - Read existing content
file = open("sample.txt", "r")
print("Read mode:")
print(file.read())
file.close()


# w mode - Overwrites existing content
file = open("sample.txt", "w")
file.write("New content using w mode")
file.close()

print("\nw mode: Content overwritten")


# a mode - Adds content at the end
file = open("sample.txt", "a")
file.write("\nNew content using a mode")
file.close()

print("a mode: Content appended")