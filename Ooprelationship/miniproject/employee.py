class Employee:
    def work(self):
        print("Employee is working")


class Doctor(Employee):
    def treat_patient(self):
        print("Doctor is treating patient")


class Nurse(Employee):
    def care_patient(self):
        print("Nurse is caring for patient")


class Patient:
    def __init__(self, name):
        self.name = name


class BillingService:
    def generate_bill(self, patient, amount):
        print("Patient:", patient)
        print("Bill: ₹", amount)


class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor(),
            Doctor()
        ]

        self.patients = [
            Patient("Kalyani"),
            Patient("Ravi")
        ]

    def create_bill(self):
        billing = BillingService()
        billing.generate_bill(self.patients[0].name, 5000)


hospital = Hospital()

hospital.doctors[0].work()
hospital.doctors[0].treat_patient()

hospital.create_bill()