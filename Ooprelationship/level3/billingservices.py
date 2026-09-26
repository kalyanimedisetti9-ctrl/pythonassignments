class BillingService:
    def generate_bill(self, patient, amount):
        print(f"Patient: {patient}")
        print(f"Hospital Bill: ₹{amount}")


class Hospital:
    def create_bill(self, patient, amount):
        billing = BillingService()
        billing.generate_bill(patient, amount)


hospital = Hospital()
hospital.create_bill("Ravi", 5000)