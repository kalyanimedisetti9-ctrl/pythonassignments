class Doctor:
    def __init__(self, name):
        self.name = name


class Patient:
    def __init__(self, name):
        self.name = name


class BillingService:
    def generate_bill(self, patient, amount):
        print(f"Bill for {patient}: ₹{amount}")


class Hospital:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Ravi"),
            Doctor("Dr. Sita")
        ]

        self.patients = [
            Patient("Kalyani"),
            Patient("Ramesh")
        ]

    def create_bill(self):
        billing = BillingService()
        billing.generate_bill(self.patients[0].name, 5000)


hospital = Hospital()
hospital.create_bill()