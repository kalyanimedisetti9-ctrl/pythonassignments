student = {
    "name": "Kalyani",
    "age": 18,
    "course": "Computer Engineering"
}

try:
    key = input("Enter key: ")

    if key.strip() == "":
        raise ValueError("Key cannot be empty")

    print("Value:", student[key])

except ValueError as e:
    print("Error:", e)

except KeyError:
    print("Error: Key does not exist")

except TypeError:
    print("Error: Invalid key type")