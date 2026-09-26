def search_key(data, key):
    try:
        print("Value:", data[key])
    except KeyError:
        print("Key not found")

student = {"name": "Kalyani", "age": 20}

search_key(student, "name")
search_key(student, "marks")