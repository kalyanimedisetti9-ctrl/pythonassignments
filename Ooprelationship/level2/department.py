class Department:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Department:", self.name)


class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR"),
            Department("Finance")
        ]

    def display_departments(self):
        print("Company Departments:")
        for department in self.departments:
            department.display()


company = Company()
company.display_departments()
