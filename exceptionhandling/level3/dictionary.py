student = {
    "name": "Kalyani",
    "age": 18,
    "course": "Computer Engineering"
}

try:
    key = input("Enter dictionary key: ")

    if not isinstance(key, str):
        raise TypeError("Key must be a string")

    print("Value:", student[key])

except KeyError:
    print("Error: Key not found")

except TypeError:
    print("Error: Invalid key type")