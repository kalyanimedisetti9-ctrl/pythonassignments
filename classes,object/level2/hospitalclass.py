class Hospital:
    def __init__(self, patient_name, age, disease, doctor_name):
        self.patient_name = patient_name
        self.age = age
        self.disease = disease
        self.doctor_name = doctor_name

patient1 = Hospital("Kalyani", 18, "Fever", "Dr. Ravi")
patient2 = Hospital("Anitha", 25, "Cold", "Dr. Suresh")
patient3 = Hospital("Ravi", 30, "Diabetes", "Dr. Kumar")

print("Patient:", patient1.patient_name)
print("Age:", patient1.age)
print("Disease:", patient1.disease)
print("Doctor:", patient1.doctor_name)

print()

print("Patient:", patient2.patient_name)
print("Age:", patient2.age)
print("Disease:", patient2.disease)
print("Doctor:", patient2.doctor_name)

print()

print("Patient:", patient3.patient_name)
print("Age:", patient3.age)
print("Disease:", patient3.disease)
print("Doctor:", patient3.doctor_name)