event1 = {"Kalyani", "Ravi", "Anu", "Suresh"}
event2 = {"Ravi", "Priya", "Rahul", "Anu"}

print("Students who attended exactly one event:")

for student in event1:
    if student not in event2:
        print(student)

for student in event2:
    if student not in event1:
        print(student)