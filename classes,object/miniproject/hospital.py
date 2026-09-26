class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print("Patient:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def display(self):
        print("Doctor:", self.name)
        print("Specialization:", self.specialization)


class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display(self):
        print("Patient:", self.patient.name)
        print("Doctor:", self.doctor.name)
        print("Date:", self.date)


patient = Patient("Kalyani", 18, "Fever")
doctor = Doctor("Dr. Ravi", "General Physician")

appointment = Appointment(patient, doctor, "18-08-2026")

patient.display()
print()
doctor.display()
print()
appointment.display()