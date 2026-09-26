class InvalidPatientError(Exception):
    pass


class Hospital:
    def register_patient(self, name, age):
        try:
            if name == "":
                raise InvalidPatientError("Patient name cannot be empty")

            if age <= 0:
                raise InvalidPatientError("Invalid patient age")

            print("Patient registered successfully")
            print("Name:", name)
            print("Age:", age)

        except InvalidPatientError as e:
            print("Error:", e)


hospital = Hospital()
hospital.register_patient("Kalyani", 20)
hospital.register_patient("", 20)
hospital.register_patient("Ravi", -5)