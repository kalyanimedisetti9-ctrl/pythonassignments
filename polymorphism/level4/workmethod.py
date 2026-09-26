class Developer:
    def work(self):
        print("Developer writes code")

class Tester:
    def work(self):
        print("Tester tests software")

class Manager:
    def work(self):
        print("Manager manages the team")


def assign_work(employee):
    employee.work()


assign_work(Developer())
assign_work(Tester())
assign_work(Manager())