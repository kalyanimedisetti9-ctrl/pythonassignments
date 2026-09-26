class HospitalPatient:
    def __init__(self, name, age, disease, room_no):
        self.name = name
        self.age = age
        self.disease = disease
        self.room_no = room_no

    def display(self):
        print("Patient Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Room Number:", self.room_no)

p = HospitalPatient("Ravi", 35, "Fever", 101)

p.display()