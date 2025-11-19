class Employee:
    def role(self):
        print("Employee works in the company")

class Developer(Employee):
    def role(self):
        print("Developer writes code")

class Tester(Employee):
    def role(self):
        print("Tester tests the software")

# Different child classes show different behavior (Polymorphism)
# for emp in [Developer(), Tester(), Employee()]:
#     emp.role()
