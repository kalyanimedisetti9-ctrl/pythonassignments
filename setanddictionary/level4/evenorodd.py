numbers = {
    "a": 10,
    "b": 15,
    "c": 20,
    "d": 25,
    "e": 30
}

even = 0
odd = 0

for value in numbers.values():
    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)