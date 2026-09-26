students = [
    "101,Kalyani,20,Computer Engineering,85\n",
    "102,Ravi,21,Computer Engineering,72\n",
    "103,Sita,20,Computer Engineering,90\n",
    "104,Ram,21,Computer Engineering,68\n"
]

with open("students.txt", "w") as file:
    file.writelines(students)

print("Multiple student records written successfully")