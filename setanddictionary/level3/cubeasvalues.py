cubes = {}

for num in range(1, 11):
    cubes[num] = num ** 3

print("Numbers and Cubes:")

for key, value in cubes.items():
    print(key, ":", value)