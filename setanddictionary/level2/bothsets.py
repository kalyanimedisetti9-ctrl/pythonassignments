set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

unique_numbers = set()

for num in set1:
    unique_numbers.add(num)

for num in set2:
    unique_numbers.add(num)

print("Unique numbers:", unique_numbers)