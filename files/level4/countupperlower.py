with open("sample.txt", "r") as file:
    data = file.read()

uppercase = 0
lowercase = 0

for ch in data:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1

print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)