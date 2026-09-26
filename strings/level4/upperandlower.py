text = "Hello Python"

uppercase = 0
lowercase = 0

for char in text:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1

print("Uppercase characters:", uppercase)
print("Lowercase characters:", lowercase)