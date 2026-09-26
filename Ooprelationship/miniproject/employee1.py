class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def code(self):
        print("Developer is coding")


class Manager(Employee):
    def manage(self):
        print("Manager is managing")


class Department:
    def __init__(self, name):
        self.name = name


class PaymentService:
    def pay_salary(self, employee, salary):
        print("Salary paid to", employee, "₹", salary)


class PayrollService:
    def process_salary(self, employee, salary):
        payment = PaymentService()
        payment.pay_salary(employee, salary)


class Company:
    def __init__(self):
        self.departments = [
            Department("IT"),
            Department("HR")
        ]

        self.employees = [
            Developer(),
            Manager()
        ]

    def process_payroll(self):
        payroll = PayrollService()

        payroll.process_salary("Ravi", 30000)
        payroll.process_salary("Sita", 40000)


company = Company()

company.employees[0].work()
company.employees[0].code()

company.employees[1].work()
company.employees[1].manage()

company.process_payroll()