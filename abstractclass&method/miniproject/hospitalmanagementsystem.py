from abc import ABC, abstractmethod

class HospitalEmployee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

    def show_name(self):
        print("Employee Name:", self.name)

class Doctor(HospitalEmployee):
    def work(self):
        print("Doctor treats patients")

class Nurse(HospitalEmployee):
    def work(self):
        print("Nurse takes care of patients")

class Receptionist(HospitalEmployee):
    def work(self):
        print("Receptionist manages appointments")

employees = [
    Doctor("Dr. Ravi"),
    Nurse("Anitha"),
    Receptionist("Sita")
]

for employee in employees:
    employee.show_name()
    employee.work()