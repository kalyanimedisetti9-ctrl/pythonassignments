class InvalidPatientError(Exception):
    pass

class DoctorUnavailableError(Exception):
    pass

class InvalidAppointmentError(Exception):
    pass


class Hospital:
    def __init__(self):
        self.doctors = ["Dr. Ravi", "Dr. Sita"]

    def book_appointment(self, patient_name, age, doctor, date):
        try:
            if patient_name == "" or age <= 0:
                raise InvalidPatientError("Invalid patient details")

            if doctor not in self.doctors:
                raise DoctorUnavailableError("Doctor is unavailable")

            if date == "":
                raise InvalidAppointmentError("Invalid appointment date")

            print("Appointment booked successfully")
            print("Patient:", patient_name)
            print("Doctor:", doctor)
            print("Date:", date)

        except InvalidPatientError as e:
            print("Error:", e)
        except DoctorUnavailableError as e:
            print("Error:", e)
        except InvalidAppointmentError as e:
            print("Error:", e)


hospital = Hospital()

hospital.book_appointment(
    "Kalyani", 20, "Dr. Ravi", "20-08-2026"
)

hospital.book_appointment(
    "Ravi", 25, "Dr. Kumar", "20-08-2026"
)

hospital.book_appointment(
    "", 20, "Dr. Sita", "20-08-2026"
)