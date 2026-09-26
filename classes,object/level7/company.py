class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name):
        self.employees.append(name)
        print(name, "added successfully")

    def remove_employee(self, name):
        if name in self.employees:
            self.employees.remove(name)
            print(name, "removed successfully")
        else:
            print(name, "not found")

    def search_employee(self, name):
        if name in self.employees:
            print(name, "is working in the company")
        else:
            print(name, "not found")

    def display_employees(self):
        print("Company:", self.company_name)
        print("Employees:")

        for employee in self.employees:
            print(employee)


company = Company("ABC Technologies")

company.add_employee("Kalyani")
company.add_employee("Ravi")
company.add_employee("Anitha")
company.add_employee("Kiran")

print()

company.display_employees()

print()

company.search_employee("Ravi")

print()

company.remove_employee("Anitha")

print()

company.display_employees()