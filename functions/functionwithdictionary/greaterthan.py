def greater_than_50(data):
    result = []

    for key, value in data.items():
        if value > 50:
            result.append(key)

    return result

marks = {
    "Maths": 75,
    "Physics": 45,
    "Python": 90,
    "English": 50
}

print(greater_than_50(marks))